import streamlit as st
import io

st.set_page_config(page_title="Company Details", page_icon="🏢", layout="wide")

# Hide default Streamlit elements
st.markdown("""
<style>
.stAppHeader, .st-emotion-cache-6qob1r, .stSidebar { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# Initialize session state variables if not already set
if "company_name" not in st.session_state:
    st.session_state["company_name"] = None
    st.session_state["email"] = None
    st.session_state["company_logo"] = None

# Check if details already exist
is_edit_mode = st.session_state["company_name"] is not None

st.title("🏢 Enter Company Details" if not is_edit_mode else "✏️ Edit Company Details")

with st.form("company_form"):
    company_name = st.text_input("Company Name", value=st.session_state["company_name"] or "")
    email = st.text_input("Email Address", value=st.session_state["email"] or "")
    logo = st.file_uploader("Upload Company Logo", type=["png", "jpg", "jpeg"])

    submit = st.form_submit_button("Submit")

    if submit:
        if not company_name or not email or (not logo and not is_edit_mode):
            st.error("❌ Please fill all fields (including logo for first time)!")
        else:
            st.session_state["company_name"] = company_name
            st.session_state["email"] = email

            # Store logo if uploaded, otherwise keep old logo
            if logo is not None:
                bytes_data = io.BytesIO(logo.getvalue())  # Convert uploaded file to BytesIO
                st.session_state["company_logo"] = bytes_data  # Store in session state

            st.success("✅ Details saved! Redirecting to dashboard...")
            st.switch_page("pages/dashboard.py")  # Redirect to dashboard
