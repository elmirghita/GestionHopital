import streamlit as st


from pages.ordonnance_medical.add_ordonnance_medical import render_add_ordonnance_medical
from pages.ordonnance_medical.delete_ordonnance_medical import render_delete_ordonnance_medical
from pages.ordonnance_medical.display_ordonnance_medical import render_display_ordonnance_medical

st.set_page_config(page_title="Gestion des ordonnances medicales", layout="wide")
st.title("🏥 Gestion des ordonnances medicales")

tab_add, tab_delete,tab_display = st.tabs(
    [
        "➕ Nouvelle ordonnance medicale ",
        "🗑️ Supprimer une ordonnance medicale ",
        "📋 Liste des ordonnances medicales"
    ]
)


with tab_add:
    render_add_ordonnance_medical()

with tab_delete:
    render_delete_ordonnance_medical()

with tab_display:
    render_display_ordonnance_medical()
