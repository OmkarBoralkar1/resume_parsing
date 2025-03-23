import spacy
import PyPDF2
import re
from fuzzywuzzy import process
from config import SKILL_SET

# Load pre-trained NLP model (spaCy's large model for better accuracy)
nlp = spacy.load("en_core_web_sm")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
    
    # Process text using NLP
    doc = nlp(text)
    
    # Extract name, email, phone number
    name = extract_name(doc)
    email = extract_email(text)
    phone = extract_phone_number(text)
    
    # Extract structured information
    structured_data = extract_sections(text)
    structured_data.update({
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Matched Skills": extract_skills(text)
    })
    
    return structured_data

# Function to extract name using NER
def extract_name(doc):
    name_parts = []
    for token in doc:
        if token.pos_ == "PROPN":  # Proper noun (Singular or Plural)
            name_parts.append(token.text)
        if len(name_parts) == 4:  # Limit to a maximum of 4 words
            break
    
    # If name parts are found, join them to form the full name
    if name_parts:
        return " ".join(name_parts)
    return "Unknown"
# Function to extract email
def extract_email(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    matches = re.findall(email_pattern, text)
    return matches[0] if matches else "Not Found"

# Function to extract phone number
def extract_phone_number(text):
    phone_pattern = r"\+?\d{1,3}[-.\s]?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}"
    matches = re.findall(phone_pattern, text)
    return matches[0] if matches else "Not Found"

# Function to extract sections using NLP
def extract_sections(text):
    sections = {}
    lines = text.split("\n")
    current_section = None
    
    for line in lines:
        doc = nlp(line.strip())
        
        # Identify section headers based on NLP features
        if len(doc) < 5 and any(token.pos_ == "NOUN" for token in doc):
            current_section = line.strip()
            sections[current_section] = ""
        elif current_section:
            sections[current_section] += line.strip() + "\n"
    
    return sections
# Function to extract skills using fuzzy matching
def extract_skills(text):
    found_skills = set()
    doc = nlp(text)  # Parse the text into a doc object

    # Loop through the SKILL_SET to match the skills in the text
    for skill in SKILL_SET:
        lower_skill = skill.lower()  # Convert skill to lowercase for matching
        for token in doc:
            # Only consider tokens with exact matches, preserving the format
            if lower_skill == token.text.lower():
                found_skills.add(skill)

    return list(found_skills) if found_skills else ["Not Found"]
