# pages/medecins/update_medecin.py
import streamlit as st
from pages.db import get_connection

def render_update_medecin():
    """Render the 'Update medecin' tab"""
    st.header("✏️ Modifier les informations d'un Medecin")
    
    conn = get_connection()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id_medecin, nom_medecin, prenom_medecin FROM medecin ORDER BY nom_medecin")
        medecins = cursor.fetchall()
        
        if not medecins:
            st.info("ℹ️ Aucun Medecin trouvé.")
            return
        
        # Medecin selection
        medecin_options = [f"{nom} {prenom} (ID: {id})" for id, nom, prenom in medecins]
        selected = st.selectbox("Sélectionnez un medecin", medecin_options)
        
        if selected:
            # Extract ID from selection
            medecin_id = int(selected.split("ID: ")[1].replace(")", ""))
            
            # Get current data
            cursor.execute("SELECT * FROM medecin WHERE id_medecin = %s", (medecin_id,))
            current = cursor.fetchone()
            
            # Update form
            with st.form("update_form"):
                col1, col2 = st.columns(2)
                with col1:
                    new_nom = st.text_input("Nom", value=current[1], max_chars=50)
                    new_prenom = st.text_input("Prénom", value=current[2], max_chars=50)
                    new_tel = st.text_input("Telephone*",value=current[3],max_chars=30)
                with col2:
                    new_specialite = st.text_input("specialite*",value= current[4], max_chars=15)
                    new_departement = st.text_input("departement*",value= current[5], max_chars=20)
                    
                if st.form_submit_button("Mettre à jour"):
                    cursor.execute(
                        "UPDATE medecin SET nom_medecin=%s, prenom_medecin=%s, tel_medecin=%s,type_specialite=%s,nom_departement=%s, WHERE id_medecin=%s",
                        (new_nom, new_prenom,new_specialite,new_departement, medecin_id)
                    )
                    conn.commit()
                    st.success("✅ Medecin mis à jour!")
    except Exception as e:
        st.error(f"❌ Erreur: {e}")
    finally:
        conn.close()