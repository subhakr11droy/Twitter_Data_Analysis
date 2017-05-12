from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
words = ['python', 'pythoned', 'pythoning', 'pythoned', 'pythonly']

# for w in words:
#     print(ps.stem(w))

new_text = "It is important to be pythonly while you are pythoning with python. All pythoners have poorly pythoned atleast once!"
new_words = word_tokenize(new_text)

for w in new_words:
    print(ps.stem(w))
