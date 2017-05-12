import nltk
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("ducks"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("rockets"))
print(lemmatizer.lemmatize("feet"))

print(lemmatizer.lemmatize("better", pos='a'))
print(lemmatizer.lemmatize("best", pos='a'))

print(lemmatizer.lemmatize("run", pos='a'))
print(lemmatizer.lemmatize("run"))
