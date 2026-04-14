class Student:
    def __init__(self, name, surname, e_mail, number, ID, mark, classroom, address, parent_info):
        self.name = name
        self.surname = surname
        self.e_mail = e_mail
        self.number = number
        self.ID = ID
        self.mark = mark
        self.classroom = classroom
        self.address = address
        self.parent_info = parent_info
    def info(self):
        try:
            return f"ID-{self.ID}\nName-{self.name}\nSurname-{self.surname}\nE-Mail-{self.e_mail}\nPhone Number-{self.number}\nClass-{self.classroom}\nAddress-{self.address}\nParent Info-{self.parent_info}\nMark-{self.mark}\n"
        except Exception as e:
            return f"Error in info: {e}"
    def add_info(self):
        try:
            df = pd.read_excel("student.xlsx")
        except FileNotFoundError:
            df = pd.DataFrame()
        except Exception as e:
            print(f"Error reading file: {e}")
            return
        d = {
            "ID": self.ID,
            "Name": self.name,
            "Surname": self.surname,
            "E-Mail": self.e_mail,
            "Phone Number": self.number,
            "Class": self.classroom,
            "Address": self.address,
            "Parent Info": self.parent_info,
            "Mark": self.mark,
        }
        try:
            df = pd.concat([df, pd.DataFrame([d])], ignore_index=True)
            df.to_excel("student.xlsx", index=False)
            print("Added successfully")
        except Exception as e:
            print(f"Error while adding: {e}")
    def change_info(self, column, new_value, index):
        try:
            df = pd.read_excel("student.xlsx")
            df.loc[index, column] = new_value
            df.to_excel("student.xlsx", index=False)
            print("Changed successfully")
        except FileNotFoundError:
            print("File not found")
        except KeyError:
            print("Column does not exist")
        except Exception as e:
            print(f"Error while changing: {e}")
    def delete_info(self, index):
        try:
            df = pd.read_excel("student.xlsx")
            df = df.drop(index).reset_index(drop=True)
            df.to_excel("student.xlsx", index=False)
            print("Deleted successfully")
        except FileNotFoundError:
            print("File not found")
        except KeyError:
            print("Invalid index")
        except Exception as e:
            print(f"Error while deleting: {e}")
    def mean_mark(self):
        try:
            if isinstance(self.mark, list):
                return sum(self.mark) / len(self.mark)
            else:
                return float(self.mark)
        except TypeError:
            print("Mark should be numbers")
        except ZeroDivisionError:
            print("Mark list is empty")
        except Exception as e:
            print(f"Error in mean_mark: {e}")