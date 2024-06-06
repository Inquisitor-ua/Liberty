class Vehicle():
    def __init__(self, model, color):
        self.color = color
        self.model = model
    

class Car(Vehicle):
    def __init__(self, horse_power, col, model, color):
        super().__init__(model, color)
        self.__hp = horse_power
        self.col = col
    
    def show_hp(self):
        print(f"Количество hp: {self.__hp}")
    
    def tunning(self, plus):
        self.__hp += (5 *plus)
        
    def start(self):
        print("Вы вставляете ключ в замок зажигания 😏")
        self.__electro()
        self.__fuel()
        self.__ready()
        
    def __electro(self):
        print("Электроприборы работают")
    
    def __fuel(self):
        print("Топливная система заработала")
    
    def __ready(self):
        print("Машина готова ехать")
        
    
    
class Plane(Vehicle):
    def __init__(self, height, weapons, model, color):
        super().__init__(model, color)
        self.height = height
        self.weapons = weapons
        
    def fly(self):
        print("Полетели")

bmw = Car(250, 5, 'E39 M', 'black')
f16 = Plane(10000, True, 'F-16', 'Gray')

bmw.start()
bmw.show_hp()