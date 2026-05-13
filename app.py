import streamlit as st
import pandas as pd
import plotly.express as px

# PAGE SETTINGS
st.set_page_config(page_title="VCPL HR Dashboard", layout="wide")

# COMPANY TITLE
st.markdown("""
<h1 style='text-align: center; color: darkblue;'>
Viswanathan Constructions Pvt Ltd
</h1>
<hr>
""", unsafe_allow_html=True)

# GOOGLE SHEETS CONNECTION
sheet_url = "https://docs.google.com/spreadsheets/d/1oS0iWSno_tjfThlkt-Gbm1wVcfWp4o1Qu-WVG0q5zJo/export?format=csv"

data = pd.read_csv(sheet_url)

# LATEST DATA
latest = data.iloc[-1]

# KPIs
total_strength = latest["Total Employee Strength"]
present = latest["Employees Present"]
absent = latest["LOP / Absentees"]
attendance = latest["Attendance %"]
joiners = latest["New Joiners"]
left_emp = latest["Employees Left"]

# KPI CARDS
col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Employees", total_strength)
col2.metric("Present", present)
col3.metric("Absentees", absent)
col4.metric("New Joiners", joiners)
col5.metric("Employees Left", left_emp)

st.markdown("---")

# CHARTS

# Attendance Pie Chart
attendance_data = pd.DataFrame({
    "Status": ["Present", "Absent"],
    "Count": [present, absent]
})

fig1 = px.bar(
    attendance_data,
    x="Status",
    y="Count",
    color="Status",
    text="Count",
    title="Today's Attendance"
)

# Joiners vs Left
fig2 = px.line(
    data,
    x="Date",
    y=["New Joiners", "Employees Left"],
    markers=True,
    title="Daily Employee Movement"

)

# Attendance Trend
fig3 = px.line(
    data,
    x="Date",
    y="Attendance %",
    markers=True,
    title="Attendance Percentage Trend"
)

# DISPLAY CHARTS
c1, c2 = st.columns(2)

with c1:
    st.plotly_chart(fig1, use_container_width=True)

with c2:
    st.plotly_chart(fig2, use_container_width=True)

st.plotly_chart(fig3, use_container_width=True)

# TABLE
st.markdown("## Attendance Data")

st.dataframe(data, use_container_width=True)