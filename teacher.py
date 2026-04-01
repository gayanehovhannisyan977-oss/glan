class Teacher:
    def __init__(self, name, surname, gender, Id, birthay, subject, salary, number, email, experience):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.Id = Id
        self.birthay = birthay
        self.subject = subject
        self.salary = salary
        self.number = number
        self.email = email
        self.experience = experience
    def string(self):
        return (f"Name - {self.name}\nSurname - {self.surname}\nGender - {self.gender}\nID - {self.Id}\nBirthay date - {self.birthay}\nSubject - {self.subject}\nSalary - {self.salary}\nNumber")