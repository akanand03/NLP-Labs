import os
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from collections import Counter

# File paths
file1_path = "/Users/akshitanand/Desktop/NLP Lab Work/lab2/doc1.txt"
file2_path = "/Users/akshitanand/Desktop/NLP Lab Work/lab2/doc2.txt"

# Read the contents of the files
with open(file1_path, "r") as file1, open(file2_path, "r") as file2:
    doc1 = file1.read()
    doc2 = file2.read()

# Function to count punctuation characters
def count_punctuation(text):
    return len(re.findall(r'[^\w\s]', text))

# Function to clean the text and count removed punctuation
def clean_text_and_count_punctuation(text):
    original_punctuation_count = count_punctuation(text)
    text_cleaned = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    cleaned_punctuation_count = count_punctuation(text_cleaned)
    removed_punctuation_count = original_punctuation_count - cleaned_punctuation_count
    words = text_cleaned.split()
    words = [word.lower() for word in words if word.lower() not in ENGLISH_STOP_WORDS]  # Remove stopwords
    return words, removed_punctuation_count

# Clean and count punctuation for both documents
doc1_clean, doc1_removed_punctuation = clean_text_and_count_punctuation(doc1)
doc2_clean, doc2_removed_punctuation = clean_text_and_count_punctuation(doc2)

# Function to get word frequency
def get_word_frequency(words):
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict

# Get word frequencies for both documents
doc1_word_freq = get_word_frequency(doc1_clean)
doc2_word_freq = get_word_frequency(doc2_clean)

# Convert frequencies to sets of unique words
doc1_unique_words = set(doc1_word_freq.keys())
doc2_unique_words = set(doc2_word_freq.keys())

# Find common words
common_words = doc1_unique_words.intersection(doc2_unique_words)

# Print unique words and their frequencies
print("Unique Words with Frequency in Document 1:")
for word in sorted(doc1_word_freq):
    print(f"{word}: {doc1_word_freq[word]}")

print("\nUnique Words with Frequency in Document 2:")
for word in sorted(doc2_word_freq):
    print(f"{word}: {doc2_word_freq[word]}")

# Print common words and their frequencies
print("\nCommon Words with Frequency in Both Documents:")
for word in sorted(common_words):
    print(f"{word}: Document 1: {doc1_word_freq[word]}, Document 2: {doc2_word_freq[word]}")

# Print removed punctuation counts
print(f"\nTotal Punctuation Removed from Document 1: {doc1_removed_punctuation}")
print(f"Total Punctuation Removed from Document 2: {doc2_removed_punctuation}")

# Print total word count including punctuation
doc1_total_words_including_punctuation = len(doc1.split())
doc2_total_words_including_punctuation = len(doc2.split())
print(f"\nTotal Words Including Punctuation in Document 1: {doc1_total_words_including_punctuation}")
print(f"Total Words Including Punctuation in Document 2: {doc2_total_words_including_punctuation}")

# Print total word count excluding punctuation
doc1_total_words_excluding_punctuation = len(doc1_clean)
doc2_total_words_excluding_punctuation = len(doc2_clean)
print(f"Total Words Excluding Punctuation in Document 1: {doc1_total_words_excluding_punctuation}")
print(f"Total Words Excluding Punctuation in Document 2: {doc2_total_words_excluding_punctuation}")

# Print the size of the text files
doc1_size = os.path.getsize(file1_path)
doc2_size = os.path.getsize(file2_path)
print(f"\nSize of Document 1: {doc1_size} bytes")
print(f"Size of Document 2: {doc2_size} bytes")
