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


# Sprawdza, o ile można się przemieścić w danym kierunku
def checkSides(direction, playerPos, tl, br):
    collision = []
    radarWidth = 180
    radarHeight = 130
    if direction == 'left:':
        if playerPos[0] - 30 - radarWidth < tl[0]:
            regionX = tl[0]
        else:
            regionX = playerPos[0] - 30 - radarWidth
        if playerPos[1] - 110 > tl[1]:
            regionY = tl[1]
        else:
            regionY = playerPos[1] - 110
        region = (regionX, regionY, radarWidth, radarHeight)
    else:
        regionX = playerPos[0] + 30
        if playerPos[0] + 30 + radarWidth > br[0]:
            radarWidth = br[0] - (playerPos[0] + 30)
        else:
            radarWidth = 180
        if playerPos[1] - 110 > tl[1]:
            regionY = tl[1]
        else:
            regionY = playerPos[1] - 110
        region = (regionX, regionY, radarWidth, radarHeight)
    collision.append(radarWidth)
    scr = pyautogui.screenshot('sceren2.png', region=region)
    for y in range(radarHeight):
        for x in range(radarWidth):
            pix = scr.getpixel((x, y))
            if not (pix[0] == pix[1] and pix[0] == pix[2]):
                collision.append(abs(playerPos[0] - x) - 1)
    return min(collision)


def wallDetection(playerPos, tl, br):
    if playerPos[0] - 30 <= tl.x or playerPos[0] + 30 >= br.x:
        return True
    return False
