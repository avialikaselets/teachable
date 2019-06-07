#!/usr/bin/python3

from statistics import *

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
    while True:
        print("Select operation:\n1. Enter grade\n2. Add student\n3. Delete student\n4. Print the list of students\n5. Calculate average grade for a student\n6. Exit")
        ctrl = input("Type your choice:")
        print("\n")
        if ctrl == "6":
            break
        if ctrl == "1":
            name = input("Student's name:")
            grade = input("Enter grade:")
            EnterGrade(name, int(grade))
        if ctrl == "2":
            name = input("Type student's name:")
            AddStudent(name)
        if ctrl == "3":
            name = input("Type student's name:")
            DeleteStudent(name)
        if ctrl =="4":
            print(students)
        if ctrl =="5":
            name = input("Type student's name:")
            print(mean(students[name]))
main()
