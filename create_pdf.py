# from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, PageBreak
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

# Define a custom page size for "pocket book"
pocket_book = (5 * inch, 8 * inch)  # Width x Height

def create_sudoku_pdf(filename, sudoku_puzzles):
    doc = SimpleDocTemplate(filename, pagesize=pocket_book)

    elements = []

    for puzzle in sudoku_puzzles:
        data = [[str(puzzle[i][j]) if puzzle[i][j] != 0 else '' for j in range(9)] for i in range(9)]
        table = Table(data, colWidths=30, rowHeights=30)

        # Specify alignment and padding for each cell in the Sudoku grid
        style = TableStyle([
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 20),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Vertically center text
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),  # Text color
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),  # Inner grid lines
            ('BACKGROUND', (0, 0), (-1, -1), colors.white),  # Cell background color
            ('LEFTPADDING', (0, 0), (-1, -1), 4),  # Left padding
            ('RIGHTPADDING', (0, 0), (-1, -1), 4),  # Right padding
            ('TOPPADDING', (0, 0), (-1, -1), -4),  # Negative top padding to move text up
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),  # Bottom padding
        ])

        table.setStyle(style)
        elements.append(table)
        elements.append(PageBreak())

    doc.build(elements)
