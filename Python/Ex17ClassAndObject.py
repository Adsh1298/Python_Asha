  # class Person:
  #     def __init__(self, name, address, Phone):
  #         self.nam
  # e = name
  # self.address = address
  # self.Phone = Phone
  # def display_details(self):
  # print(f"The name is {self.name} is from {self.address} and can be contacted by {self.Phone}")
  #
  # person=Person(name="asha",phone=9491508968,address="Bangalore")
  #                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               person.display_details()
  # print("The name of the Person is " :+person.name)
class Student:
    def __init__(self, name, dob):
        self.__name = name
        self.__dob = dob
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__dob
new_student = Student("asha","01/01/2001")
new_student2=Student("rohit","01/01/2001")
print(f"The name of {new_student.get_name()}) and his birth is {new_student.get_dob()}")


