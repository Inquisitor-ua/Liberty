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
        self.weight = weight
        self.height = height        
   
   # def tunning(self, plus):
    #    self.hp += (5 *plus)
        
    
    
 #class appearance(children):
     #def __init__(self, weight, height, model, color):
         #super().__init__(model, color)
         #self.weight = weight
         #self.height = height
    
    def drive(self):
        print("Аукцион открыт")    
   
   #def fly(self):
        #print("Полетели")

chynga = Appearance("black", "brown", '88', "185", "2010", 'black')
changa = Appearance("blonde", "green", '74', "179", "2008", 'white')

changa.drive()
print(chynga.hair)
print(chynga.color)
print(changa.hair)
print(changa.color)