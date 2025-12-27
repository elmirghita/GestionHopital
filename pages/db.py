# pages/db.py
import psycopg2
import streamlit as st
from config import DB_CONFIG

def get_connection():
    """Create and return a database connection"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        st.error("❌ Database connection error")
        st.exception(e)  
