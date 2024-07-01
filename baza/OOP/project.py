# class User():
#     def __init__(self):
#         self.money = 
# class Animal():
    
# class Chiken(Animal):

# class Cow(Animal):

# class Pig(Animal):
    
class User():
    def __init__(self, name, animal):
        self.coin = 0
        self.name = name
        self.animal = animal
        self.up = 1
        self.lvl = 0
    def tap(self):
        self.coin += self.up
        return f"+ {self.up} coin"



def animal_choose():
    animals = {
        '1': "Бабочка",
        '2': "Осьминог",
        '3': 'Леопард',
        '4': 'Феникс'
    }
    animal = input("1. Бабочка\n2. Осьминог\n3. Леопард\n4. Феникс\n")
    if animal in animals:
        return animals[animal]
    else:
        print("Такого животного нет!")
        return animal_choose()

def main():
    name = input("Как тебя зовут?\n")
    animal = animal_choose()
    user = User(name, animal)
    while True:
        go = input("Что ты делаешь?\n 1. ")
        if go == "":
            user.tap()
        elif go == 

if __name__ == "__main__":
    main()