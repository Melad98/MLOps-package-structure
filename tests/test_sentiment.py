import pytest
from arabic_nlp_toolkit.sentiment import analyze_sentiment

def test_positive_sentiment():
    text = "هذا عمل عظيم وممتاز"
    assert analyze_sentiment(text) == "positive"

def test_negative_sentiment():
    text = "هذا شيء سيء و فظيع"
    assert analyze_sentiment(text) == "negative"

def test_neutral_sentiment():
    text = "ذهبت إلى المدرسة اليوم"
    assert analyze_sentiment(text) == "neutral"

def test_mixed_sentiment():
    # 'عظيم' (positive) vs 'سيء' (negative) and 'فظيع' (negative)
    # 1 pos, 2 neg => negative
    text = "هذا عمل عظيم ولكنه سيء و فظيع في النهاية"
    assert analyze_sentiment(text) == "negative"

def test_empty_sentiment():
    assert analyze_sentiment("") == "neutral"
    assert analyze_sentiment(None) == "neutral"
