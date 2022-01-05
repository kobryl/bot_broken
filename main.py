import cv2
import numpy as np
import PIL
from time import sleep, time
import pyautogui
# todo: wywalić niepotrzebne

import input
import image


def main():
    input.initWindow()
    pyautogui.FAILSAFE = False

    tl, br = image.locateCorners()
    interval = 0.1

    pyautogui.keyDown('space')

    while not image.isGameOver():
        playerPos = image.locatePlayer(tl, br)
        y = br[1] - 21
        bullets = image.radar((playerPos, y))
        if len(bullets) > 0:
            direction = determineDodgeDirection(bullets, playerPos)
            length = determineDodgeLength(bullets, playerPos, direction)
            input.move(length, direction)
        sleep(interval)

    pyautogui.keyUp('space')

    print('Koniec programu')
    return


def determineDodgeDirection(bullets, playerPos):
    leftBullets = 0
    rightBullets = 0
    for bullet in bullets:
        if bullet <= playerPos:
            leftBullets += 1
        else:
            rightBullets += 1
    if leftBullets > rightBullets:
        return 'right'
    else:
        return 'left'


def determineDodgeLength(bullets, playerPos, direction):
    dangerBounds = (min(bullets), max(bullets))
    leftPlayerBoundary = playerPos - 30
    rightPlayerBoundary = playerPos + 30

    if direction == 'left':
        return dangerBounds[1] - leftPlayerBoundary
    else:
        return rightPlayerBoundary - dangerBounds[0]


if __name__ == '__main__':
    main()
