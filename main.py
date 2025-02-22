import streamlit as st

st.set_page_config(page_title="Company Details", page_icon="🏢", layout="wide")
# removing 3 bar and on streamlit
st.markdown("""
<style>
.stAppHeader.st-emotion-cache-h4xjwg.e4hpqof0,.st-emotion-cache-6qob1r.e1c29vlm8,.stSidebar.st-emotion-cache-rpj0dg.e1c29vlm0,s.t-emotion-cache-1y9tyez.e1c29vlm15
{ visibility:hidden;
}
</style>
""",unsafe_allow_html=True)

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
