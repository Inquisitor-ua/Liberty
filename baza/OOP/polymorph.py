class Square():
    def __init__(self, a):
        self.a = a
    def s(self):
        return self.a**2
        
class Rectangle():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def s(self):
        return self.a * self.b
        
class Circle():
    def __init__(self, r):
        self.r = r
        
    def s(self):
        return 3.14 * (self.r**2)
    
def main():
    sq1 = Square(5)
    sq2 = Square(7)
    rec1 = Rectangle(4, 9)
    rec2 = Rectangle(3, 6)
    cir1 = Circle(2)
    cir2 = Circle(8)
    figures = [sq1, sq2, rec1, rec2, cir1, cir2]
    for figure in figures:
        print(figure.s())

if __name__ == "__main__":
    main()