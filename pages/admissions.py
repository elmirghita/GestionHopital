import streamlit as st


from pages.admissions.add_admissions import render_add_admission

from pages.admissions.update_admission import render_update_admission
from pages.admissions.delete_admission import render_delete_admission
from pages.admissions.display_admission import render_display_admission

st.set_page_config(page_title="Gestion des Admissions", layout="wide")
st.title("🏥 Gestion des Admissions")

tab_add, tab_update, tab_delete, tab_display = st.tabs(
    [
        "➕ Nouvelle Admission",
        "✏️ Modifier Admission",
        "🗑️ Supprimer Admission",
        "📋 Liste des Admissions"
    ]
)

with tab_add:
    render_add_admission()

with tab_update:
    render_update_admission()

with tab_delete:
    render_delete_admission()

with tab_display:
    render_display_admission()
