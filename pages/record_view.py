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

# Display Data
st.dataframe(df, use_container_width=True)

# Download Button
st.download_button("📥 Download Excel", df.to_csv(index=False), "productivity_data.csv", "text/csv")

# Sidebar Delete & Edit Options
st.sidebar.header("Manage Data")

if not df.empty:  # ✅ Only show delete & edit options if DataFrame is not empty
    # Delete Row
    row_num = st.sidebar.number_input("Enter Row Number to Delete", min_value=0, max_value=len(df)-1, step=1)
    if st.sidebar.button("🗑️ Delete Row"):
        df.drop(index=row_num, inplace=True)
        df.to_excel(data_file, index=False)
        st.rerun()

    # Edit Row
    edit_row = st.sidebar.number_input("Enter Row Number to Edit", min_value=0, max_value=len(df)-1, step=1)
    if st.sidebar.button("✏️ Edit Row"):
        st.write("Editing Row:", edit_row)
        df.loc[edit_row, "Type"] = st.text_input("Update Type", df.loc[edit_row, "Type"])
        df.loc[edit_row, "Name"] = st.text_input("Update Name", df.loc[edit_row, "Name"])
        df.loc[edit_row, "Department"] = st.text_input("Update Department", df.loc[edit_row, "Department"])
        df.loc[edit_row, "Input"] = st.number_input("Update Input", value=df.loc[edit_row, "Input"])
        df.loc[edit_row, "Output"] = st.number_input("Update Output", value=df.loc[edit_row, "Output"])
        df.loc[edit_row, "Productivity"] = df.loc[edit_row, "Output"] / df.loc[edit_row, "Input"]
        
        if st.button("✅ Save Changes"):
            df.to_excel(data_file, index=False)
            st.success("Row Updated Successfully!")
            st.rerun()
else:
    st.sidebar.warning("No data available to delete or edit.")  # ✅ Show warning if DataFrame is empty
