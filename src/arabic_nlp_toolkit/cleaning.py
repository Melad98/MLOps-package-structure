import re

def remove_diacritics(text: str) -> str:
    """
    Removes Arabic diacritics (Tashkeel) from the given text.
    
    Args:
        text (str): The Arabic text to process.
        
    Returns:
        str: Text without diacritics.
    """
    arabic_diacritics = re.compile("""
                             ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    return re.sub(arabic_diacritics, '', text)

def normalize_arabic(text: str) -> str:
    """
    Normalizes Arabic orthography (e.g. Alif/Ya/Ta-Marbuta variants).
    
    Args:
        text (str): The Arabic text to normalize.
        
    Returns:
        str: Normalized text.
    """
    text = re.sub(r'[إأآا]', 'ا', text)
    text = re.sub(r'ى', 'ي', text)
    text = re.sub(r'ة', 'ه', text)
    text = re.sub(r'ؤ', 'و', text)
    text = re.sub(r'ئ', 'ي', text)
    return text

def remove_special_characters(text: str) -> str:
    """
    Removes non-alphanumeric and special characters from text, preserving Arabic spaces.
    
    Args:
        text (str): The input text.
        
    Returns:
        str: Text without special characters.
    """
    # Keeps Arabic letters, English letters, numbers, and spaces
    text = re.sub(r'[^\w\s\u0600-\u06FF]', ' ', text)
    # Condense multiple spaces into one
    text = re.sub(r'\s+', ' ', text).strip()
    return text
