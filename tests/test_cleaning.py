import pytest
from arabic_nlp_toolkit.cleaning import remove_diacritics, normalize_arabic, remove_special_characters

def test_remove_diacritics():
    text_with_diacritics = "مَرْحَبَاً بِكُمْ"
    expected = "مرحبا بكم"
    assert remove_diacritics(text_with_diacritics) == expected

def test_normalize_arabic():
    # Test normalization cases
    cases = {
        "أحمد": "احمد",
        "مستشفى": "مستشفي",
        "مدرسة": "مدرسه",
        "تساؤل": "تساول",
        "مائة": "مايه"
    }
    for input_text, expected in cases.items():
        assert normalize_arabic(input_text) == expected

def test_remove_special_characters():
    text = "مرحبا! كيف الحال؟ (الحمد لله) 123 @#"
    expected = "مرحبا كيف الحال؟ الحمد لله 123"
    result = remove_special_characters(text)
    # the function should replace special chars with space and condense it
    assert result == expected

def test_empty_string():
    assert remove_diacritics("") == ""
    assert normalize_arabic("") == ""
    assert remove_special_characters("") == ""
