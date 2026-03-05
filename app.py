import streamlit as st

st.set_page_config(layout="wide")
st.title("🛡️ UNICEF Child Protection Dashboard - Project Officer")

st.markdown("""
<style>
.metric {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin: 0.5rem;}
.alert {background: #fee; padding: 1rem; border-left: 5px solid #f44336; margin: 1rem 0;}
.chart {background: white; padding: 20px; border-radius: 10px; margin: 20px 0; box-shadow: 0 4px 6px rgba(0,0,0,0.1);}
</style>
""", unsafe_allow_html=True)

# KPI
col1, col2, col3 = st.columns(3)
col1.markdown('<div class="metric"><h2>72,048</h2><p>👶 Children Reached</p></div>', unsafe_allow_html=True)
col2.markdown('<div class="metric"><h2>92.3%</h2><p>🎯 Progress</p></div>', unsafe_allow_html=True)
col3.markdown('<div class="metric"><h2>8.7/10</h2><p>⭐ Satisfaction</p></div>', unsafe_allow_html=True)

# FILTRES
st.subheader("🔍 Interactive Filters")
col1, col2 = st.columns(2)
month_f = col1.multiselect("Month", ["Oct-25", "Nov-25", "Dec-25", "Jan-26", "Feb-26", "Mar-26"], default=["Oct-25", "Nov-25"])
region_f = col2.multiselect("Region", ["North", "South", "East", "West"], default=["North", "South"])

# GRAFICO 1 - REGION BARRAS
st.markdown('<div class="chart"><h3>🗺️ Children Reached by Region</h3><svg width="100%" height="250" viewBox="0 0 500 250"><rect x="30" y="200" width="50" height="50" fill="#4CAF50"/><text x="55" y="235" text-anchor="middle" font-size="12">North 18.5k</text><rect x="110" y="150" width="50" height="100" fill="#2196F3"/><text x="135" y="185" text-anchor="middle" font-size="12">South 21k</text><rect x="190" y="210" width="50" height="40" fill="#FF9800"/><text x="215" y="245" text-anchor="middle" font-size="12">East 16.5k</text><rect x="270" y="205" width="50" height="45" fill="#F44336"/><text x="295" y=
