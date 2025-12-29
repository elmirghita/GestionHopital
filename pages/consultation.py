import streamlit as st


from pages.consultation.add_consultation import render_add_consultation
from pages.consultation.update_consultation import render_update_consultation
from pages.consultation.delete_consultation import render_delete_consultation
from pages.consultation.display_consultation import render_display_consultation

st.set_page_config(page_title="Gestion des consultations", layout="wide")
st.title("🏥 Gestion des consultations")

tab_add, tab_update, tab_delete, tab_display = st.tabs(
    [
        "➕ Nouvelle consultation",
        "✏️ Modifier consultation",
        "🗑️ Supprimer consultation",
        "📋 Liste des consultations"
    ]
)

with tab_add:
    render_add_consultation()

with tab_update:
    render_update_consultation()

with tab_delete:
    render_delete_consultation()

with tab_display:
    render_display_consultation()
