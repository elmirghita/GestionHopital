import streamlit as st
from pages.db import get_connection

def render_add_departement():
    st.subheader("➕ Ajouter un département")

    with st.form("add_departement"):
        nom = st.text_input("Nom du département*")
        submitted = st.form_submit_button("Ajouter", type="primary")

    if submitted:
        if nom:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO departement (nom_departement) VALUES (%s)",
                    (nom,)
                )
                conn.commit()
                st.success("✅ Département ajouté")
            except Exception as e:
                st.error(f"❌ Erreur : {e}")
            finally:
                conn.close()
        else:
            st.warning("⚠️ Champ obligatoire")
