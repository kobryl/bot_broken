import pyautogui
from time import sleep

import image

movingLeft = False
ovingRight = False
fps = 50
interval = 1 / fps
speed = 8
pixelsPerSecond = fps * speed

pyautogui.PAUSE = 0

# todo: komentarz
def initWindow():
    focusTimer(5)
    # fullscreen
    pyautogui.keyDown('f11')
    pyautogui.keyUp('f11')
    # reset zoom
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('0')
    pyautogui.keyUp('0')
    pyautogui.keyUp('ctrl')
    sleep(1.5)
    # refresh
    pyautogui.keyDown('f5')
    pyautogui.keyUp('f5')
    sleep(0.3)


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


# Przesuwa gracza o 'x' pikseli w lewo, gdzie x to wielokrotność prędkości gracza, czyli 8.
def left(x):
    pyautogui.keyDown('left')
    sleep(x / pixelsPerSecond)
    pyautogui.keyUp('left')


# Przesuwa gracza o 'x' pikseli w prawo, gdzie x to wielokrotność prędkości gracza, czyli 8.
def right(x):
    pyautogui.keyDown('right')
    sleep(x / pixelsPerSecond)
    pyautogui.keyUp('right')