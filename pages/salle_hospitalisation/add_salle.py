# import streamlit as st
# from pages.db import get_connection

# def render_add_admission():
#     st.subheader("➕ Nouvelle chambre")

#     conn = get_connection()
#     if not conn:
#         return
    
#     with st.form("add_salle_form", clear_on_submit=True):
#         col1 = set.columns(1)

#         with col1:
#             num_salle = st.