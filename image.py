import pyautogui

pyautogui.FAILSAFE = False


# Function detects game over screen
# Return: True - if game over screen is visible, False - otherwise
def isGameOver():
    if pyautogui.locateOnScreen('images/gameover.png', confidence=0.8) is not None:
        return True
    else:
        return False


# Function seeks for the game board corners
# Return: Top-left and bottom-right corners' coordinates or None if not found
def locateCorners():
    try:
        tl = pyautogui.locateOnScreen('images/topleft.png')
        br = pyautogui.locateOnScreen('images/bottomright.png')

        # Add images' offset to the coordinates
        begin = tl[0] + 4, tl[1] + 1
        end = br[0] + 36, br[1] + 37

        return begin, end

    except TypeError:
        return None, None


# Function seeks for the player's position on the game board
# Parameters:
#   topLeft (x, y): top-left corner of the game board
#   bottomRight (x, y): bottom-rightt corner of the game board
# Return: Player's center x coordinate on the game board or None if corners were None
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


# Function detects any projectiles above the player
# Parameters:
#   playerPos (x, y): x - center of the player, y - height of the player;
#   tl (x, y): top-left corner of the game board
#   br (x, y): bottom-right corner of the game board
# Return: List of x coordinates of enemy projectiles
def radar(playerPos, tl, br):
    try:
        bulletsx = []
        radarHeight = 310
        radarWidth = 90

        if playerPos[0] - radarWidth / 2 < tl[0]:
            regionX = tl[0]
        else:
            regionX = playerPos[0] - radarWidth / 2
        if playerPos[1] - radarHeight < tl[1]:
            regionY = tl[1]
        else:
            regionY = playerPos[1] - radarHeight

        region = (regionX, regionY, radarWidth, radarHeight)
        scr = pyautogui.screenshot(region=region)

        for y in range(radarHeight):
            for x in range(radarWidth):
                pix = scr.getpixel((x, y))
                if not (pix[0] == pix[1] and pix[0] == pix[2]):
                    if not (x + 7 >= radarWidth):
                        if not (scr.getpixel((x + 7, y)) == pix):
                            bulletsx.append(playerPos[0] - radarWidth / 2 + x)
                            bulletsx = list(set(bulletsx))

        return bulletsx

    except TypeError:
        return None


# Function calculates maximum safe move value in given direction
# Parameters:
#   direction: 'left' or 'right'
#   playerPos (x, y): x - center of the player, y - height of the player;
#   tl (x, y): top-left corner of the game board
#   br (x, y): bottom-right corner of the game board
# Return: Maximum safe move value in given direction
def checkSides(direction, playerPos, tl, br):
    collision = []
    radarWidth = 180
    radarHeight = 130
    if direction == 'left':
        if wallDetection(playerPos[0], tl, br) == 'left':
            return 0
        if playerPos[0] - 30 - radarWidth < tl[0]:
            regionX = tl[0]
        else:
            regionX = playerPos[0] - 30 - radarWidth
        if playerPos[1] - 110 < tl[1]:
            regionY = tl[1]
        else:
            regionY = playerPos[1] - 110
        region = (regionX, regionY, radarWidth, radarHeight)
    else:
        if wallDetection(playerPos[0], tl, br) == 'right':
            return 0
        regionX = playerPos[0] + 28
        if regionX + radarWidth > br[0]:
            radarWidth = br[0] - regionX
        else:
            radarWidth = 180
        if playerPos[1] - 110 < tl[1]:
            regionY = tl[1]
        else:
            regionY = playerPos[1] - 110
        region = (regionX, regionY, radarWidth, radarHeight)
    collision.append(radarWidth)
    scr = pyautogui.screenshot(region=region)
    for y in range(radarHeight):
        for x in range(radarWidth):
            pix = scr.getpixel((x, y))
            if not (pix[0] == pix[1] and pix[0] == pix[2]):
                if direction == 'left':
                    collision.append(max(abs(radarWidth - x) - 1, 0))
                else:
                    collision.append(max(x - 1, 0))
    return min(collision)


# Function checks if the player is touching a wall
# Parameters:
#   playerPosX: center of the player;
#   tl (x, y): top-left corner of the game board
#   br (x, y): bottom-right corner of the game board
# Return: 'left' - if the player is touching the left wall, 'right' - if the player is touching the right wall,
#           False - otherwise
def wallDetection(playerPosX, tl, br):
    if playerPosX - 30 <= tl[0]:
        return 'left'
    elif playerPosX + 30 >= br[0]:
        return 'right'
    return False
