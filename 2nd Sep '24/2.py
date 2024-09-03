import re
from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
import pandas as pd

# Read the contents of the files
with open("/Users/akshitanand/Desktop/Sem VII/Gen AI & Deep L/Lab Work/NLP lab data (1).txt", "r") as file1, open("/Users/akshitanand/Desktop/Sem VII/Gen AI & Deep L/Lab Work/NLP lab data.txt", "r") as file2:
    doc1 = file1.read()
    doc2 = file2.read()

# Function to clean the text (remove stop words and punctuation)
def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    words = text.split()
    words = [word.lower() for word in words if word.lower() not in ENGLISH_STOP_WORDS]  # Remove stopwords
    return ' '.join(words)  # Return cleaned text as a single string

# Function to get word frequency
def get_word_frequency(text):
    words = text.split()
    return Counter(words)

# Clean the documents
doc1_clean = clean_text(doc1)
doc2_clean = clean_text(doc2)

# Get word frequencies
doc1_freq = get_word_frequency(doc1_clean)
doc2_freq = get_word_frequency(doc2_clean)

# Find common words between the two documents
common_words = set(doc1_freq.keys()).intersection(set(doc2_freq.keys()))
print("\nCommon Words and their Frequencies in Both Documents:")
for word in common_words:
    print(f"{word}: Document 1 - {doc1_freq[word]}, Document 2 - {doc2_freq[word]}")

# Find unique words in each document
unique_words_doc1 = set(doc1_freq.keys()) - set(doc2_freq.keys())
unique_words_doc2 = set(doc2_freq.keys()) - set(doc1_freq.keys())

print("\nUnique Words in Document 1:")
for word in unique_words_doc1:
    print(f"{word}: {doc1_freq[word]}")

print("\nUnique Words in Document 2:")
for word in unique_words_doc2:
    print(f"{word}: {doc2_freq[word]}")

# Function to count stop words in the original text
def get_stopword_frequency(text):
    words = text.split()
    stopwords_freq = Counter(word.lower() for word in words if word.lower() in ENGLISH_STOP_WORDS)
    return stopwords_freq

# Get stop word frequencies for both documents
doc1_stopwords_freq = get_stopword_frequency(doc1)
doc2_stopwords_freq = get_stopword_frequency(doc2)

print("\nStop Words and their Frequencies in Document 1:")
for word, freq in doc1_stopwords_freq.items():
    print(f"{word}: {freq}")

print("\nStop Words and their Frequencies in Document 2:")
for word, freq in doc2_stopwords_freq.items():
    print(f"{word}: {freq}")

# Vectorize the original documents
vectorizer = CountVectorizer()
X_original = vectorizer.fit_transform([doc1, doc2])

# Compute cosine similarity for original documents
similarity_matrix_original = cosine_similarity(X_original)

print("\nCosine Similarity Matrix (Original Documents):")
print(similarity_matrix_original)

# Vectorize the cleaned documents
X_cleaned = vectorizer.fit_transform([doc1_clean, doc2_clean])

# Compute cosine similarity for cleaned documents
similarity_matrix_cleaned = cosine_similarity(X_cleaned)

print("\nCosine Similarity Matrix (Cleaned Documents):")
print(similarity_matrix_cleaned)

# Generate and display the term-document matrix for cleaned documents
terms = vectorizer.get_feature_names_out()
term_document_matrix = X_cleaned.toarray()

# Convert to a DataFrame for better visualization
df = pd.DataFrame(term_document_matrix, columns=terms, index=["Document1", "Document2"])

# Display the term-document matrix
print("\nTerm-Document Matrix:")
print(df)
import re
from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
import pandas as pd

# Read the contents of the files
with open("/Users/akshitanand/Desktop/Sem VII/Gen AI & Deep L/Lab Work/NLP lab data (1).txt", "r") as file1, open("/Users/akshitanand/Desktop/Sem VII/Gen AI & Deep L/Lab Work/NLP lab data.txt", "r") as file2:
    doc1 = file1.read()
    doc2 = file2.read()

# Function to clean the text (remove stop words and punctuation)
def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    words = text.split()
    words = [word.lower() for word in words if word.lower() not in ENGLISH_STOP_WORDS]  # Remove stopwords
    return ' '.join(words)  # Return cleaned text as a single string

# Function to get word frequency
def get_word_frequency(text):
    words = text.split()
    return Counter(words)

# Clean the documents
doc1_clean = clean_text(doc1)
doc2_clean = clean_text(doc2)

# Get word frequencies
doc1_freq = get_word_frequency(doc1_clean)
doc2_freq = get_word_frequency(doc2_clean)

# Find common words between the two documents
common_words = set(doc1_freq.keys()).intersection(set(doc2_freq.keys()))
print("\nCommon Words and their Frequencies in Both Documents:")
for word in common_words:
    print(f"{word}: Document 1 - {doc1_freq[word]}, Document 2 - {doc2_freq[word]}")

# Find unique words in each document
unique_words_doc1 = set(doc1_freq.keys()) - set(doc2_freq.keys())
unique_words_doc2 = set(doc2_freq.keys()) - set(doc1_freq.keys())

print("\nUnique Words in Document 1:")
for word in unique_words_doc1:
    print(f"{word}: {doc1_freq[word]}")

print("\nUnique Words in Document 2:")
for word in unique_words_doc2:
    print(f"{word}: {doc2_freq[word]}")

# Function to count stop words in the original text
def get_stopword_frequency(text):
    words = text.split()
    stopwords_freq = Counter(word.lower() for word in words if word.lower() in ENGLISH_STOP_WORDS)
    return stopwords_freq

# Get stop word frequencies for both documents
doc1_stopwords_freq = get_stopword_frequency(doc1)
doc2_stopwords_freq = get_stopword_frequency(doc2)

print("\nStop Words and their Frequencies in Document 1:")
for word, freq in doc1_stopwords_freq.items():
    print(f"{word}: {freq}")

print("\nStop Words and their Frequencies in Document 2:")
for word, freq in doc2_stopwords_freq.items():
    print(f"{word}: {freq}")

# Vectorize the original documents
vectorizer = CountVectorizer()
X_original = vectorizer.fit_transform([doc1, doc2])

# Compute cosine similarity for original documents
similarity_matrix_original = cosine_similarity(X_original)

print("\nCosine Similarity Matrix (Original Documents):")
print(similarity_matrix_original)

# Vectorize the cleaned documents
X_cleaned = vectorizer.fit_transform([doc1_clean, doc2_clean])

# Compute cosine similarity for cleaned documents
similarity_matrix_cleaned = cosine_similarity(X_cleaned)

print("\nCosine Similarity Matrix (Cleaned Documents):")
print(similarity_matrix_cleaned)

# Generate and display the term-document matrix for cleaned documents
terms = vectorizer.get_feature_names_out()
term_document_matrix = X_cleaned.toarray()

# Convert to a DataFrame for better visualization
df = pd.DataFrame(term_document_matrix, columns=terms, index=["Document1", "Document2"])

# Display the term-document matrix
print("\nTerm-Document Matrix:")
print(df)
