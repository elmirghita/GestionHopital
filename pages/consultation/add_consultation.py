import streamlit as st
from pages.db import get_connection
from datetime import date, datetime

def render_add_consultation():
    st.header("➕ Ajouter une consultation")

    conn = get_connection()
    if not conn:
        st.error("Connexion à la base impossible")
        return

    try:
        conn.rollback()
        cursor = conn.cursor()

        # ================== MÉDECINS ==================
        cursor.execute("""
            SELECT id_medecin, nom_medecin, prenom_medecin
            FROM medecin
            ORDER BY nom_medecin
        """)
        medecins = cursor.fetchall()

        if not medecins:
            st.warning("Aucun médecin trouvé")
            return

        # ================== PATIENTS ==================
        cursor.execute("""
            SELECT id_patient, nom_patient, prenom_patient
            FROM patient
            ORDER BY nom_patient
        """)
        patients = cursor.fetchall()

        if not patients:
            st.warning("Aucun patient trouvé")
            return

        # ================== ORDONNANCES (PAR TYPE) ==================
        cursor.execute("""
            SELECT id_ordonnance, type_ordonnance
            FROM ordonnance
            ORDER BY type_ordonnance
        """)
        ordonnances = cursor.fetchall()

        if not ordonnances:
            st.warning("Aucune ordonnance trouvée")
            return

        # ================== UI ==================
        medecin = st.selectbox(
            "👨‍⚕️ Médecin",
            medecins,
            format_func=lambda m: f"{m[1]} {m[2]} (ID {m[0]})"
        )

        patient = st.selectbox(
            "🧑‍🦱 Patient",
            patients,
            format_func=lambda p: f"{p[1]} {p[2]} (ID {p[0]})"
        )

        ordonnance = st.selectbox(
            "📄 Type d’ordonnance",
            ordonnances,
            format_func=lambda o: f"{o[1]} (ID {o[0]})"
        )

        date_consultation = st.date_input("📅 Date", value=date.today())

        # ⏰ Heure automatique
        heure_consultation = datetime.now().time().replace(microsecond=0)
        st.info(f"⏰ Heure de consultation : {heure_consultation}")

        diagnostic = st.text_area("🩺 Diagnostic")

        if st.button("💾 Enregistrer"):
            if not diagnostic.strip():
                st.warning("Le diagnostic est obligatoire")
                return

            cursor.execute("""
                INSERT INTO consultation
                (date_consultation, heure, diagnostic,
                 id_medecin, id_patient, id_ordonnance)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                date_consultation,
                heure_consultation,
                diagnostic,
                medecin[0],
                patient[0],
                ordonnance[0]
            ))

            conn.commit()
            st.success("✅ Consultation ajoutée avec succès")

    except Exception as e:
        conn.rollback()
        st.error(f"❌ Erreur SQL : {e}")

    finally:
        conn.close()
