import pyautogui
from time import sleep
from time import time

movingLeft = False      # todo: usunąć niepotrzebne
movingRight = False
fps = 50
interval = 1 / fps
checkFrequency = 8      # co który tick
speed = 8

pyautogui.PAUSE = 0


# todo: komentarz
def initWindow():
    focusTimer(2)    # todo: zmiana wartości

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


def interruptMove():
    return False


# todo: komentarz
def move(x, direction):
    tickCount = x // speed
    pyautogui.keyDown(direction)

    if tickCount >= checkFrequency:
        checkCount = tickCount // checkFrequency
        timeDiff = 0
        for tick in range(0, checkCount - 1):
            if interruptMove():
                print('interrupt')
                return
            startTime = time()
            expectedTime = interval * checkFrequency
            sleep((interval * checkFrequency) - timeDiff)
            actualTime = time() - startTime
            timeDiff = actualTime - expectedTime
        offsetTime = (interval * ((tickCount % checkFrequency) + checkFrequency)) - timeDiff
        sleep(offsetTime)
    else:
        sleep(interval * tickCount)

    pyautogui.keyUp(direction)