import Pandas as pd

class Person:
    def __init__(self, name, surname, gender, Id, birthay, salary, number, email, experience):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.Id = Id
        self.birthay = birthay
        self.salary = salary
        self.number = number
        self.email = email
        self.experience = experience
    def __str__(self):
        return (f"Name - {self.name}\nSurname - {self.surname}\nGender - {self.gender}\nID - {self.Id}\nBirthay date - {self.birthay}\nSalary - {self.salary}\nNumber -{self.number}\nEmail - {self.email}\nExperience - {self.experience}")
    def tvyalneri_pahpanum(self):
        d={
            "Name":self.name,
            "Surname":self.surname,
            "Gender":self.gender,
            "Id":self.Id,
            "Birthay":self.birthay,
            "Salary":self.salary,
            "Number":self.number,
            "Email":self.email,
            "Experience":self.experience
        }




class Teacher:




class Other:
