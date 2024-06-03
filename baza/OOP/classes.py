class Vehicle():
    def __init__(self, model, color):
        self.color = color
        self.model = model
    
    def start(self):
        print(f"Двигатель {self.model} работает")

class Car(Vehicle):
    def __init__(self, horse_power, col, model, color):
        super().__init__(model, color)
        self.hp = horse_power
        self.col = col
                
    def tunning(self, plus):
        self.hp += (5 *plus)
        
    def drive(self):
        print("Поехали")
    
class Plane(Vehicle):
    def __init__(self, height, weapons, model, color):
        super().__init__(model, color)
        self.height = height
        self.weapons = weapons
        
    def fly(self):
        print("Полетели")

bmw = Car(250, 5, 'E39 M', 'black')
f16 = Plane(10000, True, 'F-16', 'Gray')

print(bmw.col)
print(bmw.color)
print(f16.weapons)
print(f16.color)

bmw.start()
f16.start()
bmw.drive()
f16.fly()