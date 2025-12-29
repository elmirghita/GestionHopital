import streamlit as st
from pages.db import get_connection


from pages.salle_hospitalisation.add_salle import render_add_salle
from pages.salle_hospitalisation.update_salle import render_update_salle
from pages.salle_hospitalisation.delete_salle import render_delete_salle
from pages.salle_hospitalisation.display_salle import render_display_salle

st.set_page_config(page_title="Gestion des Salles", layout="wide")
st.title("🏥 Gestion des Salles")

tab_new, tab_update, tab_delete, tab_display = st.tabs(
        ["➕ Nouveau Salle", "✏️ Modifier Salle", "🗑️ Supprimer Salle", "📋 Afficher tous"]
)

with tab_new:
    render_add_salle()
with tab_update:
    render_update_salle()
with tab_delete:
    render_delete_salle()
with tab_display:
    render_display_salle()