import streamlit as st
from pages.db import get_connection

def render_update_salle():
    st.subheader("✏️ Modifier une salle")

    conn = get_connection()
    if not conn:
        return
    
    try:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM salle_hospitalisation
        """)
        salles = cursor.fetchall()

        # Si on a rien trouver afficher un message
        if not salles:
            st.info("ℹ️ Aucune salle trouvé.")
        
        salles_options = [f"{num_salle} {type_chambre} (ID: {id_salle_hospitalisation})" for num_salle, type_chambre, id_salle_hospitalisation in salles]

        selected = st.selectbox("Selectionnez une salle", salles_options)

        if selected:
            salle_id = int(selected.split("ID: ")[1].replace(")", ""))


            cursor.execute("SELECT * FROM salle_hospitalisation WHERE id_salle_hospitalisation = %s", (salle_id,))
            current = cursor.fetchone()

            # Nouvelle from pour changes les infos
            with st.form("update_from"):
                new_num_salle = st.number_input("Numero Salle*", step=1, format="%d", value=1, min_value = 1, max_value=100)
                type_options = ["Individuelle", "Double", "Chambre commune"]
                new_type_chambre = st.selectbox("Type Chambre*", type_options)

                if st.form_submit_button("Mettre a jour"):
                    cursor.execute("""
                        UPDATE salle_hospitalisation SET num_salle=%s, type_chambre=%s
                        WHERE id_salle_hospitalisation=%s""",
                        (new_num_salle, new_type_chambre, salle_id)
                        )
                    conn.commit()
                    st.success("☑️ Salle mis a jour!")
    
    except Exception as e:
        st.error(f"❌ Erreur: {e}")
    finally:
        conn.close()

        