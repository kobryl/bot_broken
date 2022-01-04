import pyautogui
from time import sleep

movingLeft = False
movingRight = False
pixelsPerSec = 448


# todo: komentarz
def initWindow():
    focusTimer(10)
    # fullscreen
    pyautogui.keyDown('f11')
    pyautogui.keyUp('f11')
    # reset zoom
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('0')
    pyautogui.keyUp('0')
    pyautogui.keyUp('ctrl')
    sleep(2)
    # refresh
    pyautogui.keyDown('f5')
    pyautogui.keyUp('f5')


# Czeka 'n' sekund na przejście użytkownika do okna z grą
def focusTimer(n):
    print('Przejdź do okna przeglądarki. Skrypt rozpocznie pracę za:')
    for i in range(n, 0, -1):
        print(i)
        sleep(1)


# todo: komentarz
def shoot():
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')


# Porusza gracza o x pikseli w lewo
def left(x):
    global movingLeft
    pyautogui.keyDown('left')
    movingLeft = True
    sleep(x / pixelsPerSec)
    pyautogui.keyUp('left')
    movingLeft = False


# Porusza gracza o x pikszeli w prawo
def right(x):
    global movingRight
    pyautogui.keyDown('right')
    movingRight = True
    sleep(x / pixelsPerSec)
    pyautogui.keyUp('right')
    movingRight = False
