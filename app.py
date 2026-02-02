import streamlit as st
import matplotlib.pyplot as plt
from data_generator import generate_job_data
from analyzer import analyze_trends

st.set_page_config(page_title="Job Market Pulse", layout="centered")

st.title("📊 LinkedIn Job Market Pulse Dashboard")
st.write("Tracks trending job roles to help career planning")

if st.button("Analyze Job Market"):
    df = generate_job_data()
    trends = analyze_trends(df)

    st.subheader("🔥 Trending Job Roles")
    st.bar_chart(trends)

    st.success("Analysis Completed Successfully ✅")
