import streamlit as st 
from pages.db import get_connection

def render_add_specialite():
    st.subheader("➕ Ajouter une spécialité")

    with st.form("add_specialite"):
        nom = st.text_input("Nom de la spécialité*")
        submitted = st.form_submit_button("Ajouter", type="primary")

    if submitted:
        if nom:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO specialite (type_specialite) VALUES (%s)",
                    (nom,)
                )
                conn.commit()
                st.success("✅ Spécialité ajoutée")
            except Exception as e:
                st.error(f"❌ Erreur : {e}")
            finally:
                conn.close()
        else:
            st.warning("⚠️ Champ obligatoire")