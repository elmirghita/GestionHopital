# pages/dashboard.py
import streamlit as st
import pandas as pd
from pages.db import get_connection

# Chargement des données
def load_data():
    conn = get_connection()
    if conn is None:
        return None, None, None, None, None

    clients = pd.read_sql("SELECT COUNT(*) AS total_clients FROM client", conn)
    commandes = pd.read_sql(
        "SELECT COUNT(*) AS total_cmd, SUM(lc.qte_cmd * p.prix_unitaire) AS ca "
        "FROM commande c "
        "JOIN ligne_commande lc ON c.num_cmd = lc.num_commande "
        "JOIN produit p ON lc.code_produit = p.code_produit", conn
    )
    ruptures = pd.read_sql("SELECT COUNT(*) AS ruptures FROM stock WHERE quantite_stock = 0", conn)
    
    ventes_journalieres = pd.read_sql(
        "SELECT date_cmd, COUNT(*) AS nb_cmd "
        "FROM commande "
        "GROUP BY date_cmd ORDER BY date_cmd", conn
    )
    
    top_produits = pd.read_sql(
        "SELECT p.libelle_produit, SUM(lc.qte_cmd) AS total_vendu "
        "FROM ligne_commande lc "
        "JOIN produit p ON lc.code_produit = p.code_produit "
        "GROUP BY p.libelle_produit "
        "ORDER BY total_vendu DESC LIMIT 10", conn
    )
    
    conn.close()
    return clients, commandes, ruptures, ventes_journalieres, top_produits

# Titre
st.title("Dashboard de Gestion")

# Chargement des données
clients, commandes, ruptures, ventes_journalieres, top_produits = load_data()
if clients is None:
    st.stop()

# KPIs
col1, col2, col3, col4 = st.columns(4)
col1.metric("Clients", int(clients.total_clients[0]))
col2.metric("Commandes", int(commandes.total_cmd[0]))
col3.metric("Chiffre d'affaires", f"{float(commandes.ca[0]):,.2f} DH")
col4.metric("Produits en rupture", int(ruptures.ruptures[0]))

st.markdown("---")

# Commandes dans le temps
st.subheader("Commandes dans le temps")
st.line_chart(ventes_journalieres.set_index('date_cmd')['nb_cmd'])

st.markdown("---")

# Top produits
st.subheader("Top 10 Produits vendus")
st.bar_chart(top_produits.set_index('libelle_produit')['total_vendu'])
