import streamlit as st

# Define pages with custom titles
home_page = st.Page("pages/home.py", title="Dashboard", icon="🏠")
customers_page = st.Page("pages/patient.py", title="Patients", icon="🤒")
analytics_page = st.Page("pages/analytics.py", title="Data Analytics", icon="📈")
admission_page = st.Page("pages/admissions.py", title="Admissions", icon="🎟️")
salle_page = st.Page("pages/salle_hospitalisation.py", title="Salle Hospitalisation", icon="🏥")

# Configure the navigation menu with the pages
pg = st.navigation([
    home_page,
    customers_page,
    admission_page,
    salle_page,
    analytics_page,
])
pg.run()