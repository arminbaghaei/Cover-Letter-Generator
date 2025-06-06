from fpdf import FPDF
from datetime import date

class PDF(FPDF):
    def header(self):
        if self.logo_path:
            self.image(self.logo_path, 10, 8, 33)
            self.set_y(45)

    def __init__(self, logo_path=None):
        super().__init__()
        self.logo_path = logo_path

def generate_pdf(name, email, affiliation, title, author, journal, submission_date, paper_type, paper_aim, novelty, signature_path=None, logo_path=None):
    pdf = PDF(logo_path)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Times", size=12)

    # Normalize apostrophes
    fixed_novelty = novelty.replace("’", "'")
    fixed_aim = paper_aim.replace("’", "'")
    fixed_journal = journal.replace("’", "'")

    # Header
    pdf.cell(200, 10, txt=name, ln=True)
    pdf.cell(200, 10, txt=email, ln=True)
    pdf.cell(200, 10, txt=affiliation, ln=True)
    pdf.ln(10)

    # Letter
    pdf.multi_cell(0, 10, "Dear Editor,", align="L")
    pdf.multi_cell(0, 10,
        f'I am pleased to submit our manuscript entitled "{title}" for consideration in {fixed_journal} as a {paper_type}. '
        f'This paper is authored by {author} and addresses the following main aim: {fixed_aim}.', align="L")

    pdf.ln(5)
    pdf.multi_cell(0, 10, f"The novelty of our work lies in: {fixed_novelty}", align="L")

    pdf.ln(5)
    pdf.multi_cell(0, 10,
        f"We believe this work will be of interest to the readership of {fixed_journal} and aligns well with the journal's scope. "
        f"We confirm that this manuscript has not been published elsewhere and is not under consideration by any other journal.",
        align="L")

    pdf.ln(5)
    pdf.multi_cell(0, 10, "Thank you for considering our submission. We look forward to your positive response.\n\nSincerely,", align="L")

    # Signature
    if signature_path:
        pdf.image(signature_path, x=10, w=40)
        pdf.ln(20)

    pdf.cell(200, 10, txt=author, ln=True)
    pdf.cell(200, 10, txt=submission_date.strftime("%B %d, %Y"), ln=True)

    # Save PDF
    pdf_path = "/mnt/data/cover_letter_generated.pdf"
    pdf.output(pdf_path)
    return pdf_path

# Example call (logo/signature optional)
pdf_path = generate_pdf(
    name="Dr. Armin Baghaei",
    email="armin@example.com",
    affiliation="Tech Innovation Experts Group",
    title="A Novel Approach to Sustainable Materials",
    author="Dr. Armin Baghaei",
    journal="Journal of Eco Building",
    submission_date=date.today(),
    paper_type="Original Research",
    paper_aim="to assess the lifecycle carbon footprint of novel biocomposites in residential housing",
    novelty="the integration of waste-derived composites with enhanced thermal insulation capacity",
    signature_path=None,
    logo_path=None
)

pdf_path
