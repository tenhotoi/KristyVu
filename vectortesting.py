# https://media.licdn.com/dms/document/C4D1FAQHn35se6Dh27g/feedshare-document-pdf-analyzed/0/1678202572070?e=1678924800&v=beta&t=NnRhDmZ5oYXxTCLhY2FgpmrshuNktOtRYiA4AhzyqJU

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        newx = self.x + other.x
        newy = self.y + other.y
        return Vector(newx, newy)

    def __str__(self):
        return "(%f, %f)" %(self.x, self.y)

u = Vector(3,4)
print(u.norm())
print(Vector(5,12).norm())

u = Vector(3,4)
v = Vector(3,6)
print(u + v)    

