# Importing spaCy
import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Sample text
sample_text = "Hello! This is a sample text. It contains multiple sentences, abbreviations like U.S.A., and special cases like ellipses... Let's tokenize it!"

# Processing the text by giving sample text to the model
doc = nlp(sample_text)

# 1. Word Tokenization
print("1. Word Tokenization:")
print([token.text for token in doc])  # List of tokens

# 2. Sentence Tokenization
print("\n2. Sentence Tokenization:")
print([sent.text for sent in doc.sents])  # List of sentences

# 3. Edge Cases
print("\n3. Edge Cases:")
edge_cases = [
    "Dr. John is here.",  # Abbreviation
    "Wait... what?",      # Ellipsis
    "She said, 'Hello!'"  # Quotes
]
for case in edge_cases:
    doc = nlp(case)		  #Passing special cases to the model
    print(f"Original Text: {case}")
    print(f"Word Tokens: {[token.text for token in doc]}")
    print(f"Sentence Tokens: {[sent.text for sent in doc.sents]}\n")

# 4. Practical Example
print("4. PraxzFctical Example:")
example_text = "Breaking news: The stock market soared today, reaching a record high. Analysts are optimistic about the future!"
doc = nlp(example_text)
print("Word Tokens:", [token.text for token in doc])
print("Sentence Tokens:", [sent.text for sent in doc.sents])
