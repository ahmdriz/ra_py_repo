# PYTHON TASKS
# --------------------------------------------------------------------------- #

# A. Python is an indent based programming language
# --------------------------------------------------------------------------- #
'''
The following program throws an indentation error. Correct it and make sure it prints properly.

teams = ['Data', 'AI', 'DevOps']
for t in teams:
print('Hello', t, 'Team from Inceptez Technologies')
  print('Keep Learning and Exploring!')
'''

teams = ['Data', 'AI', 'DevOps']
for t in teams:
    print('Hello', t, 'Team from Inceptez Technologies')
print('Keep Learning and Exploring!')

# B. Commented line in Python
# --------------------------------------------------------------------------- #
# Use Case 1:
'''
Add single-line and multi-line comments to describe what the below code does for Inceptez Technologies’ training tracker.

students = 100
trainers = 2
total = students + trainers
print(total)
'''

'''
The code below calculates and prints the total number of students and trainers
for Inceptez Technologies’ training tracker.
'''
print('')
students = 100  # stores no. of students
trainers = 2  # stores no. of trainers
total = students + trainers  # calculates total no. of students and trainers
print(total)  # displays the total count

# Use Case 2:
'''
Convert the below block into a “dead code” using comments, then re-activate it later to print

print("Welcome to Inceptez Python Learning")
'''
print('')
# Dead Code
# print("Welcome to Inceptez Python Learning")

# Re-activated code
print("Welcome to Inceptez Python Learning")

# C. Playing with Quotes
# --------------------------------------------------------------------------- #
# Use Case 1:
'''
Create three string variables that correctly store and print:

This is Inceptez's "Python" class for Data Engineers & AI Engineers
→ Use single, double, and triple quotes appropriately.
'''
print('')
str1 = 'This is Inceptez\'s "Python" class for Data Engineers & AI Engineers'
str2 = "This is Inceptez's \"Python\" class for Data Engineers & AI Engineers"
str3 = '''This is Inceptez's "Python" class for Data Engineers & AI Engineers'''
print(str1)
print(str2)
print(str3)

# Use Case 2:
'''
Write a multiline string using triple quotes that prints:

Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey.
'''
print('')
print('''Welcome to Inceptez Technologies!
Python Training: Basics
Enjoy your learning journey.''')

# D. Let's learn all about VARIABLES
# --------------------------------------------------------------------------- #
# Use Case 1:
'''
Declare variables to store the following details:
- Student Name
- Course Name (e.g., “Python Fundamentals”)
- Training Institute Name (Inceptez Technologies)

Then print a formatted message:

Name: Arun is learning the course Python Fundamentals at the institute Inceptez Technologies
'''
print('')
studentName = 'Arun'
courseName = "Python Fundamentals"
trainingInstituteName = "Inceptez Technologies"
print('Name:', studentName, 'is learning the course', courseName, 'at the institute', trainingInstituteName)
print(f"Name: {studentName} is learning the course {courseName} at the institute {trainingInstituteName}")

# Use Case 2:
'''
Demonstrate dynamic inference, 
dynamic typing using with fee by applying .18 gst 
and prove strongly typing character also by operating it with Eighteen percent gst

fee = 45000
'''
print('')
fee = 45000  # Dynamic inference. The variable data type(int) is identified based on the value assigned to it
print(fee)
print(type(fee))
fee = fee + (0.18 * fee)  # Dynamic inference data type(float)
print(fee)
print(type(fee))
# totalFee = 45000 + '18% GST' #this line will throw error as python is strongly typed and will not implicitly cast incompatible data types

# E. Variables Naming Conventions
# --------------------------------------------------------------------------- #
# Use Case 1:
'''
Identify which variable names below are invalid for Inceptez’s student database:

1) 2student = 'Ravi'
2) _student_id = 1001
3) studentName = 'Priya'
4) class name = 'Python'
5) inceptez_batch = 'Morning'
'''

# 2student = 'Ravi' #Invalid. Variable name cannot start with a number
_student_id = 1001  # valid
studentName = 'Priya'  # valid
# class name = 'Python' #invalid. Variable name cannot have spaces in between
inceptez_batch = 'Morning'  # valid

# Use Case 2:
'''
Declare 3 variables following naming styles for Inceptez projects:

# PascalCase: DataEngineeringBatch
# camelCase: dataEngineeringBatch
# snake_case: data_engineering_batch
'''
PascalCase = 'DataEngineeringBatch'
camelCase = 'dataEngineeringBatch'
snake_case = 'data_engineering_batch'

# F. Type identification & Casting
# --------------------------------------------------------------------------- #
# Use Case 1:
'''
Write a program that asks for an employee’s age.
1. Checks its type is of string (think about using isinstance() function)
2. Converts it to int (continue writing your program from here..)
3. Prints the years pending for retirement, for eg. 60 is the retirement age.
'''

empAge = input("Enter Employee's Age: ")
if isinstance(empAge,str) = True
convEmpAge = int(empAge)
print(f'{60-convEmpAge} is the retirement age at Inceptez)

