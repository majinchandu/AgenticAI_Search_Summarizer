from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def save_summary_to_pdf(summary_text, topic, filename="gemini_summary.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 50, f"Summary Report: {topic}")

    # Body
    c.setFont("Helvetica", 11)
    lines = summary_text.split("\n")
    y = height - 80
    for line in lines:
        if y < 60:  # Page break
            c.showPage()
            c.setFont("Helvetica", 11)
            y = height - 50
        c.drawString(50, y, line)
        y -= 15

    c.save()
    print(f"✅ PDF saved as: {filename}")
