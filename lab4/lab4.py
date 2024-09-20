import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from spellchecker import SpellChecker
from nltk.corpus import stopwords
from collections import Counter

# Download stopwords if not already installed
nltk.download('stopwords')
nltk.download('punkt')

# Function to read text from a file
def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Function to list unique words from text, excluding stop words
def get_unique_words(text):
    tokens = word_tokenize(text.lower())  # Tokenize and convert to lowercase
    stop_words = set(stopwords.words('english'))  # Get English stop words
    unique_words = list(set([word for word in tokens if word.isalpha() and word not in stop_words]))  # Exclude stop words and non-alphabetic words
    return unique_words

# Function to perform spell check on unique words
def spell_check_words(words):
    spell = SpellChecker()
    misspelled_words = spell.unknown(words)
    corrections = {word: spell.correction(word) for word in misspelled_words}
    return corrections

# Function to create bigrams from unique words
def generate_bigrams_for_unique_words(words):
    bigrams = list(ngrams(words, 2))  # Generate bigrams for each pair of unique words
    return bigrams

# Function to count occurrences of second words in bigrams and compare with unique words
def count_target_bigrams(bigrams, target_word, unique_words):
    matching_bigrams = [bigram for bigram in bigrams if bigram[0] == target_word and bigram[1] in unique_words]  # Match first word and ensure second word is unique
    return matching_bigrams

# Function to find the bigram with the highest occurrence
def find_highest_occurrence_bigrams(matching_bigrams):
    bigram_counter = Counter(matching_bigrams)
    if bigram_counter:
        most_frequent_bigram = max(bigram_counter, key=bigram_counter.get)
        return most_frequent_bigram, bigram_counter[most_frequent_bigram]
    return None, 0

# Load the text from the file
file_path = 'test.txt'  # Ensure this is the correct path to your file
text = load_text_from_file(file_path)

# Get the unique words from the text, excluding stop words
unique_words = get_unique_words(text)

# Display the unique words
print("Unique Words in the Text:")
print(unique_words)

# Spell check the unique words
misspelled_corrections = spell_check_words(unique_words)

# Display misspelled words and their corrections
if misspelled_corrections:
    print("\nMisspelled Words and Their Corrections:")
    for word, correction in misspelled_corrections.items():
        print(f"{word} -> {correction}")
else:
    print("\nNo misspelled words found.")

# Correct the misspelled words in the unique words list
corrected_words = [misspelled_corrections.get(word, word) for word in unique_words]

# Generate bigrams for the corrected unique words
bigrams_for_corrected_words = generate_bigrams_for_unique_words(corrected_words)

# Display bigrams of corrected unique words
print("\nBigrams for Corrected Unique Words:")
print(bigrams_for_corrected_words)

# Input the target word from the user
target_word = input("\nEnter the target word: ").lower()

# Generate bigrams that match the target word and are part of the unique words
matching_bigrams = count_target_bigrams(bigrams_for_corrected_words, target_word, unique_words)

# Display the number of matching bigrams
print(f"\nNumber of Matching Bigrams for Target Word '{target_word}': {len(matching_bigrams)}")

# Display matching bigrams
if matching_bigrams:
    print("\nMatching Bigrams:")
    for bigram in matching_bigrams:
        print(bigram)
else:
    print(f"No matching bigrams found for the target word '{target_word}'.")

# Find the bigram with the highest occurrence
most_frequent_bigram, occurrences = find_highest_occurrence_bigrams(matching_bigrams)

# Display the bigram with the highest occurrence
if most_frequent_bigram:
    print(f"\nBigram with the Highest Occurrence: {most_frequent_bigram}, Occurrences: {occurrences}")
else:
    print(f"\nNo bigrams found with the target word '{target_word}'.")
