import re

def is_arabic_text(text: str) -> bool:
    """
    Checks if a string contains Arabic characters.
    
    Args:
        text (str): Input text.
        
    Returns:
        bool: True if Arabic characters are found, False otherwise.
    """
    # Hex Unicode range for Arabic script
    arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]')
    return bool(arabic_pattern.search(text))

def validate_input(text: str) -> bool:
    """
    Validates the input to ensure it is a non-empty string.
    
    Args:
        text (str): Input text.
        
    Returns:
        bool: Validation status.
        
    Raises:
        ValueError: If input is not strings or is empty.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    if not text.strip():
        raise ValueError("Input string cannot be empty")
        
    return True
