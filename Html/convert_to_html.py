from bs4 import BeautifulSoup
from docx import Document

# Path to the uploaded Word file
docx_path = "C:/Users/Utente/Downloads/POS rev0.0_04.10.2024.docx"
html_output_path_docx = "C:/Users/Utente/Downloads/POS_converted_from_docx.html"

# Load the Word document
doc = Document(docx_path)

# Convert the document to HTML
html_content_docx = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Piano Operativo di Sicurezza</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        table, th, td {
            border: 1px solid #ccc;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
    </style>
</head>
<body>
"""

# Loop through paragraphs in the document to structure the content into HTML
for paragraph in doc.paragraphs:
    text = paragraph.text.strip()
    if text:  # Only add non-empty lines
        if text.isupper():  # Assuming uppercase lines are headings
            html_content_docx += f"<h2>{text}</h2>\n"
        else:
            html_content_docx += f"<p>{text}</p>\n"

# Closing the HTML content
html_content_docx += """
</body>
</html>
"""

# Save the HTML content to a file
with open(html_output_path_docx, "w", encoding="utf-8") as html_file:
    html_file.write(html_content_docx)

html_output_path_docx = "C:/Users/Utente/Downloads/POS_converted_from_docx.html"

try:
    with open(html_output_path_docx, "w", encoding="utf-8") as html_file:
        html_file.write(html_content_docx)
    result = html_output_path_docx
except Exception as e:
    result = str(e)

result


