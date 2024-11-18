# Python output command
# print(2 + 2)

# Type of commenting
# 1. Single line comment: #
# 2. Multi-line comment: """ """ or ''' '''
'''
Hello my people.
How are we doing?

'''

"""

"""

# print("Welcome to class")
# concatenation -> method of joining two or more strings together

# print("Welcome to class" + " Mercy" )
age = 20
# print('Age: ' + str(age))
# print(f"Age: {age}")

age = age + 1
# print('Age: ' + str(age))

# Python Variable
# Variable name
# assignment operator
# value

bottle = 'Water'
# print(bottle)
bottle = 'oil'
# print(bottle)

student = 'Daniel'
# print(student)
student = 'mercy'
# print("Welcome to class " + student)

# rules guiding variable declaration
# 1. variable name must start with a letter or underscore
# 2. variable name must be descriptive
# 3. variable must not contain a space character
# 4. avoid using any python keywords
    # camel casing
firstName = 'dd'
    # snake casing
the_first_student = 'dd'
    # Pascal casing
TheFirstStudent = 'dd'

# Types of variable declaration
# 1. single variable single value
# name = 'Dami'
# 2. single variable multiple value
students = 'Daniel' , 'Mercy', 'Ope', 'Aliya'
# print(students)
# 3. multiple variable single value
x = y = z = 20
# multiple variable multiple value 
*x, y = 20, 34, 78
# print(x)
# print(y)
# print('it\'s mine')



N = 20
# print(f"+{N}")

# a) 20
# b) Error
# c) +20
# d) 21


# Python DATA TYPES
# 1.) Number type:
    # i. Integers e.g 10, 30, 343  int()
    # ii. Float e.g 10.3, 34.55 float()
    # iii. Complex e. 3 + 4j complex()

num = 3

# print(type(num))
# print(float(num))

# 2.) text type
    # string str() e.g 'Dami'

# 3.) Boolean Type bool() e.g True, False
isMarried = False
# print(isMarried)

# print(str(isMarried))

# 4.) sequence type
    # i.) tuple  tuple() e.g ( 'Ope', 'Mercy', 34, True )
    # ii.) List list() e.g [ 'Ope', 'Mercy', 34, True ]
    # iii.) Range  range() e.g range(20)

myTuple =  ('Ope', 'Mercy', 34, True) #(['O' , 'p', 'e'], ...)
myList = [ 'Ope', 'Mercy', 34, True ]
# print(tuple(myList))
# print(len(myTuple))

# var = range(20)
# var = range(1, 21)
# var = range(1, 21, 2)

# print(list(var))

# 5. Mapping type 
    # i. dictionary dict() e.g {'name':'Dami', 'age': 20}

person1 =  {
    'name':'Dami', 
    'age': 20,
    'isMarried': True
    }
# print(person1['name'])

# person1 = 'dami'

# 6. set types
    # i. ) set set() e.g {'Ope', 'Mercy', 'Daniel', 'Aliya'}
    # ii.) frozen set

myset =  {'Ope', 'Mercy', 'Daniel', 'Aliya'}
num = {9,4,5,6,7,3,2,2,1}
# print(num)
# print(myset)
# print(frozenset(myset))

# 7. Binary types
    # i. byte 
name = bytes([68, 97, 109, 105])
# print(name)
    # 11. byte array

    # binary numbers
# print(type(bin(10)))

# name = 'Dami' # ['D', 'a' , 'm', 'i'] [68, 97, 109, 105]
# print(ord('i'))

# print(chr(90))'


# Python Operators
# 1. Arithmentic => +, -, *, /, %, //, **
# print(5//2)

# 2. assignment operator => =, += (increment), -=(decrement), *=, /=,//=, **=
num = 2
# num += 5 # num = num + 5
# print(num)

# 3. comparison operator => ==, !=, >, <, >=, <=

# conditional statement

# if num == 5:
#     print('num is 5')
# else:
#     print('num is not 5')


# name = input('Input your username: ')
# password = input('Input your password: ')
# confirm_password = input('Confirm password: ')


# print(name, password)

# password validation

# if(len(password) < 8 ):
#     print('Your password must be greater than 8 characters')

# else:
#     print('Strong password')

#         # nested if/else 
#     if(password == confirm_password):
#         print('passwords match. continue')
#     else:
#         print('password does not match')


# 4. Logical operator => and, or, not
#           AND 
# A     B       result
# 1     1       1
# 0     1       0
# 1     0       0
# 0     0       0


#           OR
# A     B       result
# 1     1       1
# 0     1       1
# 1     0       1
# 0     0       0

#       NOT
# A         NOT A
# 1         0
# 0         1


username = 'Dami'
password = '12345'

# print('Login')
# inp_user = input('Username: ')
# inp_pass = input('Password: ')
# if(inp_user == username and inp_pass == password):
#     print('Login successfull')
# else:
#     print('wrong username or password')

# isActive = True

# if(not isActive):
#     print('Access denied.. login')
# else:
#     print('Access granted')


# isMarried = True
# if(not isMarried):
#     print('You no try aswear')

# else:
#     print('You do well oo. na man you be')



# 5. Membership operator =>in,  not in

favourite_dishes = ['yam', 'rice', 'pounded yam']
# print('rice' not in favourite_dishes)

# 6. identity operator => is, is not

num = 4
num2 = 4

# print(num is not num2)


#  A simple calculator
# value1 = float(input('First value: '))
# value2 = float(input('Second value: '))

# print(
#     '''
#        Option;
    
#                 1.  Addition
#                 2.  Subtraction
#                 3.  Divison
#                 #.  Exit

#     '''
# )

# option = input('Option: ')
# if option == '1':
#     result = value1 + value2
#     print(f'Result: {result}')

# elif option == '2':
#     result = value1 - value2
#     print(f'Result: {result}')

# elif option == '3':
#     result = value1 / value2
#     print(f'Result: {result}')
# elif option == '#':
#     print('Goodbye...')
#     exit() 

# else:
#     print('Invalid option!')


# Python Strings
# Strings are sequences of characters. They can be enclosed in single quotes or double quotes.
student_name = 'Daniel' # ['D', 'a', 'n', 'i', 'e', 'l']
# print(len(student_name))
# print(student_name[-6])
# slicing
# print(student_name[:]) # ['D', 'a', 'n']

# print(type(student_name))

# print(student_name.lower())
# print(student_name.upper())

expression = 'Daniel is a python programmer and a student at SQI college of ICT'
# print(expression.capitalize())
# print(expression.title())

# print('1. What is the capital of Nigeria a). Lagos b.) Abuja')
# ans = input('Your answer: ')
# if ans.upper().strip() == 'B':
#     print('Correct')
# else:
#     print('wrong')

# strip() removes both leading and trailing whitespaces

# print(expression.strip('-/'))

# print(expression.count('Daniel'))

# print(expression.split(' a '))

item = ['+234', '9042823291']
# print(''.join(item))

# print(expression.startswith('daniel'))
# print(expression.replace('Daniel', 'Aliya'))

# Escape characters 


# Python collections/ array
# list, tuple, set, dictionary

# list - ordered, mutable or changeable, can be indexed, accept duplicate value
students = ['mercy', 'ope', 'daniel', 'aliya', 'mercy']
# print(students[-4:-1]) 
# print(students[::-1])

# students[0] , students[1] = 'Abimbola', 'Abimbola'
# students[:2] = ['Abimbola', 'Abimbola']

# print(students)

# students.reverse()
# students.append('Abimbola')
# students.extend(['Abimbola', 'John', 'Shola'])
# print(students)

arr = [
    ['Banana', 'Apple', 'Orange',[23, 45]],
    ['Rice', 'Beans'],
    'Water',
    34,
    True
]
# print(arr[0][3][1])

# students.remove('ope')
# students.pop(1)
# students.clear()
# students.insert(0, 'Abimbola')
# print(students)

# For loop

# for each_student in students:
#     print('Welcome,', each_student)
#     print('------------------------')


# for x in range(20):
#     print(x)


# info = []

# for x in range(5):
#     name = input(f'Name{x + 1}: ')
#     info.append(name)

# print(info)

# for each in info:
#     print(each, 'is a member.')


students = ['Ayo', 'Dele', 'Ade']
scores = [21, 23, 44]

sum_score = sum(scores)
length = len(scores)
avg_score = sum_score/length
# print('Average score is', avg_score)

# print(min(scores))
# print(max(scores))

# for student, score in zip(students, scores):
#     print(f'{student} scored {score}')

questions = [
    '1. what is the capital of nigeria a.) accra b.) lagos',
    '2. what is the capital of ghana a.) accra b.) lagos',
]

answers =  [
    'b',
    'a'
]

# for quest, ans in zip(questions, answers):
#     print(quest)
#     answer = input('Answer: ')
#     if answer.lower() == ans:
#         print("correct")
#     else:
#         print('wrong')


# tuple: immutable or unnchangeable, can be indexed, allows duplicate values, ordered
# tuple() or ()

fruits = ('Banana', 'Orange', 'Apple' , 'Orange')
# print(fruits[0:3])
# fruits[0] = 'watermelon'


# new = list(fruits)
# new[0] = 'watermelon'
# fruits = tuple(new)
# print(fruits)


# unpacking
# (first, second, *remaining) = fruits 

# *remianing, = fruits
# print(remianing)

# print(remaining)

# var = ['Favour']
# var2 = 'Favour',
# print(type(var))

# print(fruits.count('Orange'))
# print(fruits.index('Apple'))

# list of tuple 

ques_and_ans = [
    ( '1. what is the capital of nigeria a.) accra b.) lagos', 'b'),
    ( '2. what is the capital of ghana a.) accra b.) lagos', 'a')
]

# for quest, ans in ques_and_ans:
#     print(quest)
#     print(ans)



# Set : immutable/unchangeable, can't be indexed, not ordered, it doesn't accept duplicate value
# set() or {}

fruits = {'Banana', 'mango', 'apple', 'apple', 'agbalumo'}
# print(len(fruits))

# fruits.add('tomato')
# fruits.update(['tomato', 'watermelon'])
# fruits.remove('banana')
# fruits.discard('Banana')
# fruits.clear()
# print(fruits)

# {} => empty dict
# set() => empty set


setA = {1, 3, 6, 7, 3, 4, 2, 5, 9, 0, 8}
setB = {12, 13, 2, 1 , 11}
setC = { 3, 4}


# print(setA.union(setB))
# print(setA.intersection(setB))
# print(setB - setA)
# print(setA.difference(setB))
# print(setA.symmetric_difference(setB))

# setA.intersection_update(setB)
# setA.symmetric_difference_update(setB)
# print(setA)


# print(setA.issuperset(setC))
# print(setC.issubset(setA))
# print(setC.isdisjoint(setB))


# Dictionary: ordered, changeable, it doesn't allow duplicate 
# dict(key=value) or {key:value}

phone = {
    'model':'Iphone16',
    'color':'Black',
    'rom': '128gb',
    'version':'ios 18',
    'owner':{
        "name":'john doe',
        'address':'Lagos'
    }
}


# print(phone['owner']['name'])

# phone['model'] = 'Iphone18' # update
# phone['sold'] = True
# print(phone)

# print(type(phone.keys()))
# print(list(phone.keys())[0])
# for key in phone.keys():
#     print(key)

# print(phone.values())
# for val in phone.values():
#     print(val)

# print(phone.items())

# for key, value in phone.items():
#     print(f'{key} => {value}')


# ques_and_ans = {
#     '1. what is the capital of nigeria a.) accra b.) lagos':'b',
#     '2. what is the capital of ghana a.) accra b.) lagos':'a'
# }

# for ques, ans in ques_and_ans.items():
#     print(ques)
#     user = input('answer ').strip()
#     if user.lower() == ans:
#         print('Correct')
#     else:
#         print('Wrong')


# print(phone['models'])
# print(phone.get('models'))

# phone.update({'sold':True})
# phone.pop('owner')
# print('its working')

# print(phone)



# user_db = []
# user = int(input('No of users: '))
# for x in range(user):
#     name = input(f'Name {x+1}: ')
#     user_db.append(name)

# print(user_db)


{
    1:('ade', 23),
    2:('wumi', 24)
}


# user_db = {}
# user = int(input('No of users: '))
# for x in range(user):
#     name = input(f'Name {x+1}: ')
#     age  = int(input('Age: '))
#     user_db.update({x+1:(name, age)})

# print(user_db)

# to extract the age of the second user

# print(user_db[2][1])


[
    {
        'firstName':'Ola',
        'lastName':'Ojo',
        'email':'olaojo@gmail.com',
        'password':'1234'
    },

] 

# user_db  = []
# user = int(input('No of users: '))
# for x in range(user):
#     user = {
#         'firstname': input('Firstname: '),
#         'lastname': input('Lastname: '),
#         'email': input('Email: '),
#         'password': input('Password: ')
#     }

#     user_db.append(user)

# print(user_db)



# x= 10
# while x>1:
#     print('Yo', x) 
#     x -= 1

# students = []
# user = input('insert student name, press 1 to stop or enter to continue: ')
# while user != '1':
#     user = input('Insert Name or 1 to stop: ')
#     students.append(user)

 
# print(students)


# x = 10

# while x > 1:
#     print('Yo', x)
#     x -= 1

# x = 0
# while x < 10:
#     print('Yo', x)
#     x += 1

# users = []
# slot = 5
# while slot > 0:
#     user = input('Name: ')
#     users.append(user)
#     slot -= 1
# else:
#     print('No more slot')


# ticket = 10


# while ticket > 0:
#     print(f"Tickets remaining: {ticket}")
#     age = int(input('Age: '))
#     if age < 18:
#         print('Sorry, you are not eligible for a ticket')
#         # continue
#         # break
#     else:
#         ticket -= 1
# else:
#     print('No more tickets available')


# users = []
# while True:
#     user = {
#         'firstname': input('Firstname: '),
#         'lastname': input('Lastname: '),
#         'email': input('Email: '),
#         'password': input('Password: ')
#     }
#     users.append(user)
#     option = input('press 1 to stop or enter to continue: ')
#     if option == '1':
#         break
#     else:
#         continue
        

# print(users)


# Building a TODO App 
# 1. collecting users todo
# ['eat', 'sleep'] 
# {
#     'user':'Ope',
#     'todo': 'eat',
    # 'done': False,
#     'created_at': '2022-01-01',
# }

# 2. display todo
# 3. mark todo as done
# 4. edit a todo
# 5. delete a todo



# parametized function and unparametized function

# def call_my_name():
#     print('My name is Damilare')

# call_my_name()


# def call_my_name(name):
#     print(f'My name is {name}')

# call_my_name('Dami')


# defualt parameter
# def call_my_name(name='Damilare'):
#     print(f'My name is {name}')

# call_my_name('Mercy')

def addition(value3, value2=10, value1=10):
    print(f'Answer = {value1 + value2}')

# addition(value1=23, value2= 33, value3=20)
# addition(20)

# return function 

def get_percent(score:float|int, total_score:int|float = 100) -> float|int:
    '''
    It returns the score in percentage\n
    parameter score is required\n
    parameter total score has a defualt of 100

    '''
    score_in_percent = (score/total_score) * 100
    return score_in_percent

def check_grade():
    score = float(input('Score: '))
    total_score = int(input('Total score'))
    score_in_percent = get_percent(score, total_score)
    print(f'{score_in_percent}%')
    if score_in_percent > 70:
        print(f'Grade: A\nscore:{score_in_percent}%')
    elif score_in_percent > 64 and score_in_percent < 70:
        print('Grade: B')

# check_grade()


# types of variables => global and local variable

val1 = 10
val2 = 10

def add():
    global val2
    val2 = 20
    print(val1 + val2)


def sub():
    print(val2)

# add()
# sub()   


account_balance = 100

def dashboard():
    print('''
    1. withdraw
    2. deposit
    3. check balance
    4. exit
    ''')

    option = input('option: ')
    if option == '1':
        withdraw()
    elif option == '2':
        pass
    elif option == '3':
        check_balance()
    elif option == '4':
        exit()
    else:
        print('Invalid option, try again!')
        dashboard() #recursive function


def withdraw():
    global account_balance

    amount = float(input('Amount: '))
    if amount > account_balance:
        print('Insufficient fund')

    else:
        
        account_balance -= amount
        print(f'Youve successfully withdraw #{amount}, account balance is #{account_balance}')

    option = input('Press 1 to go back to dashboard or enter to retry: ')
    if option == '1':
        dashboard()
    else: 
        withdraw()  


def check_balance():
    print(f'Your account balance is {account_balance}')



# dashboard()



all_todo = []

def dashboard():
    print(
    '''
    Welcome to myTodo App

    1. Create a todo
    2. Edit a todo
    3. delete a todo
    4. view todo
    #. exit
    
    '''
    )
    option = input('Option: ')
    if option == '1':
        createTodo()


def createTodo():
    while True:
        todo = input('Todo: ')
        all_todo.append(todo)
        option = input('press 1 to stop or enter to continue adding todo: ')
        if option == '1':
            dashboard()
        else:
            continue



# user = 2 
# all_todo[user - 1] = 'code'

# all_todo.pop(user-1)
# # dashboard()

# allTodo = ['eat', 'sleep', 'Bath']
# x=1
# for todo in allTodo:
#     print(f'{x}. {todo}')
#     x+=1


# print('Yes'if x==1 else 'no')

# OOP -> object oriented programming



class PhoneTemplate:
    # state the properties and function
    def __init__(self):

        self.model = 'Iphone XR'
        self.color = 'Blue'
        self.state = True

    def home(self):
        if self.state:

            user = input('''
                1. make a call
                2. switch on/off
            ''')
            if user == '1':
                self.make_a_call()
            elif user == '2':
                self.switch_off_or_on()
            else:
                print('Error')
                self.home()

        else:
            user = input('The phone is off. press 1 to switch on: ')
            while user != '1':
                user = input('The phone is off. press 1 to switch on: ')
            else:
                self.switch_off_or_on()

    def make_a_call(self):
        print(f'The {self.model} can make calls')

    def switch_off_or_on(self):
        if self.state:
            print('switching off...')
            self.state = False
        else:
            print('switching on...')
            self.state = True
        self.home()

phone1 = PhoneTemplate()
phone2 = PhoneTemplate()

phone1.model = 'Iphone 15'
# print(phone1.model)
# print(phone2.model)

# phone1.home()

# print(type(phone2))


class Calculator:
    def __init__(self):
        self.name = 'Casio'

    def calculate(self):
        self.value1 = float(input('Value1: '))
        self.value2 = float(input('Value2: '))
        option = input(
            """
                1. addition
                2. subtraction
                3. exit
            """
        )

        if option == '1':
            self.addition()

    def addition(self):
        print(f'Answer: {self.value1 + self.value2}')
        user = input('press 1 to exit or enter to continue')
        if user == '1':
            exit()
        else:
            self.calculate()

    def subtraction(self):
        print(f'Answer: {self.value1 - self.value2}')
        user = input('press 1 to exit or enter to continue')
        if user == '1':
            exit()
        else:
            self.calculate()


# mycalc = Calculator()
# mycalc.calculate()



# Parametized function

class Calculator:
    def __init__(self):
        self.name = 'Casio'

    def calculate(self, value1:float, value2:float):
        self.value1 = value1
        self.value2 = value2
        option = input(
            """
                1. addition
                2. subtraction
                3. exit
            """
        )

        if option == '1':
            self.addition()

    def addition(self):
        print(f'Answer: {self.value1 + self.value2}')
        user = input('press 1 to exit or enter to continue')
        if user == '1':
            exit()
        else:
            self.calculate()

    def subtraction(self):
        print(f'Answer: {self.value1 - self.value2}')
        user = input('press 1 to exit or enter to continue')
        if user == '1':
            exit()
        else:
            self.calculate()


# mycalc = Calculator()

# val1 = float(input('value 1: '))
# val2 = float(input('value 2: '))
# mycalc.calculate(val1, val2)


# parametized class

class Human:
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        print(f'My name is {self.name}')


# name = input('Name: ')
# Ayo = Human(name)
# Ayo.introduce()

class Human:
    def __init__(self):
        self.name = input('Name: ')

    def introduce(self):
        print(f'My name is {self.name}')


# name = input('Name: ')
# Ayo = Human()
# Ayo.introduce()


# Inheritance

class Parent:
    def __init__(self) -> None:
        self.surname = 'Tinubu'
        self.firstname = 'Ahmed'
        self.hobby = 'playing golf'

    def introduce(self):
        return f'My name is {self.firstname} {self.surname}. I love {self.hobby}'


# Father = Parent()
# Father.introduce()

class Child(Parent):
    def __init__(self) -> None:
        super().__init__()
        self.firstname = 'Seyi'
        self.occupation = 'politician'

    def introduce(self):
        # print(f'Helloo everyone, My name is {self.firstname} {self.surname}, I am a {self.occupation}')
        # return super().introduce()

        info = super().introduce()
        print(f'{info}. I am also {self.occupation}')
     

    def run(self):
        print(f'{self.firstname} can run very fast')
        # info = super().introduce()

# child1 = Child()
# child1.introduce()
# child1.run()



class User:
    def __init__(self, lastname, firstname, email, password) -> None:
        self.lastname = lastname
        self.firstname = firstname
        self.email = email
        self.password = password

    def info(self):
        return (f'Name: {self.firstname} {self.lastname}\nEmail: {self.email}')



class Staff(User):
    def __init__(self, lastname, firstname, email, password, staff_id, account_no) -> None:
        super().__init__(lastname, firstname, email, password)
        self.staff_id = staff_id
        self.account_no = account_no

    
    def info(self):
        detail = super().info()
        print(f'Staff ID: {self.staff_id}\n{detail}\nAccount no: {self.account_no}')


# Ade = Staff('OLatunji', 'Adetunji', 'olaade@gmail.com', '1234', '002', '123456789')
# Ade.info()

# register student
# take test 
# view result


quest_ans = {
    '1. What is the capital of Nigeria a. Tokyo b. Abuja c. Accra':'b',
    '2. What is the capital of Japan a. Tokyo b. Abuja c. Accra': 'a',
    '3. What is the capital of Ghana a. Tokyo b. Abuja c. Accra': 'c'
}

student_db = []

def registerStudent():
    global student_db

    while True:
        info = {
            'fullname':input('Fullname: '),
            'score':0
            }
        student_db.append(info)
        user = input('Press 1 to stop or enter to continue ')
        if user == '1':
            break
        else:
            continue

    print('Registration successfull...')
    print(student_db)
    dashboard()


def dashboard():
    print('''
    Welcome to myCBT APP

    1. Register Student
    2. View Result 
    3. Take Test
    #. Exit

    ''')
    option = input('Option: ')
    if option == '1':
        registerStudent()
    elif option == '2':
        resultStatistic()
    elif option == '3':
        takeTest()
    elif option == '#':
        exit()
    else:
        print('error')
        dashboard()

def resultStatistic():
    # [
    #     {'fullname': 'Ola', 'score':20},
    #     {'fullname': 'Ope', 'score':25}
    # ]

    scores = []

    if not student_db:
        print('No student found kindly register students...')
        registerStudent()
    
    print('Student Result...')
    for student in student_db:
        print(f"fullname: {student['fullname']}\nScore: {student['score']}\n")
        scores.append(student['score'])

    max_score = max(scores)
    index_maxScore = scores.index(max_score) # 1
    max_student =  student_db[index_maxScore] # {'fullname': 'Ope', 'score':25}
    print(f"{max_student['fullname']} got the highest score ")

    min_score = min(scores)
    index_minScore = scores.index(min_score) # 1
    min_student =  student_db[index_minScore] # {'fullname': 'Ope', 'score':25}
    print(f"{min_student['fullname']} got the lowest score ")

    print(f"The avarage score is {sum(scores)/len(scores)}")



def takeTest():
    global student_db
    if quest_ans:
        print('Questions are available')

        if student_db:
            print('Time to take the test...')
            for student in student_db:
                print(f"{student['fullname']} its time for your test...")
                for ques, ans in quest_ans.items():
                    print(ques)
                    user_ans = input('Answer: ')
                    if user_ans.strip().lower() == ans:
                        print('correct')
                        student['score'] += 5
                    else:
                        print('wrong')

                print(f"Test completed. Score = {student['score']}")

            print(student_db)
            dashboard()

        else:
            print('No student found kindly register students...')
            registerStudent()
    
    else:
        print('No question avaliable..')
        dashboard()


# dashboard()



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
            print(f"fullname: {student['fullname']}\nScore: {student['score']}\n")
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


# test1.quest_ans.update({'4. What is the capital of Turkey a. Ankara b. Lace c. Buba': 'a'})
# test1.quest_ans = {'4. What is the capital of Turkey a. Ankara b. Lace c. Buba': 'a'}
# print(test1.quest_ans)

# test1.dashboard()



# test2 = Exam()
# print(test2.quest_ans)


# 1. python Scripts - This just a python(.py) file with bunch of python syntax
# 2. python module - This is pyhton file that contains exportable functions, variables or class
# 3. python library - This is a folder that contains one or more python modules

# import datetime as dt
# from datetime import date
# import time
# import calendar
# from colorama import just_fix_windows_console
# just_fix_windows_console()
# from colorama import init, Fore, Back, Style
# init()
# import pandas, numpy
import random


# mydate = date.today()
# print('Loading...')
# time.sleep(2)
# print(mydate)

# year = calendar.calendar(2024)
# print(Fore.GREEN + Style.DIM +  calendar.month(2024,10))

# val = random.randint(2100000000, 2199999999)
# val = random.randint(2348100000000, 2348199999999)
# print(f'+{val}')

Fruits = ['Orange', 'Pineapple', 'Cherry', 'Mango', 'Watermelon']
# print(random.sample(Fruits, 3))
# print(random.choice(Fruits))
# random.shuffle(Fruits)
# print(Fruits)

# numbers = list(range(0, 100))
# print(random.sample(numbers, 10))


# SQL 1
'''
DBMS -> Database management system
Two basic types of DBMS
1. Relational DBMS (RDBMS) 
- SQL(Structured Query Language)
Tables (row and columns)
e.g 
mySchool Database
- student table
- teachingStaff table
- nonTeachingStaff table
- expenditure table
- revenue table

# Application
- mySQL, postgreSQL, Oracle, MicrosoftSQL, SQLlite e.t.c



2. Non-relational DBMS (NoSQL)
- Cluster - Group of Databases
- Database - e.g mySchool Database
- Collection - Group of Document
    e.g studentCollection
    [
        {
            studentName: Ope,
            age: 30
        },

        {
            studentName: Ayo,
            age: 30
        }

    
    ]

- Document - The Information Itself
    
    e.g {
            studentName: Ope,
            age: 30
        }

# Application
- MongoDB, Cassandra, Redis, Couchbase e.t.c

types of relationship
one to one relationship e.g relation between user_table and profile_table
    user table                                          profile table
user_id      email       password                    profile_id          phone       fullname        NIN      user_id   
1       ope@gmail   123456                      1                   0801234567          ayo         23234          2
2       ayo@gmail   123456                      2                   0801234567          ope         87645          1

one to many relationship e.g relation between user_table and transaction_table

user table                                                  transaction table

user_id      fullname            |         transaction_id          amount          type        user_id
1            Ope                 |          1                        1000          credit       1
                                            2                        2000          debit        1

'''