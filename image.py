import pyautogui


def isGameOver():
    if pyautogui.locateOnScreen('images/gameover.png') is not None:
        return True
    else:
        return False


def locateCorners():
    tl = pyautogui.locateOnScreen('images/topleft.png')
    br = pyautogui.locateOnScreen('images/bottomright.png')
    begin = tl[0]+4, tl[1]+1
    end = br[0]+12, br[1]+12
    return begin, end


def locatePlayer():
    playerBox = None
    playerWhiteBox = pyautogui.locateOnScreen('images/player.png')
    playerRedBox = pyautogui.locateOnScreen('images/player_invincible.png')

    if playerRedBox is not None:
        playerBox = playerRedBox
    elif playerWhiteBox is not None:
        playerBox = playerWhiteBox
    else:
        return playerBox

    x1 = playerBox[0]
    x2 = x1 + playerBox[2]

    center = (x1 + x2) / 2
    return center
