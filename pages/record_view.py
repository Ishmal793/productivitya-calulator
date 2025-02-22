import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Productivity Records", page_icon="📂", layout="wide")

st.title("📂 Productivity Data Records")


# Define Excel file name
data_file = "productivity_data.xlsx"

# Check if file exists; if not, create an empty DataFrame
if not os.path.exists(data_file):
    df = pd.DataFrame(columns=["Type", "Name", "Department", "Input", "Output", "Productivity"])
    df.to_excel(data_file, index=False)

# Load existing data
df = pd.read_excel(data_file)

# Sidebar - Selection
st.sidebar.header("Productivity Calculator")
option = st.sidebar.radio("Select Productivity Type", ["Overall Productivity", "Department Productivity", "Employee Productivity"])

# User Input Fields
with st.sidebar.form("Productivity Form"):
    if option == "Overall Productivity":
        total_input = st.number_input("Enter Total Input", min_value=1.0)
        total_output = st.number_input("Enter Total Output", min_value=0.0)
        name, department = "-", "-"  # Not needed for overall

    elif option == "Department Productivity":
        department = st.text_input("Enter Department Name")
        total_input = st.number_input("Enter Department Input", min_value=1.0)
        total_output = st.number_input("Enter Department Output", min_value=0.0)
        name = "-"  # Not needed for department-level productivity

    else:  # Employee Productivity
        name = st.text_input("Enter Employee Name")
        department = st.text_input("Enter Department Name")
        total_input = st.number_input("Enter Employee Input", min_value=1.0)
        total_output = st.number_input("Enter Employee Output", min_value=0.0)

    # Submit Button
    add_data = st.form_submit_button(label="Calculate & Save")

if add_data:
    productivity = round(total_output / total_input, 2)  # Formula
    new_data = pd.DataFrame([[option, name, department, total_input, total_output, productivity]],
                            columns=df.columns)
    
    df = pd.concat([df, new_data], ignore_index=True)  # Append new record
    df.to_excel(data_file, index=False)  # Save to Excel

    st.success(f"Productivity Recorded: {productivity}")

# Show Data Table
st.subheader("Productivity Data")
st.dataframe(df, use_container_width=True)

# Download Button
st.download_button("Download Data as Excel", df.to_csv(index=False), "productivity_data.csv", "text/csv")
