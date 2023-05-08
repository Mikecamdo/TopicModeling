import os, glob
from gensim.models import LdaSeqModel

def extract_documents():
    files = [
        "1969-70.txt",
        "1970-71.txt",
        "1971-72.txt",
        "1972-73.txt",
        "1973-74.txt",
        "1974-75.txt",
        "1975-76.txt",
        "1976-77.txt",
        "1977-78.txt",
        "1978-79.txt",
        "1979-80.txt",
        "1980-81.txt",
        "1981-82.txt",
        "1982-83.txt",
        "1983-84.txt",
        "1984-85.txt",
        "1985-86.txt",
        "1986-87.txt",
        "1987-88.txt",
        "1988-89.txt",
        "1989-90.txt",
        "1990-91.txt",
        "1991-92.txt",
        "1992-93.txt",
        "1993-94.txt",
        "1994-95.txt",
        "1995-96.txt",
        "1996-97.txt"
    ]

    each_paragraph = ""
    paragraphs = []

    for textFile in files:
        file = open(textFile, "rb")
        text = file.read().decode('utf-8', errors='replace').strip().replace('\r', ' ').split(sep='\n')

        for line in text:
            each_paragraph += line
            if len(line) < 70:
                if len(each_paragraph) > 70:
                    paragraphs.append(each_paragraph)
                    each_paragraph = ""

    paragraphs.append(each_paragraph)
    return paragraphs


docs = list(extract_documents())

from nltk.tokenize import RegexpTokenizer

# Split the documents into tokens.
print('Splitting into tokens')
tokenizer = RegexpTokenizer(r'\w+')
for idx in range(len(docs)):
    docs[idx] = docs[idx].lower()  # Convert to lowercase.
    docs[idx] = tokenizer.tokenize(docs[idx])  # Split into words.

# Remove numbers, but not words that contain numbers.
print('Removing numbers')
docs = [[token for token in doc if not token.isnumeric()] for doc in docs]

# Remove words that are only one character.
print('Remove single characters')
docs = [[token for token in doc if len(token) > 1] for doc in docs]

# Lemmatize the documents.
print('Lemmatizing words')
from nltk.stem.wordnet import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
docs = [[lemmatizer.lemmatize(token) for token in doc] for doc in docs]

# Remove stop words.
print('Removing stop words')
from nltk.corpus import stopwords

stopWords = set(stopwords.words('english'))

for doc in docs:
    for token in doc:
        if token in stopWords:
            doc.remove(token)

'''
# Compute bigrams.
from gensim.models import Phrases

# Add bigrams and trigrams to docs (only ones that appear 20 times or more).
bigram = Phrases(docs, min_count=20)
for idx in range(len(docs)):
    for token in bigram[docs[idx]]:
        if '_' in token:
            # Token is a bigram, add to document.
            docs[idx].append(token)
'''

from gensim.corpora import Dictionary
# Create a dictionary representation of the documents.
print('Creating dictionary representation of the documents')
dictionary = Dictionary(docs)

# Filter out words that occur less than 5 documents, or more than 50% of the documents.
print('Filtering out words that occur in less than 5 documents, or more than 50 percent of the documents')
dictionary.filter_extremes(no_below=5, no_above=0.5)

# Bag-of-words representation of the documents.
print('Creating bag-of-words representation of the documents')
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

from pprint import pprint
print('Writing to topic-word-vectors.txt')
with open('topic-word-vectors.txt', 'w') as f:
    f.write('Topic word vectors:')
    f.write('\n')
    topics = ldaseq.print_topics(top_terms=10) #Most common words for each topic
    for topic in topics:
        f.write(str(topic))
        f.write('\n')

print('------------------------------------------------')
print('Writing to document-topic-vectors.txt')
with open('document-topic-vectors.txt', 'w') as f:
    f.write('Document topic vectors:')
    f.write('\n')
    for doc in range(200):
        f.write('Document ')
        f.write(str(doc + 1))
        f.write('\n')
        document_topics = ldaseq.doc_topics(doc)
        f.write(str(document_topics))
        f.write('\n')

print('------------------------------------------------')
print('Writing to time-slice-relevance.txt')
with open('time-slice-relevance.txt', 'w') as f:
    f.write('Relevant words for each timeslice:')
    f.write('\n')
    for i in range(10): #Most common words for each topic, per each time slice
        topic_times = ldaseq.print_topic_times(i, top_terms=5)
        f.write('Topic ')
        f.write(str(i + 1))
        f.write('\n')
        for topic in topic_times:
            f.write(str(topic))
            f.write('\n')

print('Done')
