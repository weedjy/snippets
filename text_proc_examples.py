# The most of the examples are from the article:
# https://medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908

import re
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.stem import WordNetLemmatizer
# from ICE import CollocationExtractor
# from textblob import TextBlob
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

# convert to lowercase
input_str = "The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil."
input_str = input_str.lower()
print(input_str)

# numbers removing
input_str = "Box A contains 3 red and 5 white balls, while Box B contains 4 red and 2 blue balls."
result = re.sub(r'\d+', '', input_str)
print(result)

# punctuation removal

# white spaces removal
example_str = " \t a string example\t "
example_str = example_str.strip()
print(example_str)

# stop words removal
input_str = "NLTK is a leading platform for building Python programs to work with human language data."
stop_words = set(ENGLISH_STOP_WORDS)
tokens = word_tokenize(input_str)
result = [i for i in tokens if i not in stop_words]
print(result)

# stemming
stemmer = PorterStemmer()
input_str = "There are several types of stemming algorithms."
input_str = word_tokenize(input_str)
for word in input_str:
    print(stemmer.stem(word))

# Lemmatization
# The aim of lemmatization, like stemming, is to reduce inflectional forms to
# a common base form. As opposed to stemming, lemmatization does not simply chop off
# inflections. Instead it uses lexical knowledge bases to get the correct base forms of words.
lemmatizer = WordNetLemmatizer()
input_str = "been had done languages cities mice"
input_str = word_tokenize(input_str)
for word in input_str:
    print(lemmatizer.lemmatize(word))

# Part-of-speech tagging
"""
input_str = "Parts of speech examples: an article, to write, interesting, easily, and, of"
result = TextBlob(input_str)
print(result.tags)
"""

# Chunking (shallow parsing)
# Chunking is a natural language process that identifies constituent parts of sentences
# (nouns, verbs, adjectives, etc.) and links them to higher order units that have discrete
# grammatical meanings (noun groups or phrases, verb groups, etc.)

"""
# The first step is to determine the part of speech for each word:
input_str = "A black television and a white stove were bought for the new apartment of John."
result = TextBlob(input_str)
print(result.tags)
# The second step is chunking:
reg_exp = "NP: {<DT>?<JJ>*<NN>}"
rp = nltk.RegexpParser(reg_exp)
result = rp.parse(result.tags)
print(result)
result.draw()
"""

# Named-entity recognition
input_str = "Bill works for Apple so he went to Boston for a conference."
print(ne_chunk(pos_tag(word_tokenize(input_str))))

# Coreference resolution (anaphora resolution)
# Pronouns and other referring expressions should be connected to the right individuals.
# Coreference resolution finds the mentions in a text that refer to the same real-world
# entity. For example, in the sentence, “Andrew said he would buy a car” the pronoun “he”
# refers to the same person, namely to “Andrew”.
# https://corpling.uis.georgetown.edu/xrenner/doc/using.html#importing-as-a-module


# Collocation extraction
# Collocations are word combinations occurring together more often than would be expected
# by chance. Collocation examples are “break the rules,” “free time,” “draw a conclusion,”
# “keep in mind,” “get ready,” and so on.
"""
input_str = ["he and Chazz duel with all keys on the line."]
extractor = CollocationExtractor.with_collocation_pipeline("T1", bing_key="Temp", pos_check=False)
print(extractor.get_collocations_of_length(input_str, length=3))
"""

# Relationship extraction
# Relationship extraction allows obtaining structured information from unstructured sources
# such as raw text. Strictly stated, it is identifying relations (e.g., acquisition, spouse,
# employment) among named entities (e.g., people, organizations, locations). For example,
# from the sentence “Mark and Emily married yesterday,” we can extract the information that
# Mark is Emily’s husband.
# http://www.nltk.org/howto/relextract.html
