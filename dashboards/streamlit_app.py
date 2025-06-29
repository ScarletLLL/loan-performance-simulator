import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.data_ingestion import generate_synthetic_loans
from src.simulation import simulate_performance
from src.reporting import generate_report

st.title("Loan Portfolio Performance Simulator")

n = st.slider("Number of loans", 100, 5000, 1000)

if st.button("Run Simulation"):
    loans = generate_synthetic_loans(n)
    result = simulate_performance(loans)
    summary = generate_report(result)
    st.write("## Summary")
    st.write(summary)
    st.write("## Sample Loans")
    st.dataframe(result.head())
