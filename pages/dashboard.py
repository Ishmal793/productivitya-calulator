import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Productivity Records", page_icon="📂", layout="wide")

st.title("📂 Productivity Data Records")

data_file = "data.xlsx"

# Load data
if os.path.exists(data_file):
    df = pd.read_excel(data_file)
else:
    df = pd.DataFrame(columns=["Type", "Name", "Department", "Input", "Output", "Productivity"])

st.dataframe(df, use_container_width=True)

st.download_button("📥 Download Excel", df.to_csv(index=False), "productivity_data.csv", "text/csv")
