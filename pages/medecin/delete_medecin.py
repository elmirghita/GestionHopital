# pages/medecins/delete_medecin.py
import streamlit as st
from pages.db import get_connection

def render_delete_medecin():
    """Render the 'Delete medecin' tab"""
    st.header("🗑️ Supprimer un medecin")
    
    conn = get_connection()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_medecin, nom_medecin, prenom_medecin FROM medecin;
        """)
        medecins = cursor.fetchall()
        
        if not medecins:
            st.info("ℹ️ Aucun medecin trouvé.")
            return
        
        # medecin selection with order count
        medecin_options = [f"{nom} {prenom} (ID: {id})" 
                         for id, nom, prenom in medecins]
        
        selected = st.selectbox("Sélectionnez un medecin", medecin_options,key="delete_medecin_selectbox")
        
        if selected:
            medecin_id = int(selected.split("ID: ")[1].split(")")[0])
            
            # if order_count > 0:
            #     st.error(f"⚠️ Ce medecin a {order_count} commande(s). La suppression supprimera aussi ses commandes.")
            
            confirm = st.checkbox("Je confirme la suppression")
            
            if confirm and st.button("Supprimer définitivement", type="secondary"):
                cursor.execute("DELETE FROM medecin WHERE id_medecin = %s", (medecin_id,))
                conn.commit()
                st.error(f"✅ medecin supprimé!")
                st.rerun()
    except Exception as e:
        st.error(f"❌ Erreur: {e}")
    finally:
        conn.close()