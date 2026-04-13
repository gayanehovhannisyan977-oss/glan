import pandas as pd

class Person:
    def __init__(self, name, surname, e_mail, number, ID, salary, address, experience, passport_num, subject):
        self.name=name
        self.surname=surname
        self.e_mail=e_mail
        self.number=number
        self.ID=ID
        self.salary=salary
        self.address=address
        self.experience=experience
        self.passport_num=passport_num
        self.subject=subject
    def info(self):
      pass
    def dict(self):
      pass
    def change_info(self):
      pass
    def delete_info(self):
      pass
    def add_info(self):
      pass




class Teacher(Person):
    def __init__(self, name, surname, e_mail, number, ID, salary, address, experience, passport_num, subject):
        super().__init__(name, surname, e_mail, number, ID, salary, address, experience, passport_num, subject)
    def info(self):
        return f"ID-{self.ID}\nName-{self.name}\nSurname-{self.surname}\nE-Mail{self.e_mail}\nPhone Number-{self.number}\nAddress-{self.address}\nPasport Num-{self.passport_num}\nSalary-{self.salary}\nExperience-{self.experience}\nSubject-{self.subject}\n"
    def add_info(self):
        df=pd.read_excel("teacher.xlsx")
        d1={
            "ID": self.ID,
            "Name": self.name,
            "Surnmae": self.surname,
            "E-Mail": self.e_mail,
            "Phone Number": self.number,
            "Address": self.address,
            "Passport Num": self.passport_num,
            "Salary": self.salary,
            "Experience": self.experience,
            "Subject": self.subject,
        }
        if self.ID in df["ID"].values:
            try:
                df = pd.concat([df, pd.DataFrame([d1])], ignore_index=True)
            except:
                print("This person has already excists")
    def change_info(self, column, new_value, index):
        try:
            df=pd.read_csv("teacher.xlsx")
            df.loc[index, column]=new_value
        except:
            print("No person was found with this ID")
    def delete_info(self, index):
        try:
            (df)=pd.read_csv("teacher.xlsx")
            df = df.drop(index)
        except:
            print("No person was found with this ID")





class Other(Person):

    def __init__(self, name, surname, e_mail, number, ID, salary, address, experience, passport_num, subject, position):
        super().__init__(name, surname, e_mail, number, ID, salary, address, experience, passport_num, subject)
        self.position=position
    def info(self):
        return f"ID-{self.ID}\nName-{self.name}\nSurname-{self.surname}\nE-Mail{self.e_mail}\nPhone Number-{self.number}\nAddress-{self.address}\nPasport Num-{self.passport_num}\nSalary-{self.salary}\nExperience-{self.experience}\nPostion-{self.position}\n"
    def add_info(self):
        df=pd.read_excel("other.xlsx")
        d2={
            "ID": self.ID,
            "Name": self.name,
            "Surnmae": self.surname,
            "E-Mail": self.e_mail,
            "Phone Number": self.number,
            "Address": self.address,
            "Passport Num": self.passport_num,
            "Salary": self.salary,
            "Experience": self.experience,
            "Position": self.position,
        }
        if self.ID in df["ID"].values:
            try:
                df = pd.concat([df, pd.DataFrame([d2])], ignore_index=True)
            except:
                print("This person has already excists")

    def change_info(self, column, new_value, index):
            try:
                df=pd.read_csv("other.xlsx")
                df.loc[index, column] =new_value
            except:
                print("No person was found with this ID")
    def delete_info(self, index):
        try:
            df=pd.read_csv("other.xlsx")
            df=df.drop(index)
        except:
            print("No person was found with this ID")
