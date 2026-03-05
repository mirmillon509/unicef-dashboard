import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("🛡️ UNICEF Child Protection Dashboard - Project Officer")

# DONNEES SIMULEES (zéro problème de fichier)
data = {
    'Month': ['Oct-25', 'Nov-25', 'Dec-25', 'Jan-26', 'Feb-26', 'Mar-26'] * 12,
    'Region': (['Region A (North)', 'Region B (South)', 'Region C (East)', 'Region D (West)'] * 3) * 6,
    'Project': (['Vaccination', 'School', 'Protection'] * 24),
    'Children_Reached': [2849,3567,3921,1876,5123,2987,4123,2345,3456,2890,1678,4231]*6,
    'Target': [6789,7456,6234,4567,6543,5123,5234,3890,7890,4321,5678,3890]*6,
    'Progress_Pct': [85.2,82.1,89.4,76.5,93.2,91.2,78.9,84.6,88.7,76.8,69.4,72.1]*6,
    'Funding_Pct': [92.1,89.4,95.2,79.8,97.3,82.3,88.4,91.8,94.1,81.2,78.9,85.6]*6,
    'Satisfaction': [8.7,9.0,9.3,8.4,9.2,8.9,9.1,8.6,9.0,8.5,8.3,8.8]*6
}
df = pd.DataFrame(data)

# KPI CARDS
col1, col2, col3, col4 = st.columns(4)
total_reached = df['Children_Reached'].sum()
