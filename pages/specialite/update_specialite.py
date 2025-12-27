import streamlit as st
from pages.db import get_connection

def render_update_specialite():
    st.subheader("✏️ Modifier une spécialité")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id_specialite, type_specialite FROM specialite")
    specialites = cursor.fetchall()

    if not specialites:
        st.info("Aucune spécialité trouvée")
        return

    spec_dict = {s[1]: s[0] for s in specialites}

    selected = st.selectbox("Choisir une spécialité", spec_dict.keys())

    nouveau_nom = st.text_input("Nouveau nom", selected)

    if st.button("Mettre à jour"):
        try:
            cursor.execute(
                "UPDATE specialite SET type_specialite = %s WHERE id_specialite = %s",
                (nouveau_nom, spec_dict[selected])
            )
            conn.commit()
            st.success("✅ Spécialité mise à jour")
        except Exception as e:
            st.error(f"❌ Erreur : {e}")
        finally:
            conn.close()
