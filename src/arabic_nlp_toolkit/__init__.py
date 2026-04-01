"""
Arabic NLP Toolkit
-----------------
A module for Arabic text processing tasks such as cleaning, tokenization, and sentiment analysis.
"""

__version__ = "0.1.0"

from .cleaning import normalize_arabic, remove_diacritics, remove_special_characters
from .tokenizer import simple_tokenizer, sentence_splitter
from .sentiment import analyze_sentiment

__all__ = [
    "normalize_arabic",
    "remove_diacritics",
    "remove_special_characters",
    "simple_tokenizer",
    "sentence_splitter",
    "analyze_sentiment",
]
