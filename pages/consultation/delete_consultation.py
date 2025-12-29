import streamlit as st
from pages.db import get_connection

def render_delete_consultation():
    st.header("🗑️ Supprimer une consultation")

    conn = get_connection()
    if not conn:
        st.error("Connexion impossible")
        return

    try:
        conn.rollback()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id_consultation, date_consultation
            FROM consultation
            ORDER BY date_consultation DESC
        """)
        consultations = cursor.fetchall()

        if not consultations:
            st.info("Aucune consultation à supprimer")
            return

        consult_dict = {
            f"Consultation {c[0]} | {c[1]}": c[0]
            for c in consultations
        }

        selected = st.selectbox(
            "Sélectionnez une consultation",
            consult_dict.keys()
        )

        confirm = st.checkbox("⚠️ Je confirme la suppression")

        if confirm and st.button("Supprimer définitivement"):
            cursor.execute(
                "DELETE FROM consultation WHERE id_consultation = %s",
                (consult_dict[selected],)
            )
            conn.commit()
            st.success("✅ Consultation supprimée")


    except Exception as e:
        conn.rollback()
        st.error(f"❌ Erreur : {e}")

    finally:
        conn.close()
