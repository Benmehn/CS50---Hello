#Class is a template for a type of object

class Point():
    def __init__(self,inputx,inputy):
        self.x = inputx
        self.y = inputy

p = Point(2,8)

print(p.x)
print(p.y)