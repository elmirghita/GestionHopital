# pages/customers.py - Main orchestrator
import streamlit as st

# Import each module directly
from pages.patients.add_patient import render_add_customer
from pages.patients.update_patient import render_update_customer
from pages.patients.delete_patient import render_delete_customer
from pages.patients.display_patient import render_display_customers

# Page configuration
st.set_page_config(page_title="Gestion des Patients", layout="wide")
st.title("👥 Gestion des Patients")

# Create tabs
tab_new, tab_update, tab_delete, tab_display = st.tabs(
    ["➕ Nouveau Patient", "✏️ Modifier Patient", "🗑️ Supprimer Patient", "📋 Afficher tous"]
)

# Render each tab from its module
with tab_new:
    render_add_customer()

with tab_update:
    render_update_customer()

with tab_delete:
    render_delete_customer()

with tab_display:
    render_display_customers()