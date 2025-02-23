import streamlit as st
import io

st.set_page_config(page_title="Company Details", page_icon="🏢", layout="wide")

# Hide default Streamlit elements
st.markdown("""
<style>
.stAppHeader, .st-emotion-cache-6qob1r, .stSidebar { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# Check if company details are already in session state
if "company_name" not in st.session_state:
    st.session_state["company_name"] = None
    st.session_state["email"] = None
    st.session_state["company_logo"] = None

# If user enters a new company, clear old data
if st.session_state["company_name"] is None:
    st.session_state.clear()  # Clear previous session data

st.title("🏢 Enter Company Details")

with st.form("company_form"):
    company_name = st.text_input("Company Name")
    email = st.text_input("Email Address")
    logo = st.file_uploader("Upload Company Logo", type=["png", "jpg", "jpeg"])
    submit = st.form_submit_button("Submit")

    if submit and company_name:
        st.session_state["company_name"] = company_name
        st.session_state["email"] = email

        # Convert logo to BytesIO and save in session state
        if logo is not None:
            bytes_data = io.BytesIO(logo.getvalue())  # Convert uploaded file to BytesIO
            st.session_state["company_logo"] = bytes_data  # Store in session state

        st.success("✅ Details saved! Redirecting to dashboard...")
        st.switch_page("pages/dashboard.py")  # Redirect to dashboard
