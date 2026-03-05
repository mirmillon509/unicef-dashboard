import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide", page_title="UNICEF Dashboard")
st.title("🛡️ UNICEF Child Protection Dashboard")

# Dataset simulé réaliste UNICEF
@st.cache_data
def load_data():
    data = {
        'Month': ['Oct-25']*4 + ['Nov-25']*4 + ['Dec-25']*4 + ['Jan-26']*4 + ['Feb-26']*4 + ['Mar-26']*4,
        'Region': ['North', 'South', 'East', 'West'] * 6,
        'Project': ['Vaccination', 'School', 'Protection', 'Health'] * 6,
        'Children_Reached': [2849, 3921, 1876, 5123, 3567, 2345, 3456, 2890, 4123, 2987, 4231, 1678, 3921, 5123, 2987, 2849, 3567, 2345, 3456, 2890, 4123, 2987, 4231, 1678],
        'Progress_Pct': [85.2, 89.4, 76.5, 93.2, 82.1, 91.2, 88.7, 76.8, 94.5, 84.6, 72.1, 69.4, 89.4, 93.2, 91.2, 85.2, 82.1, 88.7, 76.8, 94.5, 84.6, 72.1, 69.4, 89.4]
    }
    return pd.DataFrame(data)

df = load_data()

# SIDEBAR FILTRES
st.sidebar.header("🔍 Filtres")
month_filter = st.sidebar.multiselect("Mois", df['Month'].unique(), default=df['Month'].unique())
region_filter = st.sidebar.multiselect("Région", df['Region'].unique(), default=df['Region'].unique())
project_filter = st.sidebar.multiselect("Projet", df['Project'].unique(), default=df['Project'].unique())

df_filtered = df[
    (df['Month'].isin(month_filter)) &
    (df['Region'].isin(region_filter)) &
    (df['Project'].isin(project_filter))
]

# KPI PRINCIPAL
col1, col2, col3, col4 = st.columns(4)
total_reached = df_filtered['Children_Reached'].sum()
avg_progress = df_filtered['Progress_Pct'].mean()
col1.metric("👶 Enfants atteints", f"{total_reached:,}", f"+{total_reached//1000}k")
col2.metric("🎯 Progression moyenne", f"{avg_progress:.1f}%")
col3.metric("📊 Projets actifs", len(df_filtered['Project'].unique()))
col4.metric("🗺️ Régions couvertes", len(df_filtered['Region'].unique()))

# GRAPHIQUES AVANCÉS ALTAIR
st.subheader("📊 Visualisations Interactives")

col1, col2 = st.columns(2)

# 1. Évolution temporelle
line_chart = alt.Chart(df_filtered).mark_line(strokeWidth=3).encode(
    x='Month:N',
    y='Children_Reached:Q',
    color='Project:N',
    tooltip=['Month', 'Children_Reached', 'Progress_Pct']
).properties(width=400, height=300, title="Évolution Mensuelle")
col1.altair_chart(line_chart, use_container_width=True)

# 2. Répartition par région
bar_chart = alt.Chart(df_filtered).mark_bar(size=50).encode(
    x='Region:N',
    y='Children_Reached:Q',
    color='Region:N',
    tooltip=['Region', 'Children_Reached']
).properties(width=400, height=300, title="Par Région")
col2.altair_chart(bar_chart, use_container_width=True)

# 3. Heatmap progression
st.subheader("🌡️ Heatmap Progression")
heatmap = alt.Chart(df_filtered).mark_rect().encode(
    x='Region:N',
    y='Project:N',
    color='Progress_Pct:Q',
    tooltip=['Region', 'Project', 'Progress_Pct']
).properties(width=600, height=300)
st.altair_chart(heatmap, use_container_width=True)

# ALERTES
st.subheader("🚨 Alertes Automatiques")
low_progress = df_filtered[df_filtered['Progress_Pct'] < 80]
if len(low_progress) > 0:
    st.error(f"**{len(low_progress)} projets/régions** sous 80% progression !")
    st.dataframe(low_progress[['Region', 'Project', 'Progress_Pct']].head())
else:
    st.success("✅ Tous les projets > 80% progression")

# EXPLICATION IA
with st.expander("🤖 Comment j'ai créé ce dashboard avec IA"):
    st.markdown("""
    **Prompts utilisés dans Claude AI/ChatGPT :**
    1. "Simule dataset UNICEF Child Protection 6 mois 4 régions 4 projets"
    2. "Crée Streamlit dashboard avec sidebar filtres + Altair charts"
    3. "Ajoute KPI metrics + heatmap progression + alertes automatiques"
    
    **Usage responsable :** Données anonymisées, vérification manuelle, standards UNICEF (PRP/MICS).
    """)

st.markdown("---")
st.caption("Dashboard développé avec IA pour suivi projets UNICEF | Données simulées réalistes")
