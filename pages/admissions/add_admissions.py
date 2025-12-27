import streamlit as st
from pages.db import get_connection

def render_add_admission():
    st.subheader("➕ Nouvelle admission")

    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.cursor()

        # =====================
        # Patients
        # =====================
        cursor.execute("""
            SELECT id_patient, nom_patient, prenom_patient
            FROM patient
            ORDER BY nom_patient
        """)
        patients = cursor.fetchall()

        if not patients:
            st.warning("Aucun patient trouvé")
            return

        patient_options = {
            f"{nom} {prenom} (ID: {id})": id
            for id, nom, prenom in patients
        }

        selected_patient = st.selectbox(
            "👤 Patient",
            patient_options.keys()
        )
        id_patient = patient_options[selected_patient]

        # =====================
        # Salles
        # =====================
        cursor.execute("""
            SELECT num_salle, type_chambre
            FROM salle_hospitalisation
            ORDER BY num_salle
        """)
        salles = cursor.fetchall()

        if not salles:
            st.warning("Aucune salle disponible")
            return

        salle_options = {
            f"Salle {num} - {type_}": id_salle
            for num, type_ in salles
        }

        selected_salle = st.selectbox(
            "🛏️ Salle d'hospitalisation",
            salle_options.keys()
        )
        id_salle = salle_options[selected_salle]

        # =====================
        # Motif
        # =====================
        motif = st.text_area("📝 Motif d'admission")

        # =====================
        # Enregistrer
        # =====================
        if st.button("💾 Enregistrer", type="primary"):
            cursor.execute("""
                INSERT INTO admission (motif_admission, id_patient, id_salle)
                VALUES (%s, %s, %s)
            """, (motif, id_patient, id_salle))

            conn.commit()
            st.success("✅ Admission enregistrée")
            st.rerun()

    except Exception as e:
        st.error(f"❌ Erreur : {e}")

    finally:
        conn.close()
