import streamlit as st
from pages.db import get_connection

def render_delete_ordonnance():
    st.header("🗑️ Supprimer une ordonnance")

    conn = get_connection()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id_ordonnance, date_ordonnance, remarques, type_ordonnance FROM ordonnance;
        """)
        ordonnances = cursor.fetchall()

        if not ordonnances:
            st.info("ℹ️ Aucune ordonnance trouvé.")
            return
        
        # ordonnance selection with order count
        ordonnance_options = [f"(ID: {ord[0]})" 
                         for ord in ordonnances]
        
        selected = st.selectbox("Sélectionnez un ordonnance", ordonnance_options,key="delete_ordonnance_selectbox")
        
        if selected:
            ordonnance_id = int(selected.split("ID: ")[1].split(")")[0])
            
            # if order_count > 0:
            #     st.error(f"⚠️ Ce ordonnance a {order_count} commande(s). La suppression supprimera aussi ses commandes.")
                    
        
            confirm = st.checkbox("Je confirme la suppression")
            
            if confirm and st.button("Supprimer définitivement", type="secondary"):
                cursor.execute("DELETE FROM ordonnance WHERE id_ordonnance = %s", (ordonnance_id,))
                conn.commit()
                st.error(f"✅ Ordonnance supprimé!")
                st.rerun()
    except Exception as e:
        st.error(f"❌ Erreur: {e}")
    finally:
        conn.close()