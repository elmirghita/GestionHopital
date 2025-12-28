import streamlit as st

# Define pages with custom titles
home_page = st.Page("pages/home.py", title="Dashboard", icon="🏠")
patient_page = st.Page("pages/patient.py", title="Patients", icon="🤒")
medecin_page = st.Page("pages/medecin.py", title="Medecins", icon="👨‍⚕️")
specialite_page = st.Page("pages/specialite.py", title="Specialites", icon="🩺")
departement_page = st.Page("pages/departement.py", title="Departements", icon="🏥")
analytics_page = st.Page("pages/analytics.py", title="Data Analytics", icon="📈")
admission_page = st.Page("pages/admissions.py", title="Admissions", icon="🎟️")
salle_page = st.Page("pages/salle_hospitalisation.py", title="Salle Hospitalisation", icon="🏥")
facture_page = st.Page("pages/facture.py", title="Facture", icon="💳")

# Configure the navigation menu with the pages
pg = st.navigation([
    home_page,
    patient_page,
    admission_page,
    medecin_page,
    specialite_page,
    departement_page,
    salle_page,
    facture_page,
    analytics_page
])
pg.run()