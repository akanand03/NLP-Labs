import re
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

nltk.download('punkt')
nltk.download('stopwords')

stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

# List of known stemmed words to skip custom stemming
already_stemmed_words = set([
    "technology", "technolog", "analysi", "optim", "comput", "exampl", "defin"
])

def custom_stem_word(word):
   
    word = word.lower()
    
    # Check if the word is already considered stemmed
    if word in already_stemmed_words:
        return word
    
    # Custom suffix removal rules
    if word.endswith('ing'):
        word = word[:-3]
    elif word.endswith('ed'):
        word = word[:-2]
    elif word.endswith('en'):
        word = word[:-1]
    elif word.endswith('es') or word.endswith('s'):
        word = word[:-1] if len(word) > 1 else word
    
    # Fallback to Porter Stemmer for any remaining suffixes
    return stemmer.stem(word)

def clean_and_process_text(text):
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    words = word_tokenize(text)  # Tokenize the text
    processed_words = []
    
    for word in words:
        word_lower = word.lower()
        if word_lower not in stop_words:
            custom_stemmed_word = custom_stem_word(word_lower)
            processed_words.append((word, custom_stemmed_word))

    return processed_words

# Read the contents of the file
input_file_path = "/Users/horde_machine/VSCodeEditor/Extras/University/NLP/one.txt"
output_file_path = "/Users/horde_machine/VSCodeEditor/Extras/University/NLP/one_processed.csv"

with open(input_file_path, "r") as file1:
    doc1 = file1.read()

# Process the document
processed_words_list = clean_and_process_text(doc1)

# Create a DataFrame for the original words and their custom stemmed versions
df_processed_words = pd.DataFrame(processed_words_list, columns=["Original Word", "Custom Stemmed Word"])

# Count the number of words in each column
total_original_words = len(df_processed_words["Original Word"])
total_custom_stemmed_words = len(df_processed_words["Custom Stemmed Word"])

# Add a row for the count of words
summary_row = pd.DataFrame([['Total', 'Total']], columns=["Original Word", "Custom Stemmed Word"])
summary_row.loc[0, "Original Word"] = total_original_words
summary_row.loc[0, "Custom Stemmed Word"] = total_custom_stemmed_words

df_processed_words = pd.concat([df_processed_words, summary_row], ignore_index=True)

# Write the DataFrame to a CSV file
df_processed_words.to_csv(output_file_path, index=False)

print(f"Processed text has been saved to '{output_file_path}'.")

# Display the DataFrame
print("\nOriginal Words and Their Custom Stemmed Versions:")
print(df_processed_words)