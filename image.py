import pyautogui


def isGameOver():
    if pyautogui.locateOnScreen('images/gameover.png') is not None:
        return True
    else:
        return False


def locateCorners():
    try:
        tl = pyautogui.locateOnScreen('images/topleft.png')
        br = pyautogui.locateOnScreen('images/bottomright.png')
        begin = tl[0]+4, tl[1]+1
        end = br[0]+36, br[1]+37
        return begin, end
    except TypeError:
        return None, None


def locatePlayer(topLeft, bottomRight):
    try:
        playerBox = None
        # playerRegion = (8, 633, 961, 30) # 1920:1080 100%
        playerRegion = (topLeft[0], bottomRight[1] - 27, bottomRight[0] - topLeft[0] + 2, 28)
        print(playerRegion)
        playerWhiteBox = pyautogui.locateOnScreen('images/player.png', region=playerRegion)
        playerRedBox = pyautogui.locateOnScreen('images/player_invincible.png', region=playerRegion)

        if playerRedBox is None and playerWhiteBox is None:
            playerWhiteBox = pyautogui.locateOnScreen('images/player_corner.png', region=playerRegion)
            playerRedBox = pyautogui.locateOnScreen('images/player_invincible_corner.png', region=playerRegion)

        if playerRedBox is not None:
            playerBox = playerRedBox
        elif playerWhiteBox is not None:
            playerBox = playerWhiteBox
        else:
            return playerBox
        print(playerBox)
        return pyautogui.center(playerBox).x
    except TypeError:
        return None

'''
def locateEnemies():



def locateEnemyBullets():


'''