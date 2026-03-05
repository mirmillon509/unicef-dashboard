import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🛡️ UNICEF Child Protection Dashboard")

# DONNEES EMBARQUEES
data = {
    'Month': ['Oct-25', 'Nov-25', 'Dec-25', 'Jan-26', 'Feb-26', 'Mar-26'] * 12,
    'Region': (['North', 'South', 'East', 'West'] * 3) * 6,
    'Project': (['Vaccination', 'School', 'Protection'] * 24),
    'Children_Reached': [2849,3567,3921,1876,5123,2987,4123,2345,3456,2890,1678,4231]*6,
    'Target': [6789,7456,6234,4567,6543,5123,5234,3890,7890,4321,5678,3890]*6,
    'Progress_Pct': [85,82,89,76,93,91,79,85,89,77,69,72]*6
}
df = pd.DataFrame(data)

# KPI
col1, col2, col3 = st.columns(3)
total = df['Children_Reached'].sum()
col1.metric("👶 Children Reached", f"{total:,}")
col2.metric("🎯 Progress", f"{(total/df['Target'].sum()*100):.0f}%")
col3.metric("⭐ Satisfaction", "8.7/10")

# FILTRES
st.subheader("🔍 Filtres")
col1, col2 = st.columns(2)
month_f = col1.multiselect("Mois", df['Month'].unique())
region_f = col2.multiselect("Région", df['Region'].unique())
df_f = df[df['Month'].isin(month_f) & df['Region'].isin(region_f)]

# GRAPHIQUE 1 : LIGNES
fig1, ax1 = plt.subplots()
monthly = df_f.groupby('Month')['Children_Reached'].sum()
ax1.plot(monthly.index, monthly.values, marker='o', linewidth=3, color='#1f77b4')
ax1.set_title('📈 Enfants Atteints par Mois', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.set_ylabel('Nombre')
st.pyplot(fig1)

# GRAPHIQUE 2 : BARRES
fig2, ax2 = plt.subplots()
regions = df_f.groupby('Region')['Children_Reached'].sum()
colors = plt.cm.Set3(np.linspace(0,1,len(regions)))
ax2.bar(regions.index, regions.values, color=colors)
ax2.set_title('🗺️ Par Région', fontsize=14, fontweight='bold')
ax2.tick_params(axis='x', rotation=45)
st.pyplot(fig2)

# ALERTES + TABLEAU
low = df_f[df_f['Progress_Pct'] < 80]
if len(low) > 0:
    st.error(f"🚨 {len(low)} zones < 80% progression !")

st.subheader("📋 Données")
st.dataframe(df_f.head(10))
