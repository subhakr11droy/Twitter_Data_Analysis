import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

tokenized = PunktSentenceTokenizer(train_text).tokenize(sample_text)


def process_content():
    for i in tokenized:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)

        chunkGram = r""""Chunk: {<.?>+}
                                }<VB.?|IN|TO|DT>{"""

        chunk_parser = nltk.RegexpParser(chunkGram)
        chunked = chunk_parser.parse(tagged)
        chunked.draw()


process_content()
