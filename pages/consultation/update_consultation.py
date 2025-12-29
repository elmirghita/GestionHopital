import streamlit as st
from pages.db import get_connection
from datetime import date, datetime

def render_update_consultation():
    st.header("✏️ Modifier une consultation")

    conn = get_connection()
    if not conn:
        st.error("Connexion impossible")
        return

    try:
        conn.rollback()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_consultation,
                   date_consultation,
                   diagnostic
            FROM consultation
            ORDER BY date_consultation DESC
        """)
        consultations = cursor.fetchall()

        if not consultations:
            st.info("Aucune consultation à modifier")
            return

        consult_dict = {
            f"Consultation {c[0]} | {c[1]}": c
            for c in consultations
        }

        selected = st.selectbox(
            "Sélectionnez une consultation",
            consult_dict.keys(),
            key="update_consultation_select"
        )

        selected_consult = consult_dict[selected]

        new_date = st.date_input(
            "📅 Date",
            value=selected_consult[1],
            key="update_consultation_date"
        )

        new_diag = st.text_area(
            "🩺 Diagnostic",
            value=selected_consult[2],
            key="update_consultation_diag"
        )

        new_time = datetime.now().time().replace(microsecond=0)
        st.info(f"⏰ Nouvelle heure automatique : {new_time}")

        if st.button("Mettre à jour", key="update_consultation_btn"):
            if not new_diag.strip():
                st.warning("Le diagnostic est obligatoire")
                return

            cursor.execute("""
                UPDATE consultation
                SET date_consultation = %s,
                    heure = %s,
                    diagnostic = %s
                WHERE id_consultation = %s
            """, (
                new_date,
                new_time,
                new_diag,
                selected_consult[0]
            ))

            conn.commit()
            st.success("✅ Consultation mise à jour")


    except Exception as e:
        conn.rollback()
        st.error(f"❌ Erreur : {e}")

    finally:
        conn.close()
