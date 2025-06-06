
import streamlit as st
from datetime import date

st.set_page_config(page_title="Cover Letter Generator", layout="centered")
st.title("📄 Manuscript Cover Letter Generator")

st.write("Fill in the details below to generate a professional cover letter.")

# Input fields
title = st.text_input("Manuscript Title")
author = st.text_input("Corresponding Author Name")
journal = st.text_input("Journal Name")
submission_date = st.date_input("Submission Date", value=date.today())
paper_type = st.selectbox("Paper Type", ["Original Research", "Review", "Short Communication", "Case Study"])
paper_aim = st.text_area("Main Aim or Objective of the Paper")
novelty = st.text_area("Novelty or Key Contribution")

# Upload manuscript (optional, for future keyword extraction)
manuscript = st.file_uploader("Upload your manuscript (optional)", type=["docx", "pdf"])

if st.button("Generate Cover Letter"):
    cover_letter = f"""
Dear Editor,

I am pleased to submit our manuscript entitled "{title}" for consideration in *{journal}* as a {paper_type}. This paper is authored by {author} and addresses the following main aim: {paper_aim}.

The novelty of our work lies in: {novelty}

We believe this work will be of interest to the readership of *{journal}* and aligns well with the journal’s scope. We confirm that this manuscript has not been published elsewhere and is not under consideration by any other journal.

Thank you for considering our submission. We look forward to your positive response.

Sincerely,

{author}  
{submission_date.strftime("%B %d, %Y")}
"""
    st.success("✅ Cover Letter Generated:")
    st.text_area("Generated Letter", value=cover_letter, height=300)
    st.download_button("📥 Download as TXT", cover_letter, file_name="cover_letter.txt")
