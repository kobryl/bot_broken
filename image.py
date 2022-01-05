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
            if img.getpixel((x, 0)) >= 40:
                return x + 30

    except TypeError:
        return None


def radar(playerPos):
    bulletsx = []
    region = (playerPos[0] - 40, playerPos[1] - 300, 80, 300)
    scr = pyautogui.screenshot('sceren.png', region=region)
    for y in range(300):
        for x in range(80):
            pix = scr.getpixel((x, y))
            if x + 7 < 80:
                scanx = x + 7
            elif x - 7 >= 0:
                scanx = x - 7
            else:
                scanx = x
            if not (pix[0] == pix[1] and pix[0] == pix[2]) and not (scanx != x and scr.getpixel((scanx, y)) != pix):
                bulletsx.append(playerPos[0] - 40 + x)
                bulletsx = list(set(bulletsx))
    return bulletsx


def checkSides(playerPos, move, direction):
    safe = True
    x1 = playerPos[0] - 30
    region = ()
    return safe
