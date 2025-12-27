import streamlit as st


from pages.specialite.add_specialite import render_add_specialite
from pages.specialite.update_specialite import render_update_specialite
from pages.specialite.delete_specialite import render_delete_specialite
from pages.specialite.display_specialite import render_display_specialite

st.set_page_config(page_title="Gestion des specialites", layout="wide")
st.title("🏥 Gestion des specialites")

tab_add, tab_update, tab_delete, tab_display = st.tabs(
    [
        "➕ Nouvelle Specialite",
        "✏️ Modifier Specialite",
        "🗑️ Supprimer Specialite",
        "📋 Liste des Specialites"
    ]
)

with tab_add:
    render_add_specialite()

with tab_update:
    render_update_specialite()

with tab_delete:
    render_delete_specialite()

with tab_display:
    render_display_specialite()
