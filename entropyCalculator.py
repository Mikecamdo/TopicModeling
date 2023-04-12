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
entropy_finder = { }
for key in sorted_temp:
    print(origTopics[topic_counter], (counter + 1),':', sorted_temp[key])
    entropy_finder.update({origTopics[topic_counter] + ' ' + str((counter + 1)) + ':' : sorted_temp[key]})
    counter += 1
    if counter == 20:
        topic_counter += 1
        counter = 0

import numpy as np

origTopicsNums = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]