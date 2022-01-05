from time import sleep
import pyautogui

import input
import image


def main():
    # input.initWindow(10)        #todo: uncomment
    pyautogui.FAILSAFE = False

    tl, br = image.locateCorners()
    interval  = 0.08
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
    print(image.checkSides('right', (488, br[1] - 20), tl, br))
    print('Koniec programu')
    return


# Function determines in which direction the player should escape
# Parameters:
#   bullets - list of detected bullets' x coordinates
#   playerPos (x, y): x - player's center x coordinate, y - player's height
#   tl: top-left corner coordinates
#   br: bottom-right corner coordinates
# Return: direction in which move should be made ('left' or 'right')
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


# Function determines how long should move be to dodge the bullets
# Parameters:
#   bullets: list of bullets' x coordinates
#   playerPos (x, y): x - player's center x coordinate, y - player's height
#   direction - 'left' or 'right'
# Return: Lengh of needed dodge
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
