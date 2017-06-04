from math import *
from tkinter import *
from random import *
from time import *

tk = Tk()

s = Canvas(tk, width=1200, height=800, background="skyblue")
s.pack()


def setInitialValues():
    global Tilex, Tiley, TileSpeedx, TileSpeedy, TileWidth, TileHeight, Ballx, Bally, BallSpeedx, BallSpeedy, BallRadius, xMouse, yMouse, ballcolour
    ballcolour = "black"
    xMouse = 0
    yMouse = 0
    TileWidth = 200
    TileHeight = 50
    Tilex = 600
    Tiley = 700
    TileSpeedx = 0
    TileSpeedy = 0
    Ballx = 650
    Bally = 650
    BallSpeedx = 0
    BallSpeedy = 0
    BallRadius = 50


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
    global TileSpeedx, TileSpeedy, BallSpeedy, BallSpeedx

    if event.keysym == "Left":
        TileSpeedx = -15


    elif event.keysym == "Right":
        TileSpeedx = 15

    elif event.keysym == "Up":
        BallSpeedy = -15
        BallSpeedx = 15


def keyUpHandler(event):
    global TileSpeedx, TileSpeedy, BallSpeedy, BallSpeedx

    TileSpeedx = 0
    TileSpeedy = 0


        
def updateBallPosition():
    global Tilex, Tiley, Ballx, Bally, BallSpeedx, BallSpeedy, BallRadius, TileSpeedx, TileSpeedy

    if Ballx+BallRadius >= 1200:
        BallSpeedx = -15
    elif Ballx <= 0:
        BallSpeedx = 15
       
        
    if Bally+BallRadius >= Tiley:
        if Ballx + BallRadius  <= Tilex + TileWidth and Ballx + BallRadius >= Tilex  :
            BallSpeedy = -15
    elif Bally <=0:
        BallSpeedy = 15
        
    if Tilex + TileWidth >= 1200:
        TileSpeedx = -15
    
    elif Tilex <= 0:
        TileSpeedx = 15

    if Bally >= 800:
        BallSpeedx= 0
        BallSpeedy= 0
        Ballx= 650
        Bally= 650

    Tilex = Tilex + TileSpeedx
    Tiley = Tiley + TileSpeedy
    Ballx = Ballx + BallSpeedx
    print(Ballx, " ", BallSpeedx)
    Bally = Bally + BallSpeedy
    print (Bally, "     ")
    
   


def DrawObject():
    global Ball, Tile
    Ball = s.create_oval(Ballx, Bally, Ballx + BallRadius, Bally + BallRadius, fill=ballcolour)
    Tile = s.create_rectangle(Tilex, Tiley, Tilex + TileWidth, Tiley + TileHeight, fill="Yellow", outline="Yellow")
    


def runGame():
    setInitialValues()
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
