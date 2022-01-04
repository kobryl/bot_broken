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
    playerBox = None
    playerWhiteBox = pyautogui.locateOnScreen('images/player.png')
    playerRedBox = pyautogui.locateOnScreen('images/plyer_invincible.png')
    if playerRedBox is not None:
        playerBox = playerRedBox
    elif playerWhiteBox is not None:
        playerBox = playerWhiteBox
    else:
        return playerBox
    x1 = playerBox['left']
    y1 = playerBox['top']
    x2 = x1 + playerBox['width']
    y2 = y1 + playerBox['height']

    center = (x1 + x2) / 2, (y1 + y2) / 2
    return center
