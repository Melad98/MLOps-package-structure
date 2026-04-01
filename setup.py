import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arabic_nlp_toolkit",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A complete production-ready Python package for processing Arabic text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Melad98/MLOps-package-structure",
    project_urls={
        "Bug Tracker": "https://github.com/Melad98/MLOps-package-structure/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Arabic",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[
        "nltk>=3.6.2",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2.5",
            "pytest-cov>=2.12.1",
            "build>=0.7.0",
        ]
    },
)
