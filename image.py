import pyautogui

# NIE DZIAŁA
def isGameOver():
    if pyautogui.locateOnScreen('images/gameover.png') is not None:
        return True
    else:
        return False


def locateCorners():
    tl = pyautogui.locateOnScreen('images/topleft.png')
    br = pyautogui.locateOnScreen('images/bottomright.png')
    print(tl, br)


def locatePlayer():
