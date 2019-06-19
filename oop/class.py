#!/usr/bin/python3


class Employee:

    def __init__(self):
        self.first_name = "Bill"
        self.last_name = "Clinton"
        self.uid = 355

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_uid(self):
        return self.uid


def main():
    employee_01 = Employee()
    print("\n\t***Welcome to the Employee Database***\n\n"
          "First name:", employee_01.get_first_name(), "\n"
          "Last name:", employee_01.get_last_name(), "\n"
          "User ID:", employee_01.get_uid(), "\n")


main()
