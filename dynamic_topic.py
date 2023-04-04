#First topic: NFL
#Second topic: XFL
#Third topic: NBA
#Fourth topic: Facebook
#Fifth topic: Twitter
#Sixth topic: France
#Seventh topic: Mexico
#Eighth topic: World War II
#Ninth topic: Cybersecurity
#Tenth topic: Marvel

import os, glob
from gensim.models import LdaSeqModel

path1 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//TopicModeling//Mixed Articles 2.0//Time1//'
path2 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//TopicModeling//Mixed Articles 2.0//Time2//'
path3 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//TopicModeling//Mixed Articles 2.0//Time3//'
path4 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//TopicModeling//Mixed Articles 2.0//Time4//'
path5 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//TopicModeling//Mixed Articles 2.0//Time5//'
path6 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//TopicModeling//Mixed Articles 2.0//Time6//'
path7 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//TopicModeling//Mixed Articles 2.0//Time7//'
path8 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//TopicModeling//Mixed Articles 2.0//Time8//'
path9 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//TopicModeling//Mixed Articles 2.0//Time9//'
path10 = 'C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//TopicModeling//Mixed Articles 2.0//Time10//'

def extract_documents():
    folder1 = os.listdir(path1)
    folder2 = os.listdir(path2)
    folder3 = os.listdir(path3)
    folder4 = os.listdir(path4)
    folder5 = os.listdir(path5)
    folder6 = os.listdir(path6)
    folder7 = os.listdir(path7)
    folder8 = os.listdir(path8)
    folder9 = os.listdir(path9)
    folder10 = os.listdir(path10)

    for i in range(20): #Time 1
        with open(path1 + folder1[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')
    
    for i in range(24): #Time 2
        with open(path2 + folder2[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')

    for i in range(24): #Time 3
        with open(path3 + folder3[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')

    for i in range(20): #Time 4
        with open(path4 + folder4[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')

    for i in range(21): #Time 5
        with open(path5 + folder5[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')

    for i in range(22): #Time 6
        with open(path6 + folder6[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')
    
    for i in range(17): #Time 7
        with open(path7 + folder7[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')

    for i in range(18): #Time 8
        with open(path8 + folder8[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')

    for i in range(16): #Time 9
        with open(path9 + folder9[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')

    for i in range(18): #Time 10
        with open(path10 + folder10[i], 'rb') as file:
            yield file.read().decode('utf-8', errors='replace')


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
    time_slice=[20, 24, 24, 20, 21, 22, 17, 18, 16, 18], 
    id2word=id2word,
    num_topics=10, 
    chunksize=1)

print('Topic word vectors:')
from pprint import pprint
topics = ldaseq.print_topics(top_terms=10) #Most common words for each topic
pprint(topics)

print('------------------------------------------------')
print('Document topic vectors:')

for doc in range(200):
    print('Document', doc + 1)
    document_topics = ldaseq.doc_topics(doc)
    pprint(document_topics)

print('------------------------------------------------')
print('Relevant words for each timeslice:')

for i in range(10): #Most common words for each topic, per each time slice
    topic_times = ldaseq.print_topic_times(i, top_terms=5)
    print('Topic', i + 1)
    pprint(topic_times)
