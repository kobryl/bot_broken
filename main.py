from time import sleep
import pyautogui

import input
import image


def main():
    # input.initWindow(10)        #todo: uncomment
    pyautogui.FAILSAFE = False

    tl, br = image.locateCorners()
    interval = 0.08

    pyautogui.keyDown('space')

    while not image.isGameOver():
        playerPos = image.locatePlayer(tl, br)
        y = br[1] - 20
        bullets = image.radar((playerPos, y), tl, br)
        if len(bullets) > 0:
            direction = determineDodgeDirection(bullets, (playerPos, y), tl, br)
            length = determineDodgeLength(bullets, playerPos, direction)
            #print(playerPos, length, direction, bullets)
            input.move(length, direction)
        else:
            wall = image.wallDetection(playerPos, tl, br)
            if wall == 'left':
                leftSafe = image.checkSides('left', (playerPos, y), tl, br)
                input.move(leftSafe, 'left')
            elif wall == 'right':
                rightSafe = image.checkSides('left', (playerPos, y), tl, br)
                input.move(rightSafe, 'left')
        sleep(interval)

    pyautogui.keyUp('space')

    print('Koniec programu')
    return


def determineDodgeDirection(bullets, playerPos, tl, br):
    leftSafe = image.checkSides('left', playerPos, tl, br)
    rightSafe = image.checkSides('right', playerPos, tl, br)
    print(leftSafe, rightSafe)
    leftRequired = determineDodgeLength(bullets, playerPos[0], 'left')
    rightRequired = determineDodgeLength(bullets, playerPos[0], 'right')
    if leftSafe >= leftRequired:
        return 'left'
    elif rightSafe >= rightRequired:
        return 'right'
    else:
        leftBullets = 0
        rightBullets = 0
        for bullet in bullets:
            if bullet <= playerPos[0]:
                leftBullets += 1
            else:
                rightBullets += 1
        if leftBullets > rightBullets:
            return 'right'
        else:
            return 'left'


def determineDodgeLength(bullets, playerPos, direction):
    radarOffset = 15
    moveOffset = 8
    dangerBounds = (min(bullets), max(bullets))
    leftPlayerBoundary = playerPos - 30 - radarOffset
    rightPlayerBoundary = playerPos + 30 + radarOffset + 8

    if direction == 'right':
        return dangerBounds[1] - leftPlayerBoundary + moveOffset
    else:
        return rightPlayerBoundary - dangerBounds[0] - moveOffset + 8


if __name__ == '__main__':
    main()
