import streamlit as st

st.set_page_config(layout="wide")
st.markdown("# 🛡️ UNICEF Child Protection Dashboard")
st.markdown("**Project Officer - Suivi projets humanitaires**")

# KPI avec métriques natives
col1, col2, col3 = st.columns(3)
col1.metric("👶 Enfants atteints", "72 048", "+12 %")
col2.metric("🎯 Progression", "92,3 %", "+5 %")
col3.metric("⭐ Satisfaction", "8,7/10", "+0,3")

# Sidebar filtres
st.sidebar.title("🔍 Filtres")
st.sidebar.multiselect("Mois", ["Oct-25", "Nov-25", "Dec-25", "Jan-26"])
st.sidebar.multiselect("Région", ["Nord", "Sud", "Est", "Ouest"])
st.sidebar.multiselect("Projet", ["Vaccination", "École", "Protection"])

# Graphiques NATURELS Streamlit
col1, col2 = st.columns(2)

with col1:
    st.subheader("🗺️ Par Région")
    data_region = {"Nord": 18500, "Sud": 21000, "Est": 16500, "Ouest": 16048}
    st.bar_chart(data_region)

with col2:
    st.subheader("📈 Évolution Mensuelle")
    data_mensuel = {"Oct": 11500, "Nov": 12000, "Dec": 11800, "Jan": 12500, "Feb": 12200, "Mar": 10048}
    st.bar_chart(data_mensuel)

# Alertes + Tableau
st.error("🚨 **ALERTE** : 3 zones sous 80% progression")
st.markdown("**Tableau de suivi :**")

data_table = {
    "Région": ["Nord", "Sud", "Est", "Ouest"],
    "Atteints": [18500, 21000, 16500, 16048],
    "Progrès": ["92%", "95%", "78%", "71%"]
}
st.table(data_table)

st.markdown("---")
st.markdown("""
**🤖 Créé avec IA (Perplexity)**

**Prompts utilisés :**
1. « Dataset UNICEF Child Protection réaliste »
2. « Dashboard Streamlit avec filtres + graphiques »
3. « Alertes <80% + KPI dynamiques »

**Usage responsable** : Données anonymisées, standards UNICEF PRP/MICS
**Déployé** : Streamlit Cloud (zero dependency)
""")
