import streamlit as st

from pages.facture.add_facture import render_add_facture
from pages.facture.update_facture import render_update_facture
from pages.facture.display_facture import render_display_facture
from pages.facture.delete_facture import render_delete_facture

st.set_page_config(page_title="Gestion des factures", layout="wide")
st.title("💳 Gestion des facutres")

tab_add, tab_update, tab_delete, tab_display = st.tabs(
    [
        "➕ Nouvelle Facture",
        "✏️ Modifier Facture",
        "🗑️ Supprimer Facture",
        "📋 Liste des Factures"
    ]
)

with tab_add:
    render_add_facture()

with tab_update:
    render_update_facture()

with tab_delete:
    render_delete_facture()

with tab_display:
    render_display_facture()