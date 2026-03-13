import fitz

def extract_text_from_pdf(uploaded_file):
    text = ""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page in doc:
        text += page.get_text()

    doc.close() 
    return text

def clean_text(text):
    text = text.replace("\n", " ")   # remove new lines
    text = text.replace("\t", " ")   # remove tabs
    text = " ".join(text.split())    # remove extra spaces
    return text