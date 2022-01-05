from time import sleep

import pyautogui
import cv2
from PIL import ImageGrab

pyautogui.FAILSAFE = False


def isGameOver():
    if pyautogui.locateOnScreen('images/gameover.png', confidence=0.8) is not None:
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
        playerRegion = (topLeft[0], bottomRight[1] - 5, bottomRight[0] - topLeft[0] + 1, 1)
        img = pyautogui.screenshot(region=playerRegion)
        img = img.convert('L')
        width = bottomRight[0] + 1
        for x in range(0, width):
            print(x)
            if img.getpixel((x, 0)) >= 40:
                return x + 30

    except TypeError:
        return None


'''def locatePlayer(topLeft, bottomRight):
    try:
        playerBox = None
        # playerRegion = (8, 633, 961, 30) # 1920:1080 100%
        playerRegion = (topLeft[0], bottomRight[1] - 27, bottomRight[0] - topLeft[0] + 2, 28)

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
        return pyautogui.center(playerBox).x

    except TypeError:
        return None'''


def radar(playerPos):
    region = (playerPos['x'] - 10, playerPos['y'] - 300, 70, 300)
    scr = pyautogui.screenshot('sceren.png', region=region)
    for y in range(playerPos['y'] - 300, playerPos['y']):
        for x in range(playerPos['x'] - 10, playerPos['x'] + 70):
            continue
