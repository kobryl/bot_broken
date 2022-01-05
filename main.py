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
    interval = 0.2

    pyautogui.keyDown('space')

    while not image.isGameOver():
        playerPos = image.locatePlayer(tl, br)
        #bullets = radar()
        #if bullets is not None:
        #    for bullet in bullets:
        #        if bulletInRange(bullet, playerPos):

        sleep(interval)

    pyautogui.keyUp('space')

    print('Koniec programu')
    return


def bulletInRange(x, pos):
    if x >= pos - 40 and x <= pos + 40:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
