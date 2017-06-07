from math import *
from tkinter import *
from random import *
from time import *

tk = Tk()

WIDTH = 1200
HEIGHT = 600

s = Canvas(tk, width=WIDTH, height=HEIGHT, background="skyblue")
s.pack()


def setInitialValues():
    global Tilex, Tiley, TileSpeedx, TileSpeedy, TileWidth, TileHeight, Ballx, Bally, BallSpeedx, BallSpeedy, BallRadius, xMouse, yMouse, ballcolour, Coinsx, Coinsy, CoinsRadius
    ballcolour = "black"
    xMouse = 0
    yMouse = 0
    TileWidth = 200
    TileHeight = 50
    Tilex = (.50 * WIDTH)
    Tiley = (.85 * HEIGHT)
    TileSpeedx = 0
    TileSpeedy = 0
    Ballx = (.50 * WIDTH)
    Bally = (.76 * HEIGHT)
    BallSpeedx = 0
    BallSpeedy = 0
    BallRadius = 50
    Coinsx = []
    Coinsy= []
    CoinsRadius= 25


##def mouseInsideBall():
##    dist = sqrt( (yMouse-Bally)**2 + (xMouse-Ballx)**2 )
##
##    if dist < BallRadius:
##        return True
##
##    else:
##        return False
##
##
##
##def mouseClickHandler( event ):
##
##    global xMouse, yMouse, ballcolour, Ballx , Bally
##
##    xMouse = event.x
##    yMouse = event.y
##
##    if mouseInsideBall() == True:
##
##        BallSpeedx = 15
##        BallSpeedy = -15

def keyDownHandler(event):
    global TileSpeedx, TileSpeedy, BallSpeedy, BallSpeedx, SpeedPositive, SpeedNegative

    if event.keysym == "Left":
        TileSpeedx = -15


    elif event.keysym == "Right":
        TileSpeedx = 15

    elif event.keysym == "Up":
        BallSpeedy = -5
        BallSpeedx = 5

def keyUpHandler(event):
    global TileSpeedx, TileSpeedy, BallSpeedy, BallSpeedx

    TileSpeedx = 0
    TileSpeedy = 0


        
def updateBallPosition():
    global Tilex, Tiley, Ballx, Bally, BallSpeedx, BallSpeedy, BallRadius, TileSpeedx, TileSpeedy

    if Ballx+BallRadius >= WIDTH:
        BallSpeedx = -15
    elif Ballx <= 0:
        BallSpeedx = 15
       
        
    if Bally+BallRadius >= Tiley:
        if Ballx + BallRadius  <= Tilex + TileWidth and Ballx + BallRadius >= Tilex  :
            BallSpeedy = -15
    elif Bally <=0:
        BallSpeedy = 15
        
    if Tilex + TileWidth >= WIDTH:
        TileSpeedx = -15
    
    elif Tilex <= 0:
        TileSpeedx = 15

    if Bally >= HEIGHT:
        BallSpeedx= 0
        BallSpeedy= 0
        TileSpeedx  =0
        TileSpeedy = 0
        Tilex= (0.50 * WIDTH)
        Tiley= (.85 * HEIGHT)
        Ballx= (.50 * WIDTH)
        Bally= (.80 * HEIGHT)

    Tilex = Tilex + TileSpeedx
    Tiley = Tiley + TileSpeedy
    Ballx = Ballx + BallSpeedx
    print(Ballx, " ", BallSpeedx)
    Bally = Bally + BallSpeedy
    print (Bally, "     ")


# def getHexValue (x):
#
#     H= ["1","2","3","4","5", "6","7","8","9","A","B","C","D","E","F"]
#     hexValue = ""
#     while x != 0:
#         q = int(x/16)
#         r = x % 16
#         hexValue = H[r] + hexValue
#         x = q
#
#     if hexValue == "":
#         return "00"
#
#     elif len(hexValue) == 1:
#         return "0" + hexValue
#
#     else:
#         return hexValue
#
# def DrawBackground():
#    for s in range(0,256):
#         rColor = getHexValue( 255- s )
#         color = "#FFC0" + rColor
#
#         x = 3 * shade + 200
#
#         s.create_rectangle( 0, x, 1000, x+3, fill = color, outline = color)
def getDistance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def DrawCoins():
    global coinx, coiny, Coinsx, Coinsy, CoinsRadius
    for m in range(15):

        DistanceRight = False

        while DistanceRight == False:
            coinx = randint(0, 1200)
            coiny = randint(0, 300)

            Colison = 0

            for i in range(0, len(Coinsx)):
                d = getDistance(Coinsx[i], Coinsy[i], coinx, coiny)

                if d <= 2 * CoinsRadius:
                    Colison = Colison + 1

            if Colison == 0:
                DistanceRight = True

    Coinsx.append(coinx)
    Coinsy.append(coiny)
    # Colors = choice(["Red", "yellow","green", "Blue"])
    # CoinsColor.append(Colors)
    Coin = s.create_oval(coinx - CoinsRadius, coiny - CoinsRadius, coinx + CoinsRadius, coiny + CoinsRadius, fill="Red",
                         outline="white")


def checkco():
    global Coinsx, Coinsy, Ballx, Bally, CoinsRadius, BallRadius
    if Coinsx == Ballx and Coinsx + CoinsRadius == Ballx + BallRadius:
        print("hello")
        Coinsx.remove(Coinsx[i])


def DrawObject():
    global Ball, Tile
    Ball = s.create_oval(Ballx, Bally, Ballx + BallRadius, Bally + BallRadius, fill=ballcolour)
    Tile = s.create_rectangle(Tilex, Tiley, Tilex + TileWidth, Tiley + TileHeight, fill="Yellow", outline="Yellow")
    


def runGame():
    setInitialValues()
    DrawCoins()
    while True:
        updateBallPosition()
        DrawObject()
        s.update()
        sleep(0.01)
        s.delete(Tile, Ball)

##def QuitGame ():
##    
tk.after(0, runGame)
s.bind("<Key>", keyDownHandler)
s.bind("<KeyRelease>", keyUpHandler)
s.pack()
s.focus_set()
tk.mainloop()
