class Car():
    def __init__(self, horse_power, color):
        self.hp = horse_power
        self.color = color
        
    def tunning(self, plus):
        self.hp += (5 *plus)

bmw = Car(250, 'black')
audi = Car(230, 'blue')

print(bmw.hp)
plus = int(input("Введите число: "))
bmw.tunning(plus)
print(bmw.hp)
print(audi.hp)
