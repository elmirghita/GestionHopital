import streamlit as st

from pages.ligne_facture.add_ligne_facture import render_add_ligne_facture
from pages.ligne_facture.display_ligne_facture import render_display_ligne_facture
from pages.ligne_facture.update_ligne_facture import render_update_ligne_facture
from pages.ligne_facture.delete_ligne_facture import render_delete_ligne_facture
st.set_page_config(page_title="Gestion des factures", layout="wide")
st.title("📄 Ligne facture")

tab_add, tab_update, tab_delete, tab_display = st.tabs(
    [
        "➕ Nouvelle Ligne Facture",
        "✏️ Modifier Ligne Facture",
        "🗑️ Supprimer Ligne Facture",
        "📋 Liste des Ligne Factures"
    ]
)

with tab_add:
    render_add_ligne_facture()

with tab_update:
    render_update_ligne_facture()

with tab_delete:
    render_delete_ligne_facture()

with tab_display:
    render_display_ligne_facture()