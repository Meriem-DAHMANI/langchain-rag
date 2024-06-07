from pdf2image import convert_from_path
from PIL import Image

# Path to the PDF file
pdf_path = 'data/21703.06959v4.pdf'

# Convert PDF to a list of images (one per page)
pages = convert_from_path(pdf_path, fmt='tiff')

# Save the first page as a TIFF file
pages[0].save('output.tiff', 'TIFF')
