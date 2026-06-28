import streamlit as st

# 1. Page Configuration & Tactical Theme Branding
st.set_page_config(page_title="Roth Regiment | SCRA Interest Engine", page_icon="🪖", layout="centered")

st.title("🪖 ROTH REGIMENT")
st.subheader("SCRA Financial Protection Engine")
st.write("The Servicemembers Civil Relief Act (SCRA) legally commands lenders to cap all pre-service debts at **6.00% APR**. Use this engine to calculate your hidden savings and generate your legal deployment protection letter.")

st.markdown("---")

# 2. Operational Inputs
st.sidebar.header("Operational Inputs")
branch = st.sidebar.selectbox("Branch of Service", ["Army", "Navy", "Marine Corps", "Air Force", "Space Force", "Coast Guard"])
current_apr = st.sidebar.number_input("Current Loan APR (%)", min_value=6.1, max_value=35.0, value=18.0, step=0.1)
loan_balance = st.sidebar.number_input("Current Principal Balance ($)", min_value=500, max_value=100000, value=25000, step=500)

# 3. Tactical Financial Calculations
scra_cap = 6.0
apr_delta = current_apr - scra_cap
annual_savings = (loan_balance * (apr_delta / 100.0))
monthly_savings = annual_savings / 12.0

# 4. Display the Financial Intel
st.header("🚨 Financial Intelligence Report")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Your Monthly Recovered Cash", value=f"${monthly_savings:,.2f}")
with col2:
    st.metric(label="Your Immediate Annual Savings", value=f"${annual_savings:,.2f}")

st.subheader("⚖️ Legal Assessment")
st.error(f"Your current lender is charging you **{apr_delta:.2f}% over the legal SCRA maximum**. They are legally required to slash your interest rate and refund any overpayments back to your date of entry onto active duty.")

st.markdown("---")

# 5. Automated Legal Form Generator
st.subheader("📋 Direct Action Document")
st.write("Copy the finalized formal text block below, insert your personal data, and route it straight to your lender's customer service terminal via certified mail:")

legal_letter = f"""[Your Name]
[Your Mailing Address]
Date: 2026

TO: [Lender/Bank Name]
Attn: SCRA Compliance Department

RE: Request for SCRA Interest Rate Reduction to 6% (Account Number: [Your Account Number])

Pursuant to the Servicemembers Civil Relief Act (SCRA), 50 U.S.C. § 3937, I am formally requesting that the interest rate on my pre-service loan obligation be capped at the legal maximum of 6% effective from my active-duty enlistment start date.

My enlistment profile places me on active service with the United States {branch}. Under federal protection metrics, this rate limitation applies unconditionally to all obligations incurred prior to entering military service. Please adjust my principal balance calculations, reduce my monthly payment obligations immediately, and issue an account statement validating the adjustment.

Thank you for your prompt compliance with federal defense guidelines.

Sincerely,
[Your Signature]"""

st.text_area(label="Official Protection Request Handoff Letter (Copy/Paste)", value=legal_letter, height=350)