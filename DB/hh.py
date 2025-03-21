import sqlite3
# def number_chech():
#     total = input("Капуста есть: ")
#     if total.isnumeric():
#         return int(total)
#     else:
#         print("Енто не число!")
#         return number_chech() #Рекурсия

def number_check(total):
    if total.isnumeric():
        return True
    else:
        return False
    
def check_name(name):
    db = sqlite3.connect("DB/data.db")
    c = db.cursor()
    names = c.execute("SELECT name FROM users WHERE name = ?", (name,)).fetchall()
    if len(names) > 0:
        return False
    else:
        return True
    
def register():
    while True:
        global name
        name = input("Напишите имя пж по-брацки: ")
        if check_name(name):
            break
        else:
            print("Это имя занято!")
    
    password = input("Пароль суки: ")
    email = input("Мыло еще: ")

    # total = number_chech()

    total = type_number('Капуста есть: ')

    db = sqlite3.connect("DB/data.db")
    c = db.cursor() 
    c.execute("INSERT INTO users (name, password, email, total) VALUES (?,?,?,?)",(name, password, email, total))
    db.commit()
    db.close()

def upgreat(summa, tr, db, c):
    total = check_balance()
    if tr == 0:
        total -= summa
    elif tr == 1:
        total += summa
    c.execute("UPDATE users SET total = ? WHERE name = ?",(total, name))
    db.commit()

def check_balance():
    db = sqlite3.connect("DB/data.db")
    c = db.cursor()
    total = c.execute("SELECT total FROM users WHERE name = ?", (name,)).fetchone()[0]
    db.close()
    return total

def type_number(text):
    while True:
        number = input(text)
        if number_check(number):
            number = int(number)
            return number
        else:
            print("loh")

def ins_trans(trans_type, tr):
    db = sqlite3.connect("DB/data.db")
    c = db.cursor()
    trans_name = input("Введите название транзакции: ")

    summa = type_number(f"Сколько денег вы {trans_type}")

    id = c.execute("SELECT id FROM users WHERE name = ?", (name,)).fetchone()[0]
    c.execute("INSERT INTO money (vuplatu, cyma, trans_type, user_id) VALUES (?,?,?,?)", (trans_name, summa, tr, id))
    upgreat(summa, tr, db, c)
    db.commit()

def plus():
    ans = input("1. Вывести деньги\n2. пополнить баланс\n")
    if ans == "1":
        return ins_trans('хотите снять: ', 0)
    elif ans == "2":
        return ins_trans('хотите закинуть на счет: ', 1)
    else:
        print("ne ponyal")
        return plus()
    
def change():
    ans = input("1. Изменить имя\n2. Изменить пароль\n")
    if ans == '1':
        return update('name', 'новое имя лоха: ', name)
    elif ans == '2':
        return update('password', 'новый пароль лоха: ', name)
    else:
        return change()

def update(column, part, name):
    data = input(f"Введите {part}")
    db = sqlite3.connect("DB/data.db")
    c = db.cursor()
    if column == 'name':
        if check_name(data):
            c.execute("UPDATE users SET name = ? WHERE name = ?", (data, name))
            name = data
        else:
            print("Имя занято!")
            db.close()
            return update(column, part)
    elif column == 'password':
        c.execute("UPDATE users SET password = ? WHERE name = ?", (data, name))
    else:
        return "Dick"
    db.commit()
    db.close()
    return "Данные изменены"

def delete_user():
    db = sqlite3.connect("DB/data.db")
    c = db.cursor()
    id = c.execute("SELECT id FROM users WHERE name = ?", (name,)).fetchone()[0]
    c.execute("DELETE FROM users WHERE name = ?", (name,))
    c.execute("DELETE FROM money WHERE user_id = ?", (id,))
    db.commit()
    db.close()
    return "Пользователь удален из жизни!"

def main():
    register()
    while True:
        ans = input("1. Добавить транзакцию\n2. Проверить баланс\n3. Изменить аккаунт\n4. Удалить аккаунт\n5. Выйти из программы\n")
        if ans == '1':
            plus()
            print("pozdravlyau")
        elif ans == '2':
            balance = check_balance()
            print(f"Ваш баланс: {balance}")
        elif ans == '3':
            result = change()
            print(result)
        elif ans == '4':
            result = delete_user()
            print(result)
        elif ans == '5':
            print("Выходим")
            break
        else:
            print("Не понял тебя(")
            
if __name__ == "__main__":
    main()