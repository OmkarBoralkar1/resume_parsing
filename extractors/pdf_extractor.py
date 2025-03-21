import PyPDF2
import re
from fuzzywuzzy import process
from config import SKILL_SET


# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"

    # Extract name (first meaningful non-empty line)
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    name = lines[0] if lines else "Unknown"

    # Define section headers for extraction
    section_headers = [
    "Contact Details", "Work Experience", "Personal Information", "Education", "Technical Skills", "Skills",
    "Additional Skills", "Certifications", "Interests", "Experience", "Achievements", "Positions of Responsibility", "Projects",
    "CONTACT DETAILS", "WORK EXPERIENCE", "PERSONAL INFORMATION", "EDUCATION", "TECHNICAL SKILLS", "SKILLS", "PROJECTS",
    "ADDITIONAL SKILLS", "CERTIFICATIONS", "INTERESTS", "EXPERIENCE", "ACHEIVEMENTS", "POSITIONS OF RESPONSIBILITY"
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
    lower_text = text.lower()  # Convert entire text to lowercase for better matching

    for skill in SKILL_SET:
        lower_skill = skill.lower()  # Convert skill to lowercase
        if lower_skill in lower_text:  # Check if skill is present in the extracted text
            found_skills.add(skill)
    
    return list(found_skills) if found_skills else ["Not Found"]
