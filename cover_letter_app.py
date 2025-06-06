import streamlit as st
from datetime import date
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

def generate_docx(title, author, journal, submission_date, paper_type, paper_aim, novelty):
    doc = Document()
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)

    doc.add_paragraph('Dear Editor,')

    para1 = doc.add_paragraph()
    para1.add_run(f'I am pleased to submit our manuscript entitled "{title}" for consideration in ').bold = False
    para1.add_run(journal).italic = True
    para1.add_run(f' as a {paper_type}. This paper is authored by {author} and addresses the following main aim: {paper_aim}')
    para1.alignment = WD_ALIGN_PARAGRAPH.LEFT

    para2 = doc.add_paragraph()
    para2.add_run("The novelty of our work lies in: ").bold = True
    para2.add_run(novelty)
    para2.alignment = WD_ALIGN_PARAGRAPH.LEFT

    para3 = doc.add_paragraph()
    para3.add_run(f"We believe this work will be of interest to the readership of ").bold = False
    para3.add_run(journal).italic = True
    para3.add_run(" and aligns well with the journal’s scope. We confirm that this manuscript has not been published elsewhere and is not under consideration by any other journal.")
    para3.alignment = WD_ALIGN_PARAGRAPH.LEFT

    doc.add_paragraph("Thank you for considering our submission. We look forward to your positive response.")
    doc.add_paragraph("Sincerely,")
    doc.add_paragraph(author)
    doc.add_paragraph(submission_date.strftime("%B %d, %Y"))

    return doc

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

# Upload manuscript (optional)
st.file_uploader("Upload your manuscript (optional)", type=["docx", "pdf"])

if st.button("Generate Cover Letter"):
    # Generate plain text letter
    cover_letter_text = f"""
Dear Editor,

I am pleased to submit our manuscript entitled "{title}" for consideration in *{journal}* as a {paper_type}. This paper is authored by {author} and addresses the following main aim: {paper_aim}

The novelty of our work lies in: {novelty}

We believe this work will be of interest to the readership of *{journal}* and aligns well with the journal’s scope. We confirm that this manuscript has not been published elsewhere and is not under consideration by any other journal.

Thank you for considering our submission. We look forward to your positive response.

Sincerely,

{author}
{submission_date.strftime("%B %d, %Y")}
"""
    st.success("✅ Cover Letter Generated")
    st.text_area("Preview", value=cover_letter_text, height=300)

    # Generate and offer Word file for download
    doc = generate_docx(title, author, journal, submission_date, paper_type, paper_aim, novelty)
    doc.save("cover_letter.docx")
    with open("cover_letter.docx", "rb") as f:
        st.download_button("📥 Download as Word (DOCX)", f, file_name="cover_letter.docx")
