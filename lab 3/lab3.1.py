from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

file = 

singles = [stemmer.stem(plural) for plural in plurals]

print(' '.join(singles))

print(stemmer.stem('studying'))

