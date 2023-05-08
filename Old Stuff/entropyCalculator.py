answer = { }
for i in range(200):
    answer.update({i + 1: 0.0})
answer_topic = { }
for i in range(200):
    answer.update({i + 1: 0})
doc_num = 0
topic_num = 1
with open ('doc_topic_vectors.txt') as file:
    for line in file:
        line = line.strip()
        words = line.split()
        if len(words) == 0:
            continue
        elif words[0] == 'Document':
            doc_num += 1
            topic_num = 1
            continue
        
        for number in words:
            number = number.replace('array([', '')
            number = number.replace(',', '')
            number = number.replace('])', '')
            if float(number) > answer.get(doc_num):
                answer.update({doc_num: float(number)})
                answer_topic.update({doc_num: topic_num})
            topic_num += 1

import os
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

keys = list(answer_topic.keys())

temp = { }
counter = 0
for i in range(20):
    temp.update({folder1[i]: answer_topic[keys[counter]]})
    counter += 1

for i in range(24): #Time 2
    temp.update({folder2[i]: answer_topic[keys[counter]]})
    counter += 1

for i in range(24): #Time 3
    temp.update({folder3[i]: answer_topic[keys[counter]]})
    counter += 1

for i in range(20): #Time 4
    temp.update({folder4[i]: answer_topic[keys[counter]]})
    counter += 1

for i in range(21): #Time 5
    temp.update({folder5[i]: answer_topic[keys[counter]]})
    counter += 1

for i in range(22): #Time 6
    temp.update({folder6[i]: answer_topic[keys[counter]]})
    counter += 1

for i in range(17): #Time 7
    temp.update({folder7[i]: answer_topic[keys[counter]]})
    counter += 1

for i in range(18): #Time 8
    temp.update({folder8[i]: answer_topic[keys[counter]]})
    counter += 1

for i in range(16): #Time 9
    temp.update({folder9[i]: answer_topic[keys[counter]]})
    counter += 1

for i in range(18): #Time 10
    temp.update({folder10[i]: answer_topic[keys[counter]]})
    counter += 1

from natsort import natsorted
theKeys = list(temp.keys())
theKeys = natsorted(theKeys)
sorted_temp = {i: temp[i] for i in theKeys}

origTopics = ['NFL', 'XFL', 'NBA', 'Facebook', 'Twitter', 'France', 'Mexico', 'World War II', 'Cybersecurity', 'Marvel']
counter = 0
topic_counter = 0
entropy_finder_articles = [ ]
entropy_finder_topics = [ ]
for key in sorted_temp:
    entropy_finder_articles.append(origTopics[topic_counter] + ' ' + str((counter + 1)) + ':')
    entropy_finder_topics.append(sorted_temp[key])
    counter += 1
    if counter == 20:
        topic_counter += 1
        counter = 0

import numpy as np
for i in range(200):
    print(entropy_finder_articles[i], entropy_finder_topics[i])

origTopicsNums = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]

#Real Topics
nfl_entropy = -(18/20) * np.log2(18/20) - (1/20) * np.log2(1/20) - (1/20) * np.log2(1/20)

xfl_entropy = -(15/20) * np.log2(15/20) - (4/20) * np.log2(4/20) - (1/20) * np.log2(1/20)

nba_entropy = -(2/20) * np.log2(2/20) - (3/20) * np.log2(3/20) - (15/20) * np.log2(15/20)

facebook_entropy = -(1/20) * np.log2(1/20) - (1/20) * np.log2(1/20) - (18/20) * np.log2(18/20)

twitter_entropy = -(1/20) * np.log2(1/20) - (2/20) * np.log2(2/20) - (15/20) * np.log2(15/20) - (2/20) * np.log2(2/20)

france_entropy = -(2/20) * np.log2(2/20) - (1/20) * np.log2(1/20) - (13/20) * np.log2(13/20) - (1/20) * np.log2(1/20) - (3/20) * np.log2(3/20)

mexico_entropy = -(14/20) * np.log2(14/20) - (1/20) * np.log2(1/20) - (2/20) * np.log2(2/20) - (2/20) * np.log2(2/20) - (1/20) * np.log2(1/20)

ww2_entropy = -(12/20) * np.log2(12/20) - (1/20) * np.log2(1/20) - (2/20) * np.log2(2/20) - (2/20) * np.log2(2/20) - (3/20) * np.log2(3/20)

cybersecurity_entropy = -(2/20) * np.log2(2/20) - (1/20) * np.log2(1/20) - (5/20) * np.log2(5/20) - (12/20) * np.log2(12/20)

marvel_entropy = -(17/20) * np.log2(17/20) - (1/20) * np.log2(1/20) - (2/20) * np.log2(2/20)

#LDA Topics
topic1_entropy = -(18/35) * np.log2(18/35) - (15/35) * np.log2(15/35) - (2/35) * np.log2(2/35)
topic2_entropy = -(1/32) * np.log2(1/32) - (1/32) * np.log2(1/32) - (2/32) * np.log2(2/32) - (14/32) * np.log2(14/32) - (12/32) * np.log2(12/32) - (2/32) * np.log2(2/32)
topic3_entropy = -(1/8) * np.log2(1/8) - (4/8) * np.log2(4/8) - (3/8) * np.log2(3/8)
topic4_entropy = -(15/17) * np.log2(15/17) - (1/17) * np.log2(1/17) - (1/17) * np.log2(1/17)
topic5_entropy = -(1/18) * np.log2(1/18) - (1/18) * np.log2(1/18) - (13/18) * np.log2(13/18) - (1/18) * np.log2(1/18) - (2/18) * np.log2(2/18)
topic6_entropy = -(18/26) * np.log2(18/26) - (2/26) * np.log2(2/26) - (1/26) * np.log2(1/26) - (2/26) * np.log2(2/26) - (2/26) * np.log2(2/26) - (1/26) * np.log2(1/26)
topic7_entropy = -(1/18) * np.log2(1/18) - (17/18) * np.log2(17/18)
topic8_entropy = -(15/29) * np.log2(15/29) - (3/29) * np.log2(3/29) - (2/29) * np.log2(2/29) - (3/29) * np.log2(3/29) - (5/29) * np.log2(5/29) - (1/29) * np.log2(1/29)
topic9_entropy = -(1/13) * np.log2(1/13) - (12/13) * np.log2(12/13)
topic10_entropy = -(2/4) * np.log2(2/4) - (2/4) * np.log2(2/4)

print('NFL', nfl_entropy)
print('XFL', xfl_entropy)
print('NBA', nba_entropy)
print('Facebook', facebook_entropy)
print('Twitter', twitter_entropy)
print('France', france_entropy)
print('Mexico', mexico_entropy)
print('World War 2', ww2_entropy)
print('Cybersecurity', cybersecurity_entropy)
print('Marvel', marvel_entropy)

print('LDA Topic 1', topic1_entropy)
print('LDA Topic 2', topic2_entropy)
print('LDA Topic 3', topic3_entropy)
print('LDA Topic 4', topic4_entropy)
print('LDA Topic 5', topic5_entropy)
print('LDA Topic 6', topic6_entropy)
print('LDA Topic 7', topic7_entropy)
print('LDA Topic 8', topic8_entropy)
print('LDA Topic 9', topic9_entropy)
print('LDA Topic 10', topic10_entropy)