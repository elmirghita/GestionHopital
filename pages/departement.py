import streamlit as st


from pages.departement.add_departement import render_add_departement
from pages.departement.update_departement import render_update_departement
from pages.departement.delete_departement import render_delete_departement
from pages.departement.display_departement import render_display_departement

st.set_page_config(page_title="Gestion des departements", layout="wide")
st.title("🏥 Gestion des departements")

tab_add, tab_update, tab_delete, tab_display = st.tabs(
    [
        "➕ Nouvelle Departement",
        "✏️ Modifier Departement",
        "🗑️ Supprimer Departement",
        "📋 Liste des Departements"
    ]
)

with tab_add:
    render_add_departement()

with tab_update:
    render_update_departement()

with tab_delete:
    render_delete_departement()

with tab_display:
    render_display_departement()
