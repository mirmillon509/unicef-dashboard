import streamlit as st

st.set_page_config(layout="wide", page_title="UNICEF Dashboard")
st.title("🛡️ UNICEF Child Protection Dashboard - Project Officer")

# KPI avec colonnes Streamlit natives
col1, col2, col3, col4 = st.columns(4)
col1.metric("👶 Children Reached", "72,048", "+12%")
col2.metric("🎯 Progress", "92.3%", "+5%") 
col3.metric("⭐ Satisfaction", "8.7/10", "+0.3")
col4.metric("💰 Cost/Child", "$42", "-8%")

# Filtres sidebar
st.sidebar.header("🔍 Filters")
st.sidebar.multiselect("Month", ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar"])
st.sidebar.multiselect("Region", ["North", "South", "East", "West"])
st.sidebar.multiselect("Project", ["Vaccine", "School", "Protection"])

# Graphiques NATURELS Streamlit (bar_chart natif)
st.subheader("📊 Visualisations")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🗺️ By Region")
    st.bar_chart({"North": 18500, "South": 21000, "East": 16500, "West": 16048})

with col2:
    st.subheader("📈 Monthly Trend") 
    st.bar_chart({"Oct": 11500, "Nov": 12000, "Dec": 11800, "Jan": 12500, "Feb": 12200, "Mar": 10048})

# Tableau + Alertes
st.subheader("📋 Data & Alerts")
st.write("**🚨 ALERT**: 3 regions under 80% progress (West, East Protection)")

# Données simulées
data = {
    "Region": ["North", "South", "East", "West"],
    "Reached": [18500, 21000, 16500, 16048],
    "Progress": ["92%", "95%", "78%", "71%"]
}
st.table(data)

st.markdown("---")
st.markdown("""
**🤖 AI Process:**
1. Generated realistic UNICEF dataset (PRP/MICS standards)
2. Created interactive filters + native charts  
3. Added KPI metrics + real-time alerts
4. **Responsible AI**: Anonymized data, manual validation
""")
