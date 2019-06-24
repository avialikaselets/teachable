#!/usr/bin/python3


class Employee:

    def __init__(self):
        self.first_name = "N/A"
        self.last_name = "N/A"
        self. position = "N/A"
        self.uid = 0

    def __del__(self):
        print("Object", self, "is deleted!")

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_position(self):
        return self.position

    def get_uid(self):
        return self.uid

    def set_first_name(self, xFirstName):
        self.first_name = xFirstName

    def set_last_name(self, xLastName):
        self.last_name = xLastName

    def set_position(self, xPosition):
        self.position = xPosition

    def set_uid(self, xUID):
        self.uid = xUID


def main():
    employee_01 = Employee()
    print("\n\t***Welcome to the Employee Database***\n\n"
          "First name:", employee_01.get_first_name(), "\n"
          "Last name:", employee_01.get_last_name(), "\n"
          "Position:", employee_01.get_position(), "\n"
          "User ID:", employee_01.get_uid(), "\n")
    print(employee_01)
    employee_01.set_first_name("John")
    employee_01.set_last_name("Smith")
    employee_01.set_position("Manager")
    employee_01.set_uid(446)
    print("First name:", employee_01.get_first_name(), "\n"
          "Last name:", employee_01.get_last_name(), "\n"
          "Position:", employee_01.get_position(), "\n"
          "User ID:", employee_01.get_uid(), "\n")
    print(employee_01)

    # Deleting an instance of a class
    del(employee_01)
    # print(employee_01)


main()
