# Arabic NLP Toolkit

A complete, production-ready Python package for processing Arabic text following MLOps best practices. 
Designed for use in machine learning pipelines, it includes utilities for cleaning, normalization, tokenization, and basic sentiment analysis.

## Features

- **Text Cleaning**: Strip diacritics, remove special characters, and normalize Arabic text.
- **Tokenization**: Simple and rule-based tokenizers and sentence splitters tailored for Arabic text.
- **Sentiment Analysis**: Basic rule-based sentiment scoring (positive, negative, neutral).
- **MLOps Ready**: Designed with modularity, testing, and continuous integration in mind.

## Installation

### From Source

Ensure you have Python 3.8+ installed. You can install it directly by cloning the repository and running:

```bash
git clone https://github.com/Melad98/MLOps-package-structure.git
cd MLOps-package-structure
pip install .
```

For development (including dependencies for testing and building):

```bash
pip install -e ".[dev]"
```

## Usage Example

```python
from arabic_nlp_toolkit.cleaning import normalize_arabic

text = normalize_arabic("النّص العَرَبِيُّ!")
print(text)
# Output might be "النص العربي!" depending on the normalization functions
```

## Testing

To run the unit tests, install development requirements and use `pytest`:

```bash
pip install -e ".[dev]"
pytest tests/
```

## Packaging
Ensure your package is buildable using `build`:
```bash
python -m build
```
