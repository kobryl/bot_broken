import pyautogui
from time import sleep

fps = 50
interval = 1 / fps
speed = 8

pyautogui.PAUSE = 0


# Przygotowuje okno do operacji programu - pełny ekran, reset przybliżenia oraz odświeżenie
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


# Rusza graczem o 'x' pikseli w podanym kierunku ('left'/'right')
def move(x, direction):
    pyautogui.keyDown(direction)
    sleep(interval * (x / speed))
    pyautogui.keyUp(direction)
