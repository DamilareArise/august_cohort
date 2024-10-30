# import getPercent as gp
from getPercent import get_percent


class Exam:
    def __init__(self) -> None:
        self.quest_ans = {
            '1. What is the capital of Nigeria a. Tokyo b. Abuja c. Accra':'b',
            '2. What is the capital of Japan a. Tokyo b. Abuja c. Accra': 'a',
            '3. What is the capital of Ghana a. Tokyo b. Abuja c. Accra': 'c'
            }

        self.student_db = []

    def dashboard(self):
        print('''
        Welcome to myCBT APP

        1. Register Student
        2. View Result 
        3. Take Test
        #. Exit

        ''')
        option = input('Option: ')
        if option == '1':
            self.registerStudent()
        elif option == '2':
            self.resultStatistic()
        elif option == '3':
            self.takeTest()
        elif option == '#':
            exit()
        else:
            print('error')
            self.dashboard()

    def registerStudent(self):
    

        while True:
            info = {
                'fullname':input('Fullname: '),
                'score':0
                }
            self.student_db.append(info)
            user = input('Press 1 to stop or enter to continue ')
            if user == '1':
                break
            else:
                continue

        print('Resgistration successfull...')
        print(self.student_db)
        self.dashboard()

    
    def takeTest(self):
    
        if self.quest_ans:
            print('Questions are available')

            if self.student_db:
                print('Time to take the test...')
                for student in self.student_db:
                    print(f"{student['fullname']} its time for your test...")
                    for ques, ans in self.quest_ans.items():
                        print(ques)
                        user_ans = input('Answer: ')
                        if user_ans.strip().lower() == ans:
                            print('correct')
                            student['score'] += 5
                        else:
                            print('wrong')

                    print(f"Test completed. Score = {student['score']}")

                print(self.student_db)
                self.dashboard()

            else:
                print('No student found kindly register students...')
                self.registerStudent()

    def resultStatistic(self):
        scores = []

        if not self.student_db:
            print('No student found kindly register students...')
            self.registerStudent()
        
        print('Student Result...')
        for student in self.student_db:
            print(f"fullname: {student['fullname']}\nScore: {get_percent(student['score'], 15)}%\n")
            scores.append(student['score'])

        max_score = max(scores)
        index_maxScore = scores.index(max_score) # 1
        max_student =  self.student_db[index_maxScore] # {'fullname': 'Ope', 'score':25}
        print(f"{max_student['fullname']} got the highest score ")

        min_score = min(scores)
        index_minScore = scores.index(min_score) # 1
        min_student =  self.student_db[index_minScore] # {'fullname': 'Ope', 'score':25}
        print(f"{min_student['fullname']} got the lowest score ")

        print(f"The avarage score is {sum(scores)/len(scores)}")

        self.dashboard()


test1 = Exam()
test1.dashboard()