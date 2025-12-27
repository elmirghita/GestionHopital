import streamlit as st
from pages.db import get_connection

def render_update_departement():
    st.subheader("✏️ Modifier un département")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id_departement, nom_departement FROM departement")
    departements = cursor.fetchall()

    if not departements:
        st.info("Aucun département trouvé")
        return

    dep_dict = {d[1]: d[0] for d in departements}

    selected = st.selectbox("Choisir un département", dep_dict.keys())

    nouveau_nom = st.text_input("Nouveau nom", selected)

    if st.button("Mettre à jour"):
        try:
            cursor.execute(
                "UPDATE departement SET nom_departement = %s WHERE id_departement = %s",
                (nouveau_nom, dep_dict[selected])
            )
            conn.commit()
            st.success("✅ Département mis à jour")
        except Exception as e:
            st.error(f"❌ Erreur : {e}")
        finally:
            conn.close()
