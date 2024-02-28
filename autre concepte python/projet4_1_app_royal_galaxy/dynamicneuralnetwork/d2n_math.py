class Vect():
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y
        self.square_len=self.get_square_len() # (self.x)**2 + (self.y)**2
    
    def getx(self):
        return self.x
    def setx(self, x):
        self.x=x
    
    def gety(self):
        return self.y
    def sety(self, y):
        self.y=y
    
    def move(self, other):
        self.x+=other.getx()
        self.y+=other.gety()

    def get_square_len(self):
        return (self.x)**2 + (self.y)**2


a = Vect()
a.setx(3)
a.sety(4)
print(a.get_square_len())
print(f" {5//2}  {4//2}  {5//3}  {5/3}  {9//10}  {9/10} ")