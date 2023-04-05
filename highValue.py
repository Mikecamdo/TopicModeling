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
            print(float(number), answer.get(doc_num))
            if float(number) > answer.get(doc_num):
                answer.update({doc_num: float(number)})
                answer_topic.update({doc_num: topic_num})
            topic_num += 1

from pprint import pprint
pprint(answer_topic)