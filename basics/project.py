#!/usr/bin/python3

from statistics import mean

ADMIN_CREDENTIALS = {"admin": "pass",
                     "administrator": "password"}

students = {'Jeremy': [8, 8],
            'Ann': [4, 8],
            'James': [7, 6]}

def AddStudent(student_name):
    students[student_name] = [];

def DeleteStudent(student_name):
    del students[student_name]

def EnterGrade(student_name, grade):
    students[student_name].append(grade)

def main():
    name = ""
    grade = 0
    print("Select operation:",
          "1. Enter grade",
          "2. Add student",
          "3. Delete student",
          "4. Print the list of students",
          "5. Calculate average grade for a student",
          "6. Exit", sep = "\n")
    ctrl = input("Type your choice: ")
    print("\n")
    if ctrl == "6":
        exit()
    if ctrl == "1":
        name = input("Student's name: ")
        grade = input("Enter grade: ")
        EnterGrade(name, int(grade))
    if ctrl == "2":
        name = input("Type student's name: ")
        AddStudent(name)
    if ctrl == "3":
        name = input("Type student's name: ")
        DeleteStudent(name)
    if ctrl =="4":
        print(students)
    if ctrl =="5":
        name = input("Type student's name: ")
        print(mean(students[name]))
    print("\n")

username = ""
password = ""
username = input("Input username: ")
password = input("Input password: ")
if username in ADMIN_CREDENTIALS and password == ADMIN_CREDENTIALS[username]:
    while True:
        main()
else:
    print("Wrong credentials!")
