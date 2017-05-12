# look up synonyms to words, antonyms to words and find the contexxts to words
# and various meanings

from nltk.corpus import wordnet

syns = wordnet.synsets("program")
index = 1
# name of the synset
print(syns[index].name())

# just the word
print(syns[index].lemmas()[0].name())

# definition
print(syns[index].definition())

# examples
print(syns[index].examples())

# printing synonyms and antonyms

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

# similarity

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("man.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cactus.n.01")
print(w1.wup_similarity(w2))
