import fitz  # PyMuPDF
import re
from fuzzywuzzy import process
from config import SKILL_SET

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text("text") for page in doc])

    # Extract name (first meaningful non-empty line)
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    name = lines[0] if lines else "Unknown"

    # Define section headers for extraction
    section_headers = [
        "Contact Details", "Personal Information", "Education", "Technical Skills", "Skills",
        "Additional Skills", "Certifications", "Interests", "Experience", "Achievements"
    ]

    structured_data = {"Name": name}
    current_section = None

    for line in lines:
        if any(re.match(f"^{re.escape(header)}$", line, re.IGNORECASE) for header in section_headers):
            current_section = line
            structured_data[current_section] = ""
        elif current_section:
            structured_data[current_section] += line + "\n"

    # Extract and match skills
    structured_data["Matched Skills"] = extract_skills(text)

    return structured_data

# Function to extract skills using fuzzy matching
def extract_skills(text):
    found_skills = set()
    for skill in SKILL_SET:
        match = process.extractOne(skill, text.split(), score_cutoff=80)
        if match:
            found_skills.add(skill)
    return list(found_skills) if found_skills else ["Not Found"]
