import sqlite3

def insert_users(name, surname, tg_id: int):
    db = sqlite3.connect("data.db")
    c = db.cursor()
    try:
        c.execute("INSERT INTO users (name, surname, tg_id) VALUES (?,?,?)",(name, surname, tg_id))
    except sqlite3.IntegrityError as e:
        db.close()
        return "Вы уже зареганы"
    db.commit()
    db.close()
    return "Регестрация пройдена"