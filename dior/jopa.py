import sqlite3
db = sqlite3.connect("dior/bomba.db")
c = db.cursor()

def ins():
    c.execute("INSERT INTO ...")
    #Добавить код