# pages/customers/add_customer.py
import streamlit as st
from pages.db import get_connection

def render_add_patient():
    """Render the 'Add Customer' tab"""
    st.header("➕ Ajouter un nouveau Patient")
    
    with st.form("add_patient_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            nom = st.text_input("Nom*", max_chars=50)
            prenom = st.text_input("Prénom*", max_chars=50)
        
        with col2:
            tel = st.text_input("Tel*", max_chars=50)
            cin = st.text_input("CIN*", max_chars=8)
        
        submitted = st.form_submit_button("Ajouter le patient", type="primary")
        
        if submitted and nom and prenom:
            try:
                conn = get_connection()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO patient (nom_patient, prenom_patient, tel_patient, cin_patient) VALUES (%s, %s, %s, %s)",
                        (nom, prenom, tel, cin)
                    )
                    conn.commit()
                    st.success(f"✅ Patient {prenom} {nom} ajouté avec succès")
            except Exception as e:
                st.error(f"❌ Erreur: {e}")
            finally:
                if conn:
                    conn.close()
        elif submitted:
            st.warning("⚠️ Veuillez remplir toute les champs")