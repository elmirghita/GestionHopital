import streamlit as st

from pages.facture.add_facture import render_add_facture

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