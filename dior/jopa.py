import sqlite3
db = sqlite3.connect("dior/bomba.db")
c = db.cursor()

def ins(name, opis):
    c.execute("INSERT INTO pomadu (name, opis ) VALUES (?,?)", (name, opis ))
    db.commit()
    #Добавить код