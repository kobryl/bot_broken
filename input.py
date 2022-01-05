import pyautogui
from time import sleep

fps = 50
interval = 1 / fps
speed = 8

pyautogui.PAUSE = 0


# Function prepares the game's windows with appropriate commands (fullscreen, reset zoom, refresh)
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


# Function waits a given amount of seconds for the user to focus on the game's window
# Parameters:
#   n: Number of seconds to wait
def focusTimer(n):
    print('Przejdź do okna przeglądarki. Skrypt rozpocznie pracę za:')
    for i in range(n, 0, -1):
        print(i)
        sleep(1)


# Function moves the player a given amount of pixels in a given direction
# Parameters:
#   x: Number of pixels to move
#   direction: 'left' or 'right'
def move(x, direction):
    pyautogui.keyDown(direction)
    sleep(interval * (x / speed))
    pyautogui.keyUp(direction)
