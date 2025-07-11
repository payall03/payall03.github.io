Always show details

Copy
# As a workaround, switch to a PDF library that supports UTF-8 better like `reportlab`
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Set up the PDF file
pdf_path = "/mnt/data/Suno_Project_Prototype_Detailed.pdf"
c = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4

# Utility function to wrap text
def draw_wrapped_text(c, text, x, y, max_width, line_height=14, font="Helvetica", font_size=11):
    from textwrap import wrap
    c.setFont(font, font_size)
    lines = wrap(text, width=100)
    for line in lines:
        c.drawString(x, y, line)
        y -= line_height
    return y

# Document content
sections = {
    "1. Project Overview": intro,
    "2. Communication Modes": modes,
    "3. User Flow": flow,
    "4. Detailed Interface Screens": screens,
    "5. Core Features": features,
    "6. Technology Stack": tech_stack,
    "7. Summary Table": summary,
    "8. Conclusion": conclusion,
}

# Draw all content
y = height - inch
for title, content in sections.items():
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1 * inch, y, title)
    y -= 16
    y = draw_wrapped_text(c, content, 1 * inch, y, width - 2 * inch)
    y -= 20
    if y < inch:
        c.showPage()
        y = height - inch

# Save the final PDF
c.save()
pdf_path