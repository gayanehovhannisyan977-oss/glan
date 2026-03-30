class Sexan:
    def __init__(self, h, himq1, himq2, srunq):
        self.h = h
        self.himq1 = himq1
        self.himq2 = himq2
        self.srunq = srunq
    def paragic(self):
        return self.h+self.himq1+self.himq2+self.srunq
    def makeres(self):

        return (self.himq1+self.himq2)/2*self.h
