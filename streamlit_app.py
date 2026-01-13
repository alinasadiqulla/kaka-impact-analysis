import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Kaká Impact Analysis", page_icon="⚽", layout="wide")

st.title("⚽ Did Kaká Actually Impact AC Milan's Performance?")
st.write("A statistical analysis of 303 matches from the European Soccer Database")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Correlation", "-0.011", help="Between Kaká's presence and goals scored")
with col2:
    st.metric("P-Value", "0.845", help="No statistically significant difference")
with col3:
    st.metric("Model Accuracy", "47.5%", help="Logistic regression prediction accuracy")

st.markdown("---")

st.header("🔍 The Surprising Finding")
st.write("""
Despite Kaká being one of the world's best players during his AC Milan tenure, 
statistical analysis shows his presence had **minimal predictive power** on match outcomes. 
This challenges the assumption that star players automatically translate to team success.
""")

st.header("📊 Average Goals Scored")

with_kaka_goals = 1.85
without_kaka_goals = 1.87

data = pd.DataFrame({
    'Category': ['With Kaká', 'Without Kaká'],
    'Average Goals': [with_kaka_goals, without_kaka_goals]
})

fig = go.Figure(data=[
    go.Bar(
        x=data['Category'],
        y=data['Average Goals'],
        marker_color=['#000000', '#FF0000'],
        text=data['Average Goals'].round(2),
        textposition='outside'
    )
])

fig.update_layout(
    title='AC Milan Average Goals per Match',
    xaxis_title='Kaká\'s Presence',
    yaxis_title='Average Goals Scored',
    showlegend=False,
    height=450,
    yaxis_range=[0, 2.5]
)

st.plotly_chart(fig, use_container_width=True)

with st.expander("📋 View Methodology"):
    st.markdown("""
    **Data Source:** European Soccer Database (SQLite)
    
    **Analysis Steps:**
    1. Queried and filtered 303 AC Milan matches
    2. Identified matches where Kaká played by checking player lineups
    3. Performed statistical testing:
       - T-test comparing goals with/without Kaká
       - Correlation analysis between presence and goals
       - Logistic regression for win prediction
    
    **Technologies Used:** Python, SQL, Pandas, Matplotlib, scikit-learn
    
    **Key Statistical Results:**
    - T-statistic: -0.195
    - P-value: 0.845 (not significant at α=0.05)
    - Correlation coefficient: -0.011 (virtually no correlation)
    - Logistic regression accuracy: 47.5% (worse than random)
    """)

with st.expander("💡 What This Means"):
    st.write("""
    This analysis demonstrates that football/soccer is fundamentally a team sport. 
    While individual talent matters, match outcomes depend on:
    - Team chemistry and tactics
    - Opposition strength
    - Match context (home/away, competition type)
    - Injuries and form of other players
    
    Even a Ballon d'Or winner like Kaká couldn't single-handedly determine results.
    """)

st.markdown("---")
st.markdown("**[View Full Analysis & Code on GitHub](https://github.com/alinasadiqulla/kaka-impact-analysis)**")
st.caption("Built with Streamlit • Data from European Soccer Database")
