import streamlit as st
from pages.db import get_connection

def render_add_medicament():
    st.subheader("➕ Ajouter un medicament")

    with st.form("add_medicament"):
        TYPE_TRAITEMENT = {
            "ORALE": "💊 Voie orale",
            "INJECTABLE": "💉 Injection",
            "TRAITEMENT": "🧪 Traitement",
            "LOCALE": "🧴 Voie locale"      
            }
        type_medicament = st.selectbox("Type de traitement",options=list(TYPE_TRAITEMENT.keys()),format_func=lambda x: TYPE_TRAITEMENT[x])
        nom = st.text_input("Nom du medicament*",max_chars=50)
        submitted = st.form_submit_button("Ajouter", type="primary")

    if submitted:
        if nom:
            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO medicament (nom_medicament, type_medicament) VALUES (%s,%s)",
                    (nom, type_medicament,)
                )
                conn.commit()
                st.success("✅ Medicament ajouté")
            except Exception as e:
                st.error(f"❌ Erreur : {e}")
            finally:
                conn.close()
        else:
            st.warning("⚠️ Champ obligatoire")
