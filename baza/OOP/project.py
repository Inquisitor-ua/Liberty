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
        self.coins_to_up = 10
    def tap(self):
        self.coin = round(self.coin + self.up, 2)
        return f"+ {self.up} coin"
    def lvl_up(self):
        self.coin = round(self.coin - self.coins_to_up, 2)
        self.lvl += 1
        self.coins_to_up = round(self.coins_to_up * 1.7, 2)
        self.up = round(self.up * 1.5, 2)
    def enough(self):
        if self.coin >= self.coins_to_up:
            return True
        else:
            return False



def animal_choose():
    animals = {
        '1': "Бабочка",
        '2': "Осьминог",
        '3': 'Леопард',
        '4': 'Феникс'
    }
    animal = input("Выбери животного:\n1. Бабочка\n2. Осьминог\n3. Леопард\n4. Феникс\n")
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
        go = input("Что ты делаешь?\n 1. upgrade \n 2. показать статистику\n")
        if go == "":
            result = user.tap()
            print(result)
        elif go == "1":
            if user.enough(): 
                user.lvl_up()
                print("круто", user.lvl)
        elif go == "2":
            print(f"name: {user.name}\nanimal: {user.animal}\ncoin: {user.coin}\nup: {user.up}\nlvl: {user.lvl}\ncoins_to_up: {user.coins_to_up}")


if __name__ == "__main__":
    main()