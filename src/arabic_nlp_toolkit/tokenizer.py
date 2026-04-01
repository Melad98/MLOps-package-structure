import re
from typing import List

def simple_tokenizer(text: str) -> List[str]:
    """
    Tokenizes text by splitting into words based on spaces and punctuation.
    
    Args:
        text (str): The input text to tokenize.
        
    Returns:
        List[str]: A list of tokens (words).
    """
    # Split by any whitespace or basic punctuation and filter out empty strings
    tokens = re.findall(r"[^\s.,!?;،؛؟]+|[.,!?;،؛؟]", text)
    return [token for token in tokens if token.strip()]

def sentence_splitter(text: str) -> List[str]:
    """
    Splits Arabic text into sentences based on common Arabic and English delimiters.
    
    Args:
        text (str): The input text to split.
        
    Returns:
        List[str]: A list of sentences.
    """
    # Delimiters: period, question mark, exclamation mark, Arabic question mark (؟)
    # We use a positive lookbehind to split after the punctuation.
    sentences = re.split(r'(?<=[.!?؟\n])\s+', text)
    return [s.strip() for s in sentences if s.strip()]
