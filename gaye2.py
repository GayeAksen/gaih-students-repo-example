
names = ['John Doe','Jane Doe', 'John Brown', 'Jane Brown', 'Jack Brown']
school =['Yale', 'MIT', 'Oxford','Cambridge', 'Harvard']
work = ['Microsoft', 'Tesla','Apple','Google','Facebook']
list_cvs = []

for i in range(len(names)):
    list_cvs.append({'name': names[i].split()[0], 'surname': names[i].split()[1], 'school': school[i], 'work': work[i]})


for j in range(len(list_cvs)):
    print('CV NUMBER: ' + str(j+1))
    print('Name: ' + list_cvs[j].get('name'))
    print('Surname: ' + list_cvs[j].get('surname'))
    print('School: ' + list_cvs[j].get('school'))
    print('Work: ' + list_cvs[j].get('work') + '\n')