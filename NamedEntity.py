import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

tokenize = PunktSentenceTokenizer(train_text).tokenize(sample_text)


def process_content():
    for i in tokenize:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)

        named_ent = nltk.ne_chunk(tagged, binary=True)
        named_ent.draw()


process_content()
