import streamlit as st
from pages.db import get_connection

def render_delete_salle():
    st.header("🗑️ Supprimer une salle")

    conn = get_connection()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM salle_hospitalisation
            ORDER BY num_salle;
        """)
        salles = cursor.fetchall()

        if not salles:
            st.info("ℹ️ Aucune salle trouve.")
            return
        
        salle_options = [f"{num_salle} {type_chambre} (ID: {id_salle_hospitalisation})" for num_salle, type_chambre, id_salle_hospitalisation in salles]

        selected = st.selectbox(
            "Selectionnez une salle",
            salle_options,
            key="delete_salle_selectbox"
        )


        if selected:
            salle_id = int(selected.split("ID: ")[1].split(")")[0])
            confirm = st.checkbox("Je confrime la suppression")

            if confirm and st.button("Supprimer definitivement", type="secondary"):
                cursor.execute("DELETE FROM salle_hospitalisation WHERE id_salle_hospitalisation = %s", (salle_id,))
                conn.commit()
                st.error(f"✅ Salle supprime!")
                
    except Exception as e:
        st.error(f"❌ Erreur: {e}")
    finally:
        conn.close()