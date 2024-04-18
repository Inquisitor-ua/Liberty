import sqlite3
db = sqlite3.connect("dior/bomba.db")
c = db.cursor()

def ins(name, opis, ottenki, image):
    c.execute("INSERT INTO pomadu (name, opis, ottenki, image) VALUES (?,?,?,?)", (name, opis, ottenki, image))
    db.commit()
    #Добавить код