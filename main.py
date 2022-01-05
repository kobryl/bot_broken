from time import sleep
import pyautogui

import input
import image


def main():
    # input.initWindow(10)        #todo: uncomment
    pyautogui.FAILSAFE = False

    tl, br = image.locateCorners()
    interval = 0.1

    pyautogui.keyDown('space')

    while not image.isGameOver():
        playerPos = image.locatePlayer(tl, br)
        y = br[1] - 20
        bullets = image.radar((playerPos, y), tl, br)
        if len(bullets) > 1:
            direction = determineDodgeDirection(bullets, (playerPos, y), tl, br)
            if direction == 'safe':
                safe = getLongestSafe((playerPos, y), tl, br)
                direction = safe[0]
                length = safe[1]
            else:
                length = determineDodgeLength(bullets, playerPos, direction)
            print(playerPos, length, direction, bullets)
            input.move(length, direction)
        sleep(interval)

    pyautogui.keyUp('space')

    print('Koniec programu')
    return


def determineDodgeDirection(bullets, playerPos, tl, br):
    leftSafe = image.checkSides('left', playerPos, tl, br)
    rightSafe = image.checkSides('right', playerPos, tl, br)
    leftRequired = determineDodgeLength(bullets, playerPos[0], 'left')
    rightRequired = determineDodgeLength(bullets, playerPos[0], 'right')
    #print(leftSafe, rightSafe, leftRequired, rightRequired)
    if leftSafe >= leftRequired:
        return 'left'
    elif rightSafe >= rightRequired:
        return 'right'
    else:
        return 'safe'


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


def getLongestSafe(playerPos, tl, br):
    leftSafe = image.checkSides('left', playerPos, tl, br)
    rightSafe = image.checkSides('right', playerPos, tl, br)
    if rightSafe > leftSafe:
        return 'right', rightSafe
    else:
        return 'left', leftSafe


if __name__ == '__main__':
    main()
