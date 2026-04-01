import re
from typing import Dict

# Very basic dictionary for demonstration purposes
# In a real MLOps pipeline, this might be loaded from a model or a larger lexicon file
POSITIVE_WORDS = {
    'جيد', 'ممتاز', 'رائع', 'جميل', 'سعيد', 'مفرح', 
    'عظيم', 'مذهل', 'ناجح', 'مفيد'
}

NEGATIVE_WORDS = {
    'سيء', 'حزين', 'فظيع', 'مؤلم', 'كئيب', 'فاشل', 
    'بشع', 'رديء', 'قبيح', 'مضر'
}

def analyze_sentiment(text: str) -> str:
    """
    Performs a rule-based sentiment analysis on Arabic text.
    
    Args:
        text (str): Input text to analyze.
        
    Returns:
        str: 'positive', 'negative', or 'neutral'.
    """
    if not text or not isinstance(text, str):
        return 'neutral'
        
    # Simple word counting logic
    words = re.findall(r"[\w']+", text)
    
    pos_count = sum(1 for word in words if word in POSITIVE_WORDS)
    neg_count = sum(1 for word in words if word in NEGATIVE_WORDS)
    
    if pos_count > neg_count:
        return 'positive'
    elif neg_count > pos_count:
        return 'negative'
    else:
        return 'neutral'
