answer = { }
for i in range(3984):
    answer.update({i + 1: 0.0})
answer_topic = { }
for i in range(3984):
    answer_topic.update({i + 1: 0})
doc_num = -1
topic_num = 1

with open ('C://Users//mikec_g1kgiu8//OneDrive//Desktop//CS 5322//TopicModeling//Results 2//document-topic-vectors.txt') as file:
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
            number = number.replace('[', '')
            number = number.replace(']', '')
            if number == "":
                continue
            if float(number) > answer.get(doc_num):
                answer.update({doc_num: float(number)})
                answer_topic.update({doc_num: topic_num})
            topic_num += 1



answer_topic_list = { }
for i in range(28):
    answer_topic_list.update({i + 1: [ ]})

time_lengths = [67, 77, 53, 139, 148, 156, 156, 103, 150, 129, 151, 155, 142, 149, 113, 123, 84, 129, 169, 153, 95, 101, 85, 206, 286, 205, 289, 171]
time_period = 1
corrector = 0 #add this much to get right value
for time in time_lengths:
    for i in range(time):
        answer_topic_list[time_period].append(answer_topic[corrector + i + 1])
    
    corrector += time
    time_period += 1

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

counter += 1

for i in range(28):
    sheet1.write(counter, 0, 'Time ' + str(i + 1))
    counter += 1

    sheet1.write(counter, 0, "Topic")
    sheet1.write(counter, 1, "Number of Occurences")
    counter += 1

    sheet1.write(counter, 0, "1")
    sheet1.write(counter, 1, answer_topic_list[i + 1].count(1))
    counter += 1

    sheet1.write(counter, 0, "2")
    sheet1.write(counter, 1, answer_topic_list[i + 1].count(2))
    counter += 1

    sheet1.write(counter, 0, "3")
    sheet1.write(counter, 1, answer_topic_list[i + 1].count(3))
    counter += 1

    sheet1.write(counter, 0, "4")
    sheet1.write(counter, 1, answer_topic_list[i + 1].count(4))
    counter += 1

    sheet1.write(counter, 0, "5")
    sheet1.write(counter, 1, answer_topic_list[i + 1].count(5))
    counter += 1

    sheet1.write(counter, 0, "6")
    sheet1.write(counter, 1, answer_topic_list[i + 1].count(6))
    counter += 1

    sheet1.write(counter, 0, "7")
    sheet1.write(counter, 1, answer_topic_list[i + 1].count(7))
    counter += 1

    sheet1.write(counter, 0, "8")
    sheet1.write(counter, 1, answer_topic_list[i + 1].count(8))
    counter += 1

    sheet1.write(counter, 0, "9")
    sheet1.write(counter, 1, answer_topic_list[i + 1].count(9))
    counter += 1

    sheet1.write(counter, 0, "10")
    sheet1.write(counter, 1, answer_topic_list[i + 1].count(10))
    counter += 2

wb.save('finalHighValue.xls')

print('Done')