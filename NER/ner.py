# command to run before code
'''
! pip install spacy
! pip install nltk
! python - m spacy download en_core_web_sm
'''

import spacy
from spacy import displacy
# imports and load spacy english language package
nlp = spacy.load('en_core_web_sm')

# Load the text and process it
text = ('''"Python is an interpreted, high-level and general-purpose programming language.
    Pythons design philosophy emphasizes code readability with its notable use of significant indentation.
    Its language constructs and object-oriented approach aim to help programmers write clear and logical code for small and large-scale projects.''')
# text = '''In this directory I place short essays (anything from 500 to 5000 words) on various Python subjects.
#     See also a collection of presentations I have given.
#     See also my blog at blogspot.com and my previous blog at artima.com.'''

doc = nlp(text)

sentences = list(doc.sents)
print(sentences)

# tokenization
for token in doc:
    print(token.text)

# print entities
ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
print(ents)

# now we use displaycy function on doc2
displacy.render(doc, style='ent', jupyter=True)
