import pyautogui as pg
import time
#print(pg.position())

def main():
    pg.moveTo(1823, 14, 1)
    pg.click()
    time.sleep(1)
    pg.moveTo(261, y=166)
    pg.doubleClick()

def telega():
    pg.moveTo(1064, 1047, 1)
    pg.click()
    time.sleep(1)
    
