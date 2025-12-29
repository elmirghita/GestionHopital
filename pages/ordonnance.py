import streamlit as st


from pages.ordonnance.add_ordonnance import render_add_ordonnance
from pages.ordonnance.delete_ordonnance import render_delete_ordonnance
from pages.ordonnance.display_ordonnance import render_display_ordonnance


st.set_page_config(page_title="Gestion des ordonnances", layout="wide")
st.title("🏥 Gestion des ordonnances")

tab_add, tab_delete, tab_display = st.tabs(
    [
        "➕ Nouvelle ordonnance",
        "🗑️ Supprimer ordonnance",
        "📋 Liste des ordonnances"
    ]
)


with tab_add:
    render_add_ordonnance()



with tab_delete:
    render_delete_ordonnance()

with tab_display:
    render_display_ordonnance()