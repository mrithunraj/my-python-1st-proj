class bike:
    def __init__(self,name):
        self.name=name
    def names(self):
        print("name is:",self.name)

class colour(bike):
    def __init__(self,name,black):
        self.black=black
        bike.__init__(self,name)
    def blacking(self):
        print("black is:",self.black)


class engine(colour):
    def __init__(self,name,black,bs):
        self.bs=bs
        colour.__init(self,name,black)
    def bsss(self):
        print("bs is:",self.bs)

        
e=engine("ns200","blue","nice")
e.names()
e.blacking()
e.bsss()
