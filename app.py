import streamlit as st

st.set_page_config(layout="wide")
st.title("🛡️ UNICEF Child Protection Dashboard")

st.markdown("""
<style>
.metric {background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1.5rem; border-radius: 10px; color: white; text-align: center; margin: 0.5rem;}
.alert {background: #fee; padding: 1rem; border-left: 5px solid #f44336; margin: 1rem 0;}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.markdown('<div class="metric"><h2>72,048</h2><p>👶 Children Reached</p></div>', unsafe_allow_html=True)
col2.markdown('<div class="metric"><h2>92.3%</h2><p>🎯 Progress</p></div>', unsafe_allow_html=True)
col3.markdown('<div class="metric"><h2>8.7/10</h2><p>⭐ Satisfaction</p></div>', unsafe_allow_html=True)

st.subheader("🔍 Filters")
col1, col2 = st.columns(2)
col1.multiselect("Month", ["Oct-25", "Nov-25", "Dec-25"], default=["Oct-25"])
col2.multiselect("Region", ["North", "South", "East"], default=["North"])

st.markdown('<div style="background:white;padding:20px;border-radius:10px;"><h3>🗺️ By Region</h3><svg width="100%" height="200" viewBox="0 0 400 200"><rect x="20" y="150" width="40" height="50" fill="#4CAF50"/><text x="40" y="175" text-anchor="middle" font-size="12">North 18k</text><rect x="80" y="100" width="40" height="100" fill="#2196F3"/><text x="100" y="125" text-anchor="middle" font-size="12">South 21k</text><rect x="140" y="160" width="40" height="40" fill="#FF9800"/><text x="160" y="185" text-anchor="middle" font-size="12">East 16k</text></svg></div>', unsafe_allow_html=True)

st.markdown('<div style="background:white;padding:20px;border-radius:10px;margin-top:20px;"><h3>📈 Monthly Trend</h3><svg width="100%" height="200" viewBox="0 0 400 200"><polyline points="30,170 80,140 130,130 180,100 230,80 280,90" stroke="#1f77b4" stroke-width="3" fill="none"/><circle cx="30" cy="170" r="4" fill="#1f77b4"/><text x="15" y="195" font-size="11">Oct</text><circle cx="80" cy="140" r="4" fill="#1f77b4"/><text x="65" y="165" font-size="11">Nov</text></svg></div>', unsafe_allow_html=True)

st.markdown('<div style="background:#fee;padding:15px;border-left:5px solid #f44336;margin:20px 0;">🚨 ALERT: 2 regions under 80% progress</div>', unsafe_allow_html=True)

st.markdown("*AI-generated: UNICEF Child Protection KPIs with SVG charts*")
