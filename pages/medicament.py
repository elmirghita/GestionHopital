import streamlit as st


from pages.medicament.add_medicament import render_add_medicament
from pages.medicament.delete_medicament import render_delete_medicament
from pages.medicament.display_medicament import render_display_medicament

st.set_page_config(page_title="Gestion des medicaments", layout="wide")
st.title("🏥 Gestion des medicaments")

tab_add, tab_delete, tab_display = st.tabs(
    [
        "➕ Nouvelle medicament",
        "🗑️ Supprimer medicament",
        "📋 Liste des medicaments"
    ]
)


with tab_add:
    render_add_medicament()

with tab_delete:
    render_delete_medicament()

with tab_display:
    render_display_medicament()
