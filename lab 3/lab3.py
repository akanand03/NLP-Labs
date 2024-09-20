import re

class PorterStemmer:
    def __init__(self):
        pass
    
    def contains_vowel(self, word):
        for letter in word:
            if letter in 'aeiou':
                return True
        return False

    def ends_with_double_consonant(self, word):
        if len(word) >= 2 and word[-1] == word[-2] and word[-1] not in 'aeiou':
            return True
        return False

    def cvc_format(self, word):
        if len(word) >= 3 and word[-1] not in 'aeiou' and word[-2] in 'aeiou' and word[-3] not in 'aeiou':
            if word[-1] not in ['w', 'x', 'y']:
                return True
        return False
    
    def measure(self, word):
        vc_pattern = ''
        for letter in word:
            if letter in 'aeiou':
                vc_pattern += 'V'
            else:
                vc_pattern += 'C'
        
        return vc_pattern.count('VC')

    def stem(self, word):
        if word.endswith('sses'):
            word = word[:-4] + 'ss'
        elif word.endswith('ies'):
            word = word[:-3] + 'i'
        elif word.endswith('ss'):
            word = word[:-2] + 'ss'
        elif word.endswith('s'):
            word = word[:-1]

        m = self.measure(word)
        if m > 1 and word.endswith('eed'):
            word = word[:-3] + 'ee'
        elif self.contains_vowel(word[:-2]) and word.endswith('ed'):
            word = word[:-2]
        elif self.contains_vowel(word[:-3]) and word.endswith('ing'):
            word = word[:-3]

        if word.endswith('at'):
            word = word[:-2] + 'ate'
        elif word.endswith('bl'):
            word = word[:-2] + 'ble'
        elif self.ends_with_double_consonant(word) and not word.endswith(('l', 's', 'z')):
            word = word[:-1]
        elif m == 1 and self.cvc_format(word):
            word = word + 'e'

        if self.contains_vowel(word[:-1]) and word.endswith('y'):
            word = word[:-1] + 'i'

        if m > 0:
            if word.endswith('ational'):
                word = word[:-7] + 'ate'
            elif word.endswith('ization'):
                word = word[:-7] + 'ize'
            elif word.endswith('biliti'):
                word = word[:-6] + 'ble'

        if m > 0:
            if word.endswith('icate'):
                word = word[:-5] + 'ic'
            elif word.endswith('ful'):
                word = word[:-3]
            elif word.endswith('ness'):
                word = word[:-4]

        if m > 0:
            if word.endswith('ance'):
                word = word[:-4]
            elif word.endswith('ent'):
                word = word[:-3]
            elif word.endswith('ive'):
                word = word[:-3]

        if m > 1 and word.endswith('e'):
            word = word[:-1]
        elif m == 1 and not self.cvc_format(word) and word.endswith('ness'):
            word = word[:-4]

        if m > 1 and self.ends_with_double_consonant(word) and word.endswith('l'):
            word = word[:-1]

        return word


class FurtherModifiedPorterStemmer(PorterStemmer):
    def stem(self, word):
        original_word = word  # Store the original word
        
        word = super().stem(word)
        
        if word == "studi":
            return "study"
        if word == "babi":
            return "baby"
        if word.endswith("ies"):
            return word[:-3] + "y"
        if word == "stud":
            return "student"
        
        return word


# Function to load and tokenize text file
def load_text_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
    words = re.findall(r'\b\w+\b', text)  # Tokenizing using regex
    return words

# Function to apply stemming and output results
def analyze_stemming(file_path):
    words = load_text_file(file_path)
    stemmer = FurtherModifiedPorterStemmer()

    incorrect_words = []  # List to store words that were incorrectly stemmed
    corrected_words = []  # List to store the original, correct words

    print(f"{'Original Word':<20} {'Stemmed Word':<20}")
    print('-' * 40)

    for word in words:
        original_word = word
        stemmed_word = stemmer.stem(word)
        print(f"{original_word:<20} {stemmed_word:<20}")
        
        if original_word != stemmed_word:
            # Store words with changes
            incorrect_words.append(stemmed_word)
            corrected_words.append(original_word)

    # Write stemmed words (incorrect words) and their original forms to files
    with open("incorrect_words.txt", "w") as incorrect_file:
        for word in incorrect_words:
            incorrect_file.write(f"{word}\n")

    with open("corrected_words.txt", "w") as corrected_file:
        for word in corrected_words:
            corrected_file.write(f"{word}\n")

    print("\nIncorrect (stemmed) and corrected (original) words have been written to the files.")

# Example usage
file_path = '/Users/akshitanand/Desktop/NLP Lab Work/lab2/test2.txt'  # Replace with actual path
analyze_stemming(file_path)
