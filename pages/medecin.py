import streamlit as st


from pages.medecin.add_medecin import render_add_medecin
from pages.medecin.update_medecin import render_update_medecin
from pages.medecin.delete_medecin import render_delete_medecin
from pages.medecin.display_medecin import render_display_medecin

st.set_page_config(page_title="Gestion des medecins", layout="wide")
st.title("🏥 Gestion des medecins")

tab_add, tab_update, tab_delete, tab_display = st.tabs(
    [
        "➕ Nouvelle Medecin",
        "✏️ Modifier Medecin",
        "🗑️ Supprimer Medecin",
        "📋 Liste des Medecins"
    ]
)

with tab_add:
    render_add_medecin()

with tab_update:
    render_update_medecin()

with tab_delete:
    render_delete_medecin()

with tab_display:
    render_display_medecin()
