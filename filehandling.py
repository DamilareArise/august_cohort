# MODE
'''
r => read only
w => write only
a => append
x => create

'''


# file = open('C:\\All_Python\\august_cohort\\getPercent.py', mode='r', encoding="utf-8")
# file = open(r"C:\Users\Hp\Documents\What is Backend Development.txt", mode='r', encoding="utf-8")
# print(file.read())
# file.close()
# print(file.read())

# file = open('note.txt', mode='a')
# file.write('\nHello Everyone (2)...')

# file = open('issy.docx', mode='x')


# with open(r"C:\Users\Hp\Documents\What is Backend Development.txt", mode='r', encoding="utf-8") as file:
#     print(file.read())

# print(file.read())


# classwork

info =[]
president_names = []
president_heights = []

with open(r'C:\All_Python\august_cohort\president_height.csv') as file:
    info = file.readlines()

info.pop(0)
# print(info)
for data in info:
    data = data.strip('\n')
    data = data.split(',')
    name = data[1]
    height = int(data[2])
    president_names.append(name)
    president_heights.append(height)


 
# print(president_names)
# print(president_heights)
def seperate():
    header = ''
    info = []
    with open(r'C:\All_Python\august_cohort\student_grades.csv') as file:
        info = file.readlines()
        header = info.pop(0)
        info.pop(0)


    with open('GradeA.csv', 'w') as file:
        file.write(header)

    with open('GradeB.csv', 'w') as file:
        file.write(header)

    with open('GradeC.csv', 'w') as file:
        file.write(header)


    for data in info:
        data = data.split(',')
        # print(data)

        score = int(data[1])

        if score >= 70 and score <= 100:
            data[2] = 'A'
            data = ','.join(data) 

            with open('GradeA.csv', 'a') as gradeA:
                gradeA.write(data + "\n")

        elif score >= 65 and score < 70:
            data[2] = 'B'
            data = ','.join(data) 

            with open('GradeB.csv', 'a') as gradeB:
                gradeB.write(data + "\n")



import csv 


with open('GradeA.csv') as file:
    
    # data = csv.reader(file)

    data = csv.DictReader(file)
    # print(data.fieldnames)
    # print(list(data.reader))

    # print(list(data))

    # for info in data:
    #     print(info)


# data = [
#     ['Name', 'Account Balance'],
#     ['Mercy Issy', 400000],
#     ['Holla Ope', 1000000],
#     ['Bims Abimbola', 2000000000]
# ]


# with open('details.csv', 'w', newline='') as files:
#     writer = csv.writer(files)
#     writer.writerows(data)


# data = [
#     {'Name': 'Mercy Issy', 'Account Balance': 400000},
#     {'Name': 'Holla Ope', 'Account Balance': 1000000},
#     {'Name': 'Bims Abimbola', 'Account Balance': 2000000000}
# ]

# with open('details.csv', 'w', newline='') as files:
#     writer = csv.DictWriter(files, fieldnames= data[0].keys())
#     writer.writeheader()
#     writer.writerows(data)



import os, shutil

# os.mkdir('newFolder')
# os.remove(r'newfolder\index.py')
# os.rmdir('newFolder')

# shutil.rmtree()
fileTocopy = r"C:\Datasets\housing\housing.csv"
destination = r"C:\All_Python\august_cohort"

# shutil.copy(fileTocopy, destination)
# shutil.copytree(fileTocopy, destination)
# shutil.move(fileTocopy, destination)

# print(os.path.exists(r"C:\All_Python\august_cohort"))
# os.system('python errorhandling.py')
# print(os.environ['USERNAME'])
# print(os.getcwd())

# os.chdir(r'C:\All_Python')
# print(os.getlogin())
# print(os.listdir(r'C:\All_Python\august_cohort'))

# print(os.path.join(destination, 'issy.docx'))

"""
tran_id     type    amount      datetime    sender      reciever    owner's_email

"""