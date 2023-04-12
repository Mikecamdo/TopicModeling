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

time1 = []
time2 = []
time3 = []
time4 = []
time5 = []
time6 = []
time7 = []
time8 = []
time9 = []
time10 = []

for i in range(20): #Time 1
    temp = folder1[i]
    temp = temp.replace('.txt', '')
    number = int(temp)
    if number <= 20:
        time1.append('NFL')
    elif number <= 40:
        time1.append('XFL')
    elif number <= 60:
        time1.append('NBA')
    elif number <= 80:
        time1.append('Facebook')
    elif number <= 100:
        time1.append('Twitter')
    elif number <= 120:
        time1.append('France')
    elif number <= 140:
        time1.append('Mexico')
    elif number <= 160:
        time1.append('WW2')
    elif number <= 180:
        time1.append('Cybersecurity')
    else:
        time1.append('Marvel')

for i in range(24): #Time 2
    temp = folder2[i]
    temp = temp.replace('.txt', '')
    number = int(temp)
    if number <= 20:
        time2.append('NFL')
    elif number <= 40:
        time2.append('XFL')
    elif number <= 60:
        time2.append('NBA')
    elif number <= 80:
        time2.append('Facebook')
    elif number <= 100:
        time2.append('Twitter')
    elif number <= 120:
        time2.append('France')
    elif number <= 140:
        time2.append('Mexico')
    elif number <= 160:
        time2.append('WW2')
    elif number <= 180:
        time2.append('Cybersecurity')
    else:
        time2.append('Marvel')

for i in range(24): #Time 3
    temp = folder3[i]
    temp = temp.replace('.txt', '')
    number = int(temp)
    if number <= 20:
        time3.append('NFL')
    elif number <= 40:
        time3.append('XFL')
    elif number <= 60:
        time3.append('NBA')
    elif number <= 80:
        time3.append('Facebook')
    elif number <= 100:
        time3.append('Twitter')
    elif number <= 120:
        time3.append('France')
    elif number <= 140:
        time3.append('Mexico')
    elif number <= 160:
        time3.append('WW2')
    elif number <= 180:
        time3.append('Cybersecurity')
    else:
        time3.append('Marvel')
        
for i in range(20): #Time 4
    temp = folder4[i]
    temp = temp.replace('.txt', '')
    number = int(temp)
    if number <= 20:
        time4.append('NFL')
    elif number <= 40:
        time4.append('XFL')
    elif number <= 60:
        time4.append('NBA')
    elif number <= 80:
        time4.append('Facebook')
    elif number <= 100:
        time4.append('Twitter')
    elif number <= 120:
        time4.append('France')
    elif number <= 140:
        time4.append('Mexico')
    elif number <= 160:
        time4.append('WW2')
    elif number <= 180:
        time4.append('Cybersecurity')
    else:
        time4.append('Marvel')
        
for i in range(21): #Time 5
    temp = folder5[i]
    temp = temp.replace('.txt', '')
    number = int(temp)
    if number <= 20:
        time5.append('NFL')
    elif number <= 40:
        time5.append('XFL')
    elif number <= 60:
        time5.append('NBA')
    elif number <= 80:
        time5.append('Facebook')
    elif number <= 100:
        time5.append('Twitter')
    elif number <= 120:
        time5.append('France')
    elif number <= 140:
        time5.append('Mexico')
    elif number <= 160:
        time5.append('WW2')
    elif number <= 180:
        time5.append('Cybersecurity')
    else:
        time5.append('Marvel')
        
for i in range(22): #Time 6
    temp = folder6[i]
    temp = temp.replace('.txt', '')
    number = int(temp)
    if number <= 20:
        time6.append('NFL')
    elif number <= 40:
        time6.append('XFL')
    elif number <= 60:
        time6.append('NBA')
    elif number <= 80:
        time6.append('Facebook')
    elif number <= 100:
        time6.append('Twitter')
    elif number <= 120:
        time6.append('France')
    elif number <= 140:
        time6.append('Mexico')
    elif number <= 160:
        time6.append('WW2')
    elif number <= 180:
        time6.append('Cybersecurity')
    else:
        time6.append('Marvel')
        
for i in range(17): #Time 7
    temp = folder7[i]
    temp = temp.replace('.txt', '')
    number = int(temp)
    if number <= 20:
        time7.append('NFL')
    elif number <= 40:
        time7.append('XFL')
    elif number <= 60:
        time7.append('NBA')
    elif number <= 80:
        time7.append('Facebook')
    elif number <= 100:
        time7.append('Twitter')
    elif number <= 120:
        time7.append('France')
    elif number <= 140:
        time7.append('Mexico')
    elif number <= 160:
        time7.append('WW2')
    elif number <= 180:
        time7.append('Cybersecurity')
    else:
        time7.append('Marvel')
        
for i in range(18): #Time 8
    temp = folder8[i]
    temp = temp.replace('.txt', '')
    number = int(temp)
    if number <= 20:
        time8.append('NFL')
    elif number <= 40:
        time8.append('XFL')
    elif number <= 60:
        time8.append('NBA')
    elif number <= 80:
        time8.append('Facebook')
    elif number <= 100:
        time8.append('Twitter')
    elif number <= 120:
        time8.append('France')
    elif number <= 140:
        time8.append('Mexico')
    elif number <= 160:
        time8.append('WW2')
    elif number <= 180:
        time8.append('Cybersecurity')
    else:
        time8.append('Marvel')
        
for i in range(16): #Time 9
    temp = folder9[i]
    temp = temp.replace('.txt', '')
    number = int(temp)
    if number <= 20:
        time9.append('NFL')
    elif number <= 40:
        time9.append('XFL')
    elif number <= 60:
        time9.append('NBA')
    elif number <= 80:
        time9.append('Facebook')
    elif number <= 100:
        time9.append('Twitter')
    elif number <= 120:
        time9.append('France')
    elif number <= 140:
        time9.append('Mexico')
    elif number <= 160:
        time9.append('WW2')
    elif number <= 180:
        time9.append('Cybersecurity')
    else:
        time9.append('Marvel')
        
for i in range(18): #Time 10
    temp = folder10[i]
    temp = temp.replace('.txt', '')
    number = int(temp)
    if number <= 20:
        time10.append('NFL')
    elif number <= 40:
        time10.append('XFL')
    elif number <= 60:
        time10.append('NBA')
    elif number <= 80:
        time10.append('Facebook')
    elif number <= 100:
        time10.append('Twitter')
    elif number <= 120:
        time10.append('France')
    elif number <= 140:
        time10.append('Mexico')
    elif number <= 160:
        time10.append('WW2')
    elif number <= 180:
        time10.append('Cybersecurity')
    else:
        time10.append('Marvel')

time1.sort()
time2.sort()
time3.sort()
time4.sort()
time5.sort()
time6.sort()
time7.sort()
time8.sort()
time9.sort()
time10.sort()

print('Time 1', time1)
print('Time 2', time2)
print('Time 3', time3)
print('Time 4', time4)
print('Time 5', time5)
print('Time 6', time6)
print('Time 7', time7)
print('Time 8', time8)
print('Time 9', time9)
print('Time 10', time10)