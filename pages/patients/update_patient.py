# pages/customers/update_customer.py
import streamlit as st
from pages.db import get_connection

def render_update_customer():
    """Render the 'Update Customer' tab"""
    st.header("✏️ Modifier les informations d'un client")
    
    conn = get_connection()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id_patient, nom_patient, prenom_patient FROM patient ORDER BY nom_patient")
        patients = cursor.fetchall()
        
        if not patients:
            st.info("ℹ️ Aucun client trouvé.")
            return
        
        # Client selection
        patient_options = [f"{nom} {prenom} (ID: {id})" for id, nom, prenom in patients]
        selected = st.selectbox("Sélectionnez un patient", patient_options)
        
        if selected:
            # Extract ID from selection
            patient_id = int(selected.split("ID: ")[1].replace(")", ""))
            
            # Get current data
            cursor.execute("SELECT * FROM patient WHERE id_patient = %s", (patient_id,))
            current = cursor.fetchone()
            
            # Update form
            with st.form("update_form"):
                col1, col2 = st.columns(2)
                with col1:
                    new_nom = st.text_input("Nom", value=current[1], max_chars=50)
                    new_prenom = st.text_input("Prénom", value=current[2], max_chars=50)
                with col2:
                    new_telephone = st.text_input("Tel", value=current[3] or "", max_chars=50)
                    new_cin = st.text_input("CIN", value=current[4] or "", max_chars=8)
                
                if st.form_submit_button("Mettre à jour"):
                    cursor.execute(
                        "UPDATE patient SET nom_patient=%s, prenom_patient=%s, tel_patient=%s, cin_patient=%s WHERE id_patient=%s",
                        (new_nom, new_prenom, new_telephone, new_cin, patient_id)
                    )
                    conn.commit()
                    st.success("✅ Client mis à jour!")
    except Exception as e:
        st.error(f"❌ Erreur: {e}")
    finally:
        conn.close()