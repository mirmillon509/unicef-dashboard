import streamlit as st

st.set_page_config(layout="wide")
st.title("🛡️ UNICEF Child Protection Dashboard")

# CSS
st.markdown("""
<style>
.metric {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
         padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin: 0.5rem;}
.alert {background: #fee; padding: 1rem; border-left: 5px solid #f44336; margin: 1rem 0;}
</style>
""", unsafe_allow_html=True)

# DONNEES
total_reached = 72048
progress_pct = 92.3
regions = {"North": 18500, "South": 21000, "East": 16500, "West": 16048}
months = {"Oct-25": 11500, "Nov-25": 12000, "Dec-25": 11800, "Jan-26": 12500, "Feb-26": 12200, "Mar-26": 10048}

# KPI
col1, col2, col3 = st.columns(3)
col1.markdown(f'<div class="metric"><h2>{total_reached:,}</h2><p>👶 Children Reached</p></div>', unsafe_allow_html=True)
col2.markdown(f'<div class="metric"><h2>{progress_pct}%</h2><p>🎯 Progress</p></div>', unsafe_allow_html=True)
col3.markdown(f'<div class="metric"><h2>{progress_pct-1:.1f}/10</h2><p>⭐ Satisfaction</p></div>', unsafe_allow_html=True)

# FILTRES
st.subheader("🔍 Filtres")
col1, col2 = st.columns(2)
month_f = col1.multiselect("Mois", list(months.keys()), default=list(months.keys()))
region_f = col2.multiselect("Région", list(regions.keys()), default=list(regions.keys()))

# BARRES REGION (SVG simple)
st.markdown("""
<div style="background:white; padding:20px;
