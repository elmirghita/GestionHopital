import streamlit as st

# Define pages with custom titles
home_page = st.Page("pages/home.py", title="Dashboard", icon="🏠")
customers_page = st.Page("pages/customers.py", title="Patients", icon="🤒")
medecin_page = st.Page("pages/medecin.py", title="Medecins", icon="👨‍⚕️")
specialite_page = st.Page("pages/specialite.py", title="Specialites", icon="🩺")
departement_page = st.Page("pages/departement.py", title="Departements", icon="🏥")
analytics_page = st.Page("pages/analytics.py", title="Data Analytics", icon="📈")
admission_page = st.Page("pages/admissions.py", title="Admissions", icon="🎟️")

# Configure the navigation menu with the pages
pg = st.navigation([
    home_page,
    customers_page,
    medecin_page,
    specialite_page,
    departement_page,
    analytics_page,
    admission_page,
])
pg.run()