import streamlit as st

st.set_page_config(layout="wide", page_title="UNICEF Dashboard")
st.markdown("""
# 🛡️ UNICEF Child Protection Dashboard - Project Officer

**Données simulées réalistes** (6 mois, 4 régions, 3 projets)
""")

# CSS personnalisé
st.markdown("""
<style>
.metric-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
               padding: 20px; border-radius: 15px; color: white; text-align: center; }
.alert { background: #fee; padding: 15px; border-left: 5px solid #f44336; }
</style>
""", unsafe_allow_html=True)

# DONNÉES SIMULÉES
total_reached = 72048
progress_pct = 92.3
satisfaction = 8.7
regions_data = {
    "North": 18500, "South": 21000, "East": 16500, "West": 16048
}
months_data = {"Oct-25": 11500, "Nov-25": 12000, "Dec-25": 11800, "Jan-26": 12500, "Feb-26": 12200, "Mar-26": 10048}

# KPI CARDS
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"""
<div class="metric-card">
    <h2 style="margin:0">{total_reached:,}</h2>
    <p>👶 Children Reached</p>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="metric-card">
    <h2 style="margin:0">{progress_pct}%</h2>
    <p>🎯 Progress vs Target</p>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="metric-card">
    <h2 style="margin:0">{satisfaction}/10</h2>
    <p>⭐ Satisfaction</p>
</div>
""", unsafe_allow_html=True)

col4.markdown("""
<div class="metric-card">
    <h2 style="margin:0">$42</h2>
    <p>💰 Cost per Child</p>
</div>
""", unsafe_allow_html=True)

# FILTRES
st.subheader("🔍 Filtres Interactifs")
col_f1, col_f2 = st.columns(2)
month_filter = col_f1.multiselect("Mois", list(months_data.keys()), default=list(months_data.keys()))
region_filter = col_f2.multiselect("Région", list(regions_data.keys()), default=list(regions_data.keys()))

# GRAPHIQUES HTML/SVG
st.subheader("📊 Visualisations")

# Graphique en barres (Régions) - SVG pur
st.markdown(f"""
<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
<h3>🗺️ Enfants Atteints par Région</h3>
<svg width="100%" height="300" viewBox="0 0 500 300">
  <rect x="50" y="250" width="60" height="50" fill="#4CAF50" opacity="0.8"/>
  <text x="80" y="280" text-anchor="middle" fill="black" font-size="12">North<br/>{regions_data['North']:,}</text>
  <rect x="130" y="200" width="60" height="100" fill="#2196F3" opacity="0.8"/>
  <text x="160" y="230" text-anchor="middle" fill="black" font-size="12">South<br/>{regions_data['South']:,}</text>
  <rect x="210" y="260" width="60" height="40" fill="#FF9800" opacity="0.8"/>
  <text x="240" y="290" text-anchor="middle" fill="black" font-size="12">East<br/>{regions_data['East']:,}</text>
  <rect x="290" y="255" width="60" height="45" fill="#F44336" opacity="0.8"/>
  <text x="320" y="285" text-anchor="middle" fill="black" font-size="12">West<br/>{regions_data['West']:,}</text>
</svg>
</div>
""", unsafe_allow_html=True)

# Graphique ligne (Mois) - SVG
st.markdown("""
<div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-top: 20px;">
<h3>📈 Évolution Mensuelle</h3>
<svg width="100%" height="300" viewBox="0 0 600 300">
  <polyline points="50,250 120,220 190,210 260,180 330,160 400,170" 
            fill="none" stroke="#1f77b4" stroke-width="4" stroke-linecap="round"/>
  <circle cx="50" cy="250" r="6" fill="#1f77b4"/>
  <text x="40" y="275" font-size="11">Oct</text>
  <circle cx="120" cy="220" r="6" fill="#1f77b4"/>
  <text x="110" y="245" font-size="11">Nov</text>
  <circle cx="190" cy="210" r="6" fill="#1f77b4"/>
  <text x="180" y="235" font-size="11">Dec</text>
  <circle cx="260"
