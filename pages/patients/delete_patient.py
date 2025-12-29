# pages/clients/delete_customer.py
import streamlit as st
from pages.db import get_connection

def render_delete_patient():
    """Render the 'Delete Customer' tab"""
    st.header("🗑️ Supprimer un patient")
    
    conn = get_connection()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_patient, nom_patient, prenom_patient FROM patient;
        """)
        clients = cursor.fetchall()
        
        if not clients:
            st.info("ℹ️ Aucun client trouvé.")
            return
        
        # Client selection with order count
        patient_options = [f"{nom} {prenom} (ID: {id})" 
                         for id, nom, prenom in clients]
        
        selected = st.selectbox("Sélectionnez un client", patient_options)
        
        if selected:
            patient_id = int(selected.split("ID: ")[1].split(")")[0])
            
            # if order_count > 0:
            #     st.error(f"⚠️ Ce client a {order_count} commande(s). La suppression supprimera aussi ses commandes.")
            
            confirm = st.checkbox("Je confirme la suppression")
            
            if confirm and st.button("Supprimer définitivement", type="secondary"):
                cursor.execute("DELETE FROM patient WHERE id_patient = %s", (patient_id,))
                conn.commit()
                st.success(f"✅ Client supprimé!")
    except Exception as e:
        st.error(f"❌ Erreur: {e}")
    finally:
        conn.close()