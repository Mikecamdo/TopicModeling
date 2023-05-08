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

#from pprint import pprint
#pprint(answer_topic)
import xlwt
from xlwt import Workbook

wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'Document')
sheet1.write(0, 1, 'Topic')
counter = 1

for key in answer_topic:
    sheet1.write(counter, 0, key)
    sheet1.write(counter, 1, answer_topic[key])
    counter += 1

wb.save('highValue.xls')
print('Done')