from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

extract = gutenberg.raw("bible-kjv.txt")
st = sent_tokenize(extract)

print(st[1:15])
