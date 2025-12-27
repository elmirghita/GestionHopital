# pages/customers/utils.py
import streamlit as st

def format_client_name(client_tuple):
    """Format client tuple (id, nom, prenom) for display"""
    id_client, nom, prenom = client_tuple
    return f"{nom} {prenom} (ID: {id_client})"

def get_client_id_from_display(display_string):
    """Extract client ID from display string"""
    try:
        return int(display_string.split("ID: ")[1].replace(")", ""))
    except:
        return None

def display_sidebar_stats():
    """Display client statistics in sidebar"""
    # You can implement this later
    pass