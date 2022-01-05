from time import sleep
import pyautogui

import input
import image


def main():
    # input.initWindow()        #todo: uncomment
    pyautogui.FAILSAFE = False

    tl, br = image.locateCorners()
    interval = 0.15

    pyautogui.keyDown('space')

    while not image.isGameOver():
        playerPos = image.locatePlayer(tl, br)
        y = br[1] - 21
        bullets = image.radar((playerPos, y), tl, br)
        if len(bullets) > 0:
            direction = determineDodgeDirection(bullets, playerPos)
            length = determineDodgeLength(bullets, playerPos, direction)
            #print(playerPos, length, direction, bullets)
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
    radarOffset = 15
    dangerBounds = (min(bullets), max(bullets))
    leftPlayerBoundary = playerPos - 30 - radarOffset
    rightPlayerBoundary = playerPos + 30 + radarOffset

    if direction == 'right':
        return dangerBounds[1] - leftPlayerBoundary
    else:
        return rightPlayerBoundary - dangerBounds[0]


if __name__ == '__main__':
    main()
