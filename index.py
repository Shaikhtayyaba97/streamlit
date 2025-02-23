import streamlit as st
from fpdf import FPDF

# Define colors
HEADER_COLOR = (41, 128, 185)  # Blue
TEXT_COLOR = (44, 62, 80)  # Dark Grey

# Function to generate resume
def generate_resume(name, email, phone, education, skills, experience):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Header
    pdf.set_fill_color(*HEADER_COLOR)
    pdf.rect(0, 0, 210, 40, 'F')
    pdf.set_font("Arial", 'B', 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(200, 20, name, ln=True, align='C')
    pdf.ln(10)
    
    # Contact Info
    pdf.set_font("Arial", '', 12)
    pdf.set_text_color(*TEXT_COLOR)
    pdf.cell(200, 10, f"Email: {email} | Phone: {phone}", ln=True, align='C')
    pdf.ln(10)
    
    # Sections
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Education", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 8, education)
    pdf.ln(5)
    
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Skills", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 8, skills)
    pdf.ln(5)
    
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Experience", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 8, experience)
    
    return pdf

# Streamlit UI
st.set_page_config(page_title="Resume Builder", layout="wide")
st.title("Professional Resume Builder")

# User Inputs
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
education = st.text_area("Education")
skills = st.text_area("Skills")
experience = st.text_area("Experience")

# Generate Resume Button
if st.button("Generate Resume PDF"):
    pdf = generate_resume(name, email, phone, education, skills, experience)
    pdf_output = pdf.output(dest="S").encode("latin1")
    
    st.download_button(
        label="Download Resume",
        data=pdf_output,
        file_name=f"{name}_Resume.pdf",
        mime="application/pdf"
    )