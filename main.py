import streamlit as st

st.set_page_config(page_title="Company Details", page_icon="🏢", layout="wide")

# Session state for company details
if "company_name" not in st.session_state:
    st.session_state["company_name"] = None
    st.session_state["email"] = None
    st.session_state["logo"] = None

# If company details are already entered, go to dashboard
if st.session_state["company_name"]:
    st.switch_page("pages/dashboard.py")

st.title("🏢 Enter Company Details")

with st.form("company_form"):
    company_name = st.text_input("Company Name")
    email = st.text_input("Email Address")
    logo = st.file_uploader("Upload Company Logo", type=["png", "jpg", "jpeg"])
    submit = st.form_submit_button("Submit")

    if submit and company_name:
        st.session_state["company_name"] = company_name
        st.session_state["email"] = email
        st.session_state["logo"] = logo
        st.success("✅ Details saved! Redirecting to dashboard...")
        st.switch_page("pages/dashboard.py")
