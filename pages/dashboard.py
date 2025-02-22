import streamlit as st
import pandas as pd
import os


st.set_page_config(page_title="Productivity Calculator", page_icon="📊", layout="wide")

# Sidebar Logo & Company Name
if "company_logo" in st.session_state and st.session_state["company_logo"]:
    st.sidebar.image(st.session_state["company_logo"], use_column_width=True)
company_name = st.session_state.company_name if "company_name" in st.session_state else "Your Company"
st.title(f"{company_name} - Productivity Dashboard")


st.title("📊 Productivity Calculator")

# Check if Excel file exists, if not create it
data_file = "data.xlsx"
if not os.path.exists(data_file):
    df = pd.DataFrame(columns=["Type", "Name", "Department", "Input", "Output", "Productivity"])
    df.to_excel(data_file, index=False)

# Sidebar options
option = st.sidebar.radio("Select Calculation", ["Overall Productivity", "Department Productivity", "Employee Productivity"])

# Load data
df = pd.read_excel(data_file)

if option == "Overall Productivity":
    st.subheader("📈 Calculate Overall Productivity")
    total_input = st.number_input("Enter Total Input", min_value=1)
    total_output = st.number_input("Enter Total Output", min_value=1)
    if st.button("Calculate"):
        productivity = total_output / total_input
        st.success(f"✅ Productivity: {productivity:.2f}")

        # Save Data
        new_data = pd.DataFrame([["Overall", "-", "-", total_input, total_output, productivity]], 
                                columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel(data_file, index=False)

elif option == "Department Productivity":
    st.subheader("🏢 Department Productivity")
    department = st.text_input("Enter Department Name")
    dept_input = st.number_input("Enter Department Input", min_value=1)
    dept_output = st.number_input("Enter Department Output", min_value=1)
    if st.button("Calculate"):
        productivity = dept_output / dept_input
        st.success(f"✅ {department} Productivity: {productivity:.2f}")

        # Save Data
        new_data = pd.DataFrame([["Department", "-", department, dept_input, dept_output, productivity]], 
                                columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel(data_file, index=False)

elif option == "Employee Productivity":
    st.subheader("👨‍💼 Employee Productivity")
    employee = st.text_input("Enter Employee Name")
    department = st.text_input("Enter Department Name")
    emp_input = st.number_input("Enter Employee Input", min_value=1)
    emp_output = st.number_input("Enter Employee Output", min_value=1)
    if st.button("Calculate"):
        productivity = emp_output / emp_input
        st.success(f"✅ {employee} Productivity: {productivity:.2f}")

        # Save Data
        new_data = pd.DataFrame([["Employee", employee, department, emp_input, emp_output, productivity]], 
                                columns=df.columns)
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel(data_file, index=False)

