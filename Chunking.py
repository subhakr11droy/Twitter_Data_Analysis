import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    for i in tokenized:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)

        chunk_Gram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""
        chunk_parser = nltk.RegexpParser(chunk_Gram)
        chunked = chunk_parser.parse(tagged)
        chunked.draw()
        # print(chunked)


process_content()
