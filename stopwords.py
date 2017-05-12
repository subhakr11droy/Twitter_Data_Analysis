from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_text = 'This is an example showing off stop words filtration'
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_text)
list_of_words = [w for w in words if w not in stop_words]
print(list_of_words)
