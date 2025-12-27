import streamlit as st
from pages.db import get_connection

def render_add_salle():
    st.subheader("➕ Nouvelle chambre")

    conn = get_connection()
    if not conn:
        return
    
    
    with st.form("add_salle_form", clear_on_submit=True):

        num_salle = st.number_input("Numero Salle*", step=1, format="%d", value=1, min_value = 1, max_value=100)
        type_options = ["Individuelle", "Double", "Chambre commune"]
        type_chambre = st.selectbox("Type Chambre*", type_options)

        
        submitted = st.form_submit_button("Ajouter une salle", type="primary")

        if submitted and num_salle and type_chambre:
            try:
                conn = get_connection()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO salle_hospitalisation (num_salle, type_chambre)
                        VALUES (%s, %s)""",
                        (num_salle, type_chambre.strip())
                    )
                    conn.commit()
                    st.success(f"✅ Salle {num_salle} {type_chambre} ajoute avec succes")
            except Exception as e:
                st.error(f"❌ Erreur: {e}")
            finally:
                if conn:
                    conn.close()
        elif submitted:
            st.warning("⚠️ Veuillez remplir toute les champs")

