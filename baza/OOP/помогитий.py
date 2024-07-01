class Children():
    def __init__(self, model, color):
        self.color = color
        self.model = model
    
    def start(self):
        print(f"Год рождения: {self.model}")

class Appearance(Children):
    def __init__(self, hair, eyes, weight, height, model, color):
        super().__init__(model, color)
        self.hair = hair
        self.eyes = eyes
        self.__weight = weight
        self.height = height        
   
    def start(self):
        print("Завести ребенка из Китая😏")
        self.__electro()
        self.__fuel()
        self.__drive()
        
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, new):
        if new <= 0:
            print("отрицательный вес быть не может!")
        else:
            self.__weight = new 

    def __electro(self):
        print("Ребенок в пути")
    
    def __fuel(self):
        print("Ребенок прибыл")
    
    def __drive(self):
        print("Аукцион открыт")    

chynga = Appearance("black", "brown", 88, 185, 2010, 'black')
changa = Appearance("blonde", "green", 74, 155, 2008, 'white')

changa.start()
print(chynga.hair)
print(chynga.color)
print(changa.hair)
print(changa.weight)
changa.weight = 100
print(changa.weight)