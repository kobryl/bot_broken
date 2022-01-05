import pyautogui

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
        width = bottomRight[0] + 1

        for x in range(0, width):
            if img.getpixel((x, 0))[0] >= 230:
                return x + 30

    except TypeError:
        return None

    except IndexError:
        return None


def radar(playerPos, tl, br):
    bulletsx = []
    radarHeight = 310
    radarWidth = 94

    if playerPos[0] - radarWidth / 2 < tl[0]:
        regionX = tl[0]
    else:
        regionX = playerPos[0] - radarWidth / 2
    if playerPos[1] - radarHeight < tl[1]:
        regionY = tl[1]
    else:
        regionY = playerPos[1] - radarHeight

    region = (regionX, regionY, radarWidth, radarHeight)
    scr = pyautogui.screenshot('sceren.png', region=region)

    for y in range(radarHeight):
        for x in range(radarWidth):
            pix = scr.getpixel((x, y))
            if not (pix[0] == pix[1] and pix[0] == pix[2]):
                if not (x + 7 >= radarWidth):
                    if not (scr.getpixel((x + 7, y)) == pix):
                        bulletsx.append(playerPos[0] - radarWidth / 2 + x)
                        bulletsx = list(set(bulletsx))

    return bulletsx


# Sprawdza, czy bezpiecznie jest się przemieścić 'x' pikseli w bok z pozycji 'playerPos'
def checkSides(x, playerPos, tl, br):
    safe = True
    x1 = playerPos[0] - 30
    regionl = (playerPos[0] - 30 - 180, playerPos[1] - 110, 180, 130)
    regionr = (playerPos[0] + 30, playerPos[1] - 110, 180, 130)
    return safe
