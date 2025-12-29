import streamlit as st
from pages.db import get_connection
from utils.fk_helpers import get_or_create_id

def render_add_medecin():
    st.header("➕ Ajouter un nouveau Medecin")

    with st.form("add_medecin_form", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            nom = st.text_input("Nom*", max_chars=10)
            prenom = st.text_input("Prenom*",max_chars=10)
            tel = st.text_input("Tel*", max_chars=30)

        with col2:
            specialite = st.text_input("specialite*", max_chars=15)
            departement = st.text_input("departement*", max_chars=20)

        submitted = st.form_submit_button("Ajouter le medecin", type="primary")

        
    if submitted:
        if nom and prenom and specialite and departement:
            try:
                conn = get_connection()

                id_specialite = get_or_create_id(
                    conn, "specialite", "type_specialite", specialite
                )

                id_departement = get_or_create_id(
                    conn, "departement", "nom_departement", departement
                )

                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO medecin 
                    (nom_medecin, prenom_medecin, tel_medecin,id_specialite, id_departement)
                    VALUES (%s, %s, %s, %s, %s)
                """, (nom, prenom, tel,id_specialite, id_departement))

                conn.commit()
                st.success("✅ Médecin ajouté avec succès")

            except Exception as e:
                st.error(f"❌ Erreur : {e}")
            finally:
                conn.close()
        else:
            st.warning("⚠️ Veuillez remplir tous les champs obligatoires")