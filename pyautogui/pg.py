import pyautogui as pg
import time
# print(pg.position())

user = input("Введите юзернейм жертвы: ")
pg.moveTo(373, 1065, 1)
pg.click()
time.sleep(1)
pg.moveTo(141, 59, 1)
pg.click()
pg.typewrite(user,0.1)
pg.typewrite(["enter"])
time.sleep(1)
pg.moveTo(1600, 490, 1)
pg.click()
time.sleep(1)
pg.moveTo(1676, 321, 1)
pg.click()