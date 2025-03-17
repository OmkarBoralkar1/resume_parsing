import re

def clean_text(text):
    """Removes extra whitespace, special characters, and formats text."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()
