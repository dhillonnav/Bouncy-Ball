from math import *
from tkinter import *
from random import *
from time import *

WIDTH = 1000
HEIGHT = 750

# constants
PLAY = 0
INST = 1
INTRO = 2
EASY = 3
MEDIUM = 4
HARD = 5

# global variables
state = INTRO

def instructions():
    pass

def easyButton():
    setInitialValues(EASY)

def mediumButton():
    setInitialValues(MEDIUM)

def hardButton():
    setInitialValues(HARD)

def levelsButton():
    global EsayLevel, MediumLevel, HardLevel, backToIntroButton, tk
    EsayLevel= Button(tk, text="Easy", command=easyButton, font="Times 30")
    EsayLevel.pack()
    EsayLevel.place(x=435, y=300)
    MediumLevel= Button(tk, text="Medium", command=mediumButton, font="Times 30")
    MediumLevel.pack()
    MediumLevel.place(x=435, y=400)
    HardLevel= Button(tk, text="Hard", command=hardButton, font="Times 30")
    HardLevel.pack()
    HardLevel.place(x=435, y=500)
    backToIntroButton = Button(tk, text="Reset Game", font="Times 25", command=backToIntro, anchor=CENTER)
    backToIntroButton.pack()
    backToIntroButton.place(x=800, y=450)

def playPressed():
    global InstructionLabel, playButton, startMessage, background
    InstructionLabel.destroy()
    playButton.destroy()
    s.delete(startMessage)
    s.update()
    state = PLAY

def instPressed():
    state = INST

def drawIntroScreen():
    global InstructionLabel, playButton, startMessage, background, tk, s

    bac_img = PhotoImage(file="back.gif")
    background = s.create_image(500, 400, image=bac_img)

    startMessage = s.create_text(350, 50, text="Catch Some Fish", font="Times 38", fill="red", anchor=W)

    playButton = Button(tk, text="Play", font="Times 30", command=playPressed, anchor=CENTER)
    playButton.pack()
    playButton.place(x=500, y=250, width=100, height=50)

    InstructionLabel = Button(tk, text="Instructions", command=instPressed, font="Times 30")
    InstructionLabel.pack()
    InstructionLabel.place(x=435, y=300)
    s.update()

def intro_screen():
    pass

def setInitialValues(level):
    global LevelChooser, startMessage, WinMessage,  gameRunning, PlayGame, Tilex, Tiley, TileSpeedx, TileSpeedy, TileWidth, TileHeight, Ballx, Bally, BallSpeedx, BallSpeedy, BallRadius, xMouse, yMouse, ballcolour, Coins, Coinsx, Coinsy, CoinsRadius, ConstantSpeed, ConstantSpeedNegative, CoinsColour, Collided, Coin
    ballcolour = "black"
    xMouse = 0
    yMouse = 0
    TileWidth = 200
    TileHeight = 50
    Tilex = (.45 * WIDTH)
    Tiley = (.87 * HEIGHT)

    if level == EASY:
        TileSpeedx = 0
        TileSpeedy = 0
        BallSpeedx = 0
        BallSpeedy = 0
    elif level == MEDIUM:
        TileSpeedx = 0
        TileSpeedy = 0
        BallSpeedx = 0
        BallSpeedy = 0
    elif level == HARD:
        TileSpeedx = 0
        TileSpeedy = 0
        BallSpeedx = 0
        BallSpeedy = 0

    Ballx = (.45 * WIDTH)
    Bally = (.82 * HEIGHT)
    BallRadius = 57
    Coinsx = []
    Coinsy= []
    CoinsColour= []
    CoinsRadius= 23
    ConstantSpeed = 15
    ConstantSpeedNegative= -15
    Collided= False
    WinMessage = 0
    gameRunning = True


def play_game():
    exit(1)

def keyDownHandler(event):
    global ConstantSpeed, ConstantSpeedNegative,TileSpeedx, TileSpeedy, BallSpeedy, BallSpeedx, SpeedPositive, SpeedNegative
    if event.keysym == "Left":
        TileSpeedx = ConstantSpeedNegative - 10

    elif event.keysym == "Right":
        TileSpeedx = ConstantSpeed + 10

    elif event.keysym == "Up":
        BallSpeedy = ConstantSpeedNegative
        BallSpeedx = choice([ConstantSpeed, ConstantSpeedNegative])
    elif event.keysym == "Q" and "q":
        s.delete(Ball, Tile)

def keyUpHandler(event):
    global TileSpeedx, TileSpeedy, BallSpeedy, BallSpeedx

    TileSpeedx = 0
    TileSpeedy = 0

def updateBallPosition():

    global Coin, CoinsRadius, ConstantSpeed, ConstantSpeedNegative,Tilex, Tiley, Ballx, Bally, BallSpeedx, BallSpeedy, BallRadius, TileSpeedx, TileSpeedy, coinx, coiny, Coinsx, Coinsy

    if Ballx + 250 >= WIDTH:
        BallSpeedx = ConstantSpeedNegative
    elif Ballx + 50 <= 0:
        BallSpeedx = ConstantSpeed

    if Bally + 50>= Tiley:
        if Ballx   <= Tilex - 100 and Ballx + 150>= Tilex - 50 :
            BallSpeedy = ConstantSpeedNegative

        if Bally + 100 <= Tiley:
            BallSpeedx = ConstantSpeedNegative

    elif Bally - 30 <=0:
       BallSpeedy = ConstantSpeed

    if Tilex + 150>= WIDTH:
        TileSpeedx = ConstantSpeedNegative - 10
    
    elif Tilex - 150 <= 0:
        TileSpeedx = ConstantSpeed + 10

    elif Ballx >= coinx + CoinsRadius and Bally + BallRadius >= coiny + CoinsRadius and Ballx + BallRadius >= coinx:
        print ("heeeee")
        Collided = True
        if Collided == True:
            s.delete(Coins)

        BallSpeedy = ConstantSpeedNegative

    if Bally >= HEIGHT:
        BallSpeedx= 0
        BallSpeedy= 0
        TileSpeedx  =0
        TileSpeedy = 0
        Tilex= (0.50 * WIDTH)
        Tiley= (.90 * HEIGHT)
        Ballx= (.50 * WIDTH)
        Bally= (.80 * HEIGHT)

    Tilex = Tilex + TileSpeedx
    Tiley = Tiley + TileSpeedy
    Ballx = Ballx + BallSpeedx
    print(Ballx, " ", BallSpeedx)
    Bally = Bally + BallSpeedy
    print (Bally, "     ")



    
def getHexValue (x):
    H= ["1","2","3","4","5", "6","7","8","9","A","B","C","D","E","F"]
    hexValue = ""
    while x != 0:
        q = int(x/16)
        r = x % 16
        hexValue = H[r] + hexValue
        x = q

    if hexValue == "":
        return "00"

    elif len(hexValue) == 1:
        return "0" + hexValue

    else:
        return hexValue

def DrawBackground():
   for x in range(0,256):
        rColor = getHexValue(  )
        color = "#FFC0" + rColor

        x = 3 * x + 200
        s.create_oval( 0, x, 1000, x+3, fill = color, outline = color)

def getDistance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def DrawCoins():
    global coinx, coiny, Coinsx, Coinsy, CoinsRadius, CoinsColour, Coins
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
        Colors = choice(["red", "yellow", "green", "blue"])
        Coins = s.create_oval(coinx - CoinsRadius, coiny - CoinsRadius, coinx + CoinsRadius, coiny + CoinsRadius, fill=Colors,
                         outline= Colors)

def DrawObject():
    global Ball, Tile, Tile1, Ball1, s
    Ball1  = PhotoImage(file = "fishthenet.gif")
    Ball = s.create_image(Ballx, Bally, image = Ball1)
    Tile1 = PhotoImage(file = "boat.gif")
    Tile =  s.create_image(Tilex, Tiley, image = Tile1)

def runGame():
    global startMessage, gameRunning, backToIntroButton, Coins, LevelButton, gameMode

    if state == INTRO:
        drawIntroScreen()
    elif state == PLAY:
        play_game()
    elif state == INST:
        pass

    #setInitialValues()
    #DrawCoins()
    s.update()
    sleep(0.03)
    #s.delete(startMessage)

    #gameMode = "Easy"
    #LevelButton()
    #setInitialValues()
    #DrawObject()
    #updateBallPosition()
    #endGame()

    #runGame()

    #s.update()
    #sleep(0.01)
    #s.delete(Tile, Ball, Coins)


def main():
    global tk, s, state

    state = INTRO
    tk = Tk()

    s = Canvas(tk, width=WIDTH, height=HEIGHT, background="black")
    s.pack()

    s.bind("<Key>", keyDownHandler)
    s.bind("<KeyRelease>", keyUpHandler)

    tk.after(0, runGame)
    s.pack()
    s.focus_set()
    tk.mainloop()

if __name__ == '__main__':
    main()
