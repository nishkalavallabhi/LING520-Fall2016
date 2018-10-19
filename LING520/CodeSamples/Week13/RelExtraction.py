import nltk
import re

IN = re.compile(r'.*\bin\b(?!\b.+ing)')
#Pattern to capture relations like "YY in XX" but XX does not end in -ing.

for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern = IN):
        print(nltk.sem.rtuple(rel))

'''
Notes:IEER - Information Extraction and Entity Recognition Corpus.
http://www.nltk.org/_modules/nltk/corpus/reader/ieer.html
'''