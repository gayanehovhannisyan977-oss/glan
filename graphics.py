import matplotlib.pyplot as plt

class Graphic:
    def __init__(self, x, y, version):
        self.x=x
        self.y=y
        self.version=version
    def versions(self):
        if self.version==1:
            return("Teacher.xlsx")
        if self.version==2:
            return("Student.xlsx")
        if self.version==3:
            return("Other.xlsx")
    def line(self):
        df=pd.read_excel(Graphic.versions())
        plt.plot(df[self.x], df[self.y])
        plt.show()
    def scatter(self):
        df=pd.read_excel(Graphic.versions())
        plt.scatter(df[self.x], df[self.y])
    def bar(self):
        df=pd.read_excel(Graphic.versions())
        plt.bar(df[self.x], df[self.y])
        plt.show()
    def pie(self):
        df=pd.read_excel(Graphic.versions())
        plt.pie(df[self.x], df[self.y])
        plt.show()