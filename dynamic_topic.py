#First topic: Marvel
#Second topic: Russia
#Third topic: NFL
#Fourth topic: Cybersecurity
#Fifth topic: Morgan Wallen
#Sixth topic: 
#Seventh topic: 
#Eighth topic: 
#Ninth topic: 
#Tenth topic: 

import os, glob
from gensim.models import LdaSeqModel

path1 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//Project//Mixed Articles//Time1//'
path2 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//Project//Mixed Articles//Time2//'
path3 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//Project//Mixed Articles//Time3//'
path4 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//Project//Mixed Articles//Time4//'
path5 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//Project//Mixed Articles//Time5//'
def extract_documents():
    folder1 = os.listdir(path1)
    folder2 = os.listdir(path2)
    folder3 = os.listdir(path3)
    folder4 = os.listdir(path4)
    folder5 = os.listdir(path5)

    for i in range(10):
        with open(path1 + folder1[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')
    
    for i in range(10):
        with open(path2 + folder2[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')

    for i in range(10):
        with open(path3 + folder3[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')

    for i in range(10):
        with open(path4 + folder4[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')

    for i in range(10):
        with open(path5 + folder5[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')

    #print(folder1)
    #print(folder2)
    #print(folder3)
    #print(folder4)
    #print(folder5)


docs = list(extract_documents())

from nltk.tokenize import RegexpTokenizer

# Split the documents into tokens.
tokenizer = RegexpTokenizer(r'\w+')
for idx in range(len(docs)):
    docs[idx] = docs[idx].lower()  # Convert to lowercase.
    docs[idx] = tokenizer.tokenize(docs[idx])  # Split into words.

# Remove numbers, but not words that contain numbers.
docs = [[token for token in doc if not token.isnumeric()] for doc in docs]

# Remove words that are only one character.
docs = [[token for token in doc if len(token) > 1] for doc in docs]

# Lemmatize the documents.
from nltk.stem.wordnet import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
docs = [[lemmatizer.lemmatize(token) for token in doc] for doc in docs]

# Compute bigrams.
from gensim.models import Phrases

# Add bigrams and trigrams to docs (only ones that appear 20 times or more).
bigram = Phrases(docs, min_count=20)
for idx in range(len(docs)):
    for token in bigram[docs[idx]]:
        if '_' in token:
            # Token is a bigram, add to document.
            docs[idx].append(token)

from gensim.corpora import Dictionary

# Create a dictionary representation of the documents.
dictionary = Dictionary(docs)

# Filter out words that occur less than 5 documents, or more than 50% of the documents.
dictionary.filter_extremes(no_below=5, no_above=0.5)

# Bag-of-words representation of the documents.
corpus = [dictionary.doc2bow(doc) for doc in docs]

# Make an index to word dictionary.
temp = dictionary[0]  # This is only to "load" the dictionary.
id2word = dictionary.id2token

print('Making Dynamic Topic Model')
ldaseq = LdaSeqModel(
    corpus=corpus, 
    time_slice=[10, 10, 10, 10, 10], 
    id2word=id2word,
    num_topics=5, 
    chunksize=1)

from pprint import pprint
topics = ldaseq.print_topics(top_terms=25)
pprint(topics)

for i in range(5):
    topic_times = ldaseq.print_topic_times(i, top_terms=5)
    print('Topic', i + 1)
    pprint(topic_times)
#for topic in topics:
#    pprint(topic)

'''
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import io
import os
import re
import tarfile

import smart_open

def extract_documents():
    for filename in os.listdir(os.getcwd()):
        with smart_open.open(os.path.join(os.getcwd(), filename), "rb") as f:
            print('Success')
            yield f

#def extract_documents():
#    for i in range (1, 51): 
#        with open('./Articles/' + str(i) + '.txt') as file:
#            print(i)
#            yield file


docs = list(extract_documents())
#    with smart_open.open(url, "rb") as file:
#        with tarfile.open(fileobj=file) as tar:
#            for member in tar.getmembers():
#                if member.isfile() and re.search(r'nipstxt/nips\d+/\d+\.txt', member.name):
#                    member_bytes = tar.extractfile(member).read()
#                    yield member_bytes.decode('utf-8', errors='replace')

#docs = list(extract_documents())

'''