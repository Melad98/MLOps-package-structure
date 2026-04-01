import pytest
from arabic_nlp_toolkit.tokenizer import simple_tokenizer, sentence_splitter

def test_simple_tokenizer():
    text = "الجو جميل اليوم، ولكن غداً قد تمطر."
    tokens = simple_tokenizer(text)
    # The tokenizer handles punctuation by stripping it out (since we findall words and punctuation but then it's a list)
    # Wait, the simple_tokenizer returns punctuation as separate tokens if we used re.findall(r"[\w']+|[.,!?;،؛؟]", text)
    # Let's see what we expect:
    expected = ['الجو', 'جميل', 'اليوم', '،', 'ولكن', 'غداً', 'قد', 'تمطر', '.']
    # If the tokenizer keeps punctuation
    assert tokens == expected

def test_sentence_splitter():
    text = "مرحباً بكم. هذا اختبار للنظام؟ نعم، إنه كذلك!"
    sentences = sentence_splitter(text)
    expected = ["مرحباً بكم.", "هذا اختبار للنظام؟", "نعم، إنه كذلك!"]
    assert sentences == expected

def test_empty_string():
    assert simple_tokenizer("") == []
    assert sentence_splitter("") == []
