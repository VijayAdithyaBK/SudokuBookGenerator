from generate_sudoku import generate_sudoku
from create_pdf import create_sudoku_pdf
from reportlab.lib.pagesizes import landscape, inch
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.platypus import SimpleDocTemplate, PageBreak
from PyPDF2 import PdfMerger  # Use PdfMerger instead of PdfFileMerger

# Define the new cover size
cover_width = 5 * inch
cover_height = 8 * inch

def create_front_cover(title):
    doc = SimpleDocTemplate("output/front_cover.pdf", pagesize=(cover_width, cover_height))
    elements = []

    # Add a fancy title to the cover
    title_style = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])

    title_table = Table([[title]], colWidths=[cover_width], rowHeights=[cover_height * 0.6])
    title_table.setStyle(title_style)

    elements.append(title_table)

    doc.build(elements)

def create_back_cover(title):
    doc = SimpleDocTemplate("output/back_cover.pdf", pagesize=(cover_width, cover_height))
    elements = []

    # Add content to the back cover as needed
    # You can include a thank you message, contact information, or any other details
    title_style = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ])

    title_table = Table([[title]], colWidths=[cover_width], rowHeights=[cover_height * 0.6])
    title_table.setStyle(title_style)

    elements.append(title_table)

    doc.build(elements)

if __name__ == "__main__":
    # Create the front cover with a fancy title
    create_front_cover("Sudoku Adventure")

    # Generate Sudoku puzzles
    sudoku_puzzles = [generate_sudoku() for _ in range(101)]

    # Create the Sudoku puzzle book (excluding the front and back covers)
    create_sudoku_pdf("output/sudoku_book.pdf", sudoku_puzzles)

    # Create the back cover (optional)
    create_back_cover("A new 'Sudoku Adventure' awaits you.\nBuy the next publication and start your adventure again.")

    # Merge the front cover, Sudoku book, and back cover (if provided)
    merger = PdfMerger()
    merger.append("output/front_cover.pdf")
    merger.append("output/sudoku_book.pdf")
    merger.append("output/back_cover.pdf")  # Add a back cover here if needed
    merger.write("output/sudoku_book_with_covers.pdf")
    merger.close()
