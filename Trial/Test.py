
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

def pdf_to_text(pdf_path):
    # Convert PDF to a list of images
    images = convert_from_path(pdf_path)

    # Initialize a list to hold the text
    all_text = []

    # Iterate through each image (page)
    for i, image in enumerate(images):
        # Convert image to text
        text = pytesseract.image_to_string(image)
        all_text.append(text)
        print(f"Extracted text from page {i + 1}")

    # Combine all text into a single string
    full_text = "\n".join(all_text)
    return full_text

# Path to the PDF file
pdf_path = 'E:\Dhejus\PythonPractice\XII_Practicals\practical pgms 1-13.pdf'

# Extract text from the PDF
extracted_text = pdf_to_text(pdf_path)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)
