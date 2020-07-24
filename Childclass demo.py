from Loops import Calculator


class Childdemo(Calculator):
    num2 = 500

    def __init__(self):
        Calculator.__init__(self, 8, 10)

    def getCompletedata(self):
        return self.num2 + self.num + self.sum()


obj2 = Childdemo()
print(obj2.getCompletedata())
