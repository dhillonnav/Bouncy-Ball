from math import *
from tkinter import *
from random import *
from time import *


# game constants
WIDTH = 1200
HEIGHT = 750
PLAY = 0
INST = 1
INTRO = 2
EASY = 3
MEDIUM = 4
HARD = 5
tryagain = 6
quitgame= 7


def playPressed():
    state = PLAY
    prePlayScreen()


def instPressed():
    state = INST
    instructionScreen()


def introScreen():
    global background, start_message, play_button, instruction_label, bac_img

    bac_img = PhotoImage(file="back.gif")
    background = screen.create_image(0.5 * WIDTH, 0.4 * HEIGHT, image=bac_img)

    start_message = screen.create_text((0.35 * WIDTH), (0.05 * WIDTH), text="Finding NEMO", font="Times 48",
                                       fill="Orange", anchor=W)

    play_button = Button(tk, text="Play", font="Times 30", command=playPressed, anchor=CENTER)
    play_button.pack()
    play_button.place(x=(0.2 * WIDTH), y=(0.5 * HEIGHT))

    instruction_label = Button(tk, text="Instructions", command=instPressed, font="Times 30")
    instruction_label.pack()
    instruction_label.place(x=(0.15 * WIDTH), y=(0.60 * HEIGHT))
    screen.delete(instructions, message)
    back_to_intro_button.destroy()


def instructionScreen():

    global instructions, keys, message, keys_pic, back_to_intro_button, game_pic, game
    play_button.destroy()
    keys_pic = PhotoImage(file="keys.gif")
    keys = screen.create_image(0.2 * WIDTH, 0.5 * HEIGHT, image=keys_pic)
    game_pic = PhotoImage(file="game.gif")
    game = screen.create_image(0.7 * WIDTH, 0.5 * HEIGHT, image=game_pic)
    instruction_label.destroy()
    screen.delete(start_message,background)
    back_to_intro_button = Button(tk, text="Back", font="Times 25", command= inst_pre_play, anchor=CENTER)
    back_to_intro_button.pack()
    back_to_intro_button.place(x=(0.1 * WIDTH), y=(0.05 * HEIGHT))
    instructions= screen.create_text(500,100, text= "Instructions", font= "Times 40", fill= "orange")
    message= screen.create_text(500, 650, text= "Have Fun !!!", font= "Times 40", fill= "orange")


def delete_pre_play():
    easy_level_button.destroy()
    medium_level_button.destroy()
    hard_level_button.destroy()
    back_to_intro_button.destroy()


def inst_pre_play():
    global keys
    screen.delete(instructions, message)
    introScreen()
    screen.delete(keys, game)
    delete_pre_play()
    back_to_intro_button.destroy()
    screen.delete(keys)

def easyButton():
    setInitialValues(EASY)
    delete_pre_play()
    playScreen()
    screen.delete(instructions)


def mediumButton():
    setInitialValues(MEDIUM)
    delete_pre_play()
    playScreen()
    screen.delete(instructions)


def hardButton():
    setInitialValues(HARD)
    delete_pre_play()
    playScreen()
    screen.delete(instructions)


def backToIntroButton():
    state = INTRO
    delete_pre_play()
    introScreen()


def prePlayScreen():
    global easy_level_button, medium_level_button, hard_level_button, back_to_intro_button, try_again_button

    # delete previous buttons
    instruction_label.destroy()
    play_button.destroy()
    screen.delete(start_message)

    # draw new buttons
    easy_level_button = Button(tk, text="Easy", command=easyButton, font="Times 30")
    easy_level_button.pack()
    easy_level_button.place(x=(0.2 * WIDTH), y=(0.35 * HEIGHT))

    medium_level_button = Button(tk, text="Medium", command=mediumButton, font="Times 30")
    medium_level_button.pack()
    medium_level_button.place(x=(0.2 * WIDTH), y=(0.50 * HEIGHT))

    hard_level_button = Button(tk, text="Hard", command=hardButton, font="Times 30")
    hard_level_button.pack()
    hard_level_button.place(x=(0.2 * WIDTH), y=(0.65 * HEIGHT))

    back_to_intro_button = Button(tk, text="Back", font="Times 25", command=backToIntroButton, anchor=CENTER)
    back_to_intro_button.pack()
    back_to_intro_button.place(x=(0.1 * WIDTH), y=(0.05 * HEIGHT))


def setInitialValues(level):
    global sheldon_pic, sheldon,sheldonx, sheldony,sheldon_y,leftShark_3, turtle,turtle_y, turtlex, turtle_pic, medium, hard, collided3, sharksx3,sharksy3, sharks_y3, sharks3, sharks_3, shark_constant_inc, collided_2, orientation,sharks_1,sharks_2, collided, time_value, time, timer_x, timer_y, detect, leftShark, sharks_y2, sharksy2,sharks2_speedx, sharks2, sharksx2,sharks_pic2, sharks, sharksx, sharks_x, sharks_y, sharksy, sharks_pic, sharks_speedx, sharks_speedy, ball_launched, ball_x, ball_y, ball_speedx, ball_speedy, ball_colour, ball_radius, constant_speed_inc, tile_x, tile_y, \
        tile_speedx, tile_speedy, tile_width, tile_height, coins_x, coins_y, num_sharks, game_running, fishx, fishy

    # ball variables
    ball_colour = "black"
    ball_x = (.45 * WIDTH)
    ball_y = (.82 * HEIGHT)
    ball_radius = 57
    ball_launched= False

    # tile variables
    tile_width = (0.2 * WIDTH)
    tile_height = (0.15 * HEIGHT)
    tile_x = (.45 * WIDTH)
    tile_y = (.87 * HEIGHT)

    # coins variables
    medium = False
    hard= False
    collided3= False
    sharks_y=[]
    sharks_y2= []
    sharks_y3= []
    leftShark= False
    leftShark_3= False
    sharks= []
    sheldon= []
    sheldonx= WIDTH
    sheldon_y= []
    orientation= ["left_shark", "right_shark"]
    sharks3= []
    sharks_3= []
    sharks2 = []
    sharks_2= []
    sharks_1= []
    turtle_pic= PhotoImage(file= "tutu.gif")
    sharks_pic = PhotoImage(file="sharks.gif")
    sharks_pic2= PhotoImage(file= "shark2.gif")
    sheldon_pic = PhotoImage(file="sheldon.gif")
    fishx= 0.5*WIDTH
    fishy = 0.05 * HEIGHT
    turtlex= 0
    turtle_y= []
    turtle= []
    sharksx = WIDTH
    sharksx2= 20
    sharksx3= 800
    detect= False
    collided = False
    collided_2= False
    time = 60
    timer_x= 0.9 * WIDTH
    timer_y= 0
    if level == EASY:
        sharks_speedy = 0
        tile_speedx = 0
        ball_speedx = 0
        ball_speedy = 0
        time_value = 60
        num_sharks = 1
        shark_constant_inc= 20
        constant_speed_inc= 20
        for num_Sharks in range( num_sharks):
            sharksy = randint(0.2*HEIGHT, 0.3 * HEIGHT)
            sharksy2 = randint(0.3*HEIGHT, 0.5* HEIGHT)
            sharks_y.append(sharksy)
            sharks_y2 .append(sharksy2)
            sharksy3 = randint(0.4 * HEIGHT, 0.5 * HEIGHT)
            sharks_y3.append(sharksy3)
            sharks_3.append(0)
            sharks3.append(0)
            sharks.append(0)
            sharks_2.append(0)
            sharks2.append(0)
            sharks_1.append(0)
            sharksx3 = +8000

    elif level == MEDIUM:
        medium = True
        sharks_speedy = 0
        tile_speedx = 0
        tile_speedy = 0
        ball_speedx = 0
        ball_speedy = 0
        shark_constant_inc= 25
        constant_speed_inc = 15
        time_value= 50
        num_sharks  = 1
        for num_Sharks in range(num_sharks):
            sharksy = randint(0.2*HEIGHT, 0.3 * HEIGHT)
            sharksy2 = randint(0.3*HEIGHT, 0.4 * HEIGHT)
            sheldony = randint(0.5 * HEIGHT, 0.6 * HEIGHT)
            sheldon.append(0)
            sheldon_y.append(sheldony)
            sharks_y.append(sharksy)
            sharks_y2.append(sharksy2)
            sharks.append(0)
            sharks2.append(0)
            sharks_1.append(0)
            sharks_2.append(0)


    elif level == HARD:
        hard = True
        sharks_speedx = 55
        sharks_speedy = 0
        tile_speedx = 0
        tile_speedy = 0
        ball_speedx = 0
        ball_speedy = 0
        time_value= 40
        num_sharks = 1
        shark_constant_inc= 30
        constant_speed_inc = 10
        for num_Sharks in range( num_sharks):
            sharksy = randint(0.2*HEIGHT, 0.3 * HEIGHT)
            sharksy2 = randint(0.5*HEIGHT, 0.6* HEIGHT)
            sheldony = randint(0.3 * HEIGHT, 0.5 * HEIGHT)
            sheldon.append(0)
            sheldon_y.append(sheldony)
            sharks_y.append(sharksy)
            sharks_y2 .append(sharksy2)
            sharksy3 = randint(0.4 * HEIGHT, 0.5 * HEIGHT)
            sharks_y3.append(sharksy3)
            sharks_3.append(0)
            sharks3.append(0)
            sharks.append(0)
            sharks_2.append(0)
            sharks2.append(0)
            sharks_1.append(0)
            sharksx3 = +8000
            turtley = randint(0.5 * HEIGHT, 0.6 * HEIGHT)
            turtle_y.append(turtley)
            turtle.append(0)

def countDown():
    global count, background
    screen.delete(background)
    for i in range(3, -1, -1):
        if i == 0:
            count= screen.create_text(0.5*WIDTH, 0.5*HEIGHT, text= "Ready...Set...Save Dory", font= "Times, 70", fill= "red")
        else:
            count= screen.create_text(0.5*WIDTH, 0.5 *HEIGHT, text= i, font="Times, 70", fill= "red")
        screen.update()
        sleep(1)
        screen.delete(count)

def drawObject():
    global ball, tile, ball_pic, tile_pic, timer, timer_text, time_text
    ball_pic = PhotoImage(file="net.gif")
    ball = screen.create_image(ball_x, ball_y, image=ball_pic)
    tile_pic = PhotoImage(file = "boat.gif")
    tile = screen.create_image(tile_x, tile_y, image=tile_pic)
    timer= screen.create_rectangle(timer_x, timer_y, timer_x + 110, timer_y +50, fill="hot pink", outline= "hot pink")
    timer_text= screen.create_text(timer_x + 70, timer_y+ 70, text= "Time", font= "Times 20")
    time_text= screen.create_text(timer_x+50, timer_y+ 25, text= int(time_value), font= "times 25")
    screen.delete(background)
    sleep(0.03)

def drawSheldon():
    global sheldonx
    if medium == True:
        for i in range(num_sharks):
            sheldon[i] = screen.create_image(sheldonx, sheldony,image= sheldon_pic)
            screen.update()
            screen.delete(sheldon[i])


def main_fish():
    global fish_pic, fish
    fish_pic = PhotoImage(file="nemo1.gif")
    fish = screen.create_image(fishx, fishy, image=fish_pic)

def DrawSharks():
    global  ball_y,turtlex,turtle, turtle_y, sharks, sharks2, sharksx, collided, num_sharks, sharks_1, sharksx2, sharks_2, orientation

    for i in range (num_sharks):
        sharks[i] = screen.create_image(sharksx, sharks_y[i], image=sharks_pic)
        sharks_2[i] = screen.create_image(sharksx2, sharks_y2[i], image=sharks_pic2)

        if leftShark == True:
            screen.delete(sharks[i], sharks_2[i])
            sharks2[i] = screen.create_image(sharksx, sharks_y[i], image=sharks_pic2)
            sharks_1[i] = screen.create_image(sharksx2, sharks_y2[i], image=sharks_pic)

        if hard == True:
            turtle[i]= screen.create_image(turtlex, turtle_y[i], image= turtle_pic)
            sheldon[i] = screen.create_image(sheldonx, sheldony, image=sheldon_pic)
            screen.update()
            screen.delete(sheldon[i])
            if turtlex >= WIDTH:
                turtlex =  0
                print (turtlex)
            if ball_y - 50 <= turtle_y[i]:
                turtlex= -5555
                ball_y = ball_y + constant_speed_inc-10
                screen.delete(turtle)



def deleteSharks():
    global sharks, sharks2, sharks_1, sharks_2
    for i in range(num_sharks):
        screen.delete(sharks[i], sharks2[i], sharks_1[i], sharks_2[i])

def detectColision():
    global collided3, sharks3, fish, collided, num_sharks, sharksx, sharksx2, sharksx3, sharks_speedx, leftShark, collided_2, ball_speedy






    if ball_y- 50 <= sharksy:
        if ball_x <= sharksx:
            collided_2 = True

    if ball_y  - 50 <= sharksy2 :
        if ball_x <= sharksx2:
            collided = True
    else:
        collided = False


    if collided == True:
        sharksx2 = -88500
        ball_speedy = + shark_constant_inc

    if collided_2 == True:
        sharksx = + 88850


def updateBallPosition():
    global sheldonx, turtlex,fish, sharks, leftShark3, leftShark, sharksx2, sharksx3, sharks2_speedx, sharksx, sharks_speedy, sharks_speedx,  tile_x, tile_y, ball_x, ball_y, ball_speedx, ball_speedy, tile_speedx, tile_speedy

    if ball_x + 50 >= WIDTH:
        ball_speedx = -constant_speed_inc

    elif ball_x - 50 <= 0:
        ball_speedx = constant_speed_inc

    elif ball_y - 50 <= 0:
        ball_speedy = constant_speed_inc

    if ball_y + 50 >= tile_y:
        if ball_x <= tile_x-20  and ball_x + 50 >= tile_x - 100 :
            ball_speedy -= constant_speed_inc

    if tile_x + 170 >= WIDTH:
        tile_speedx = -constant_speed_inc

    elif tile_x - 160 <= 0:
        tile_speedx = constant_speed_inc

    if sharksx - 91 <= 0:
        leftShark = True

    if sharksx + 91 >= WIDTH:
        leftShark = False

    if sharksx2 + 91 >= WIDTH:
            leftShark= True


    if sheldonx <= 10:
        sheldonx= WIDTH

    if ball_y <= sheldony:
        sheldonx = 8555
        ball_y = ball_y - constant_speed_inc


    if leftShark:
        sharks_speedx = shark_constant_inc
    else:
        sharks_speedx = -shark_constant_inc

    if ball_y >= HEIGHT:
        ball_speedx = 0
        ball_speedy = 0
        tile_speedx = 0
        tile_speedy = 0
        tile_x = (0.45 * WIDTH)
        tile_y = (.87 * HEIGHT)
        ball_x = (.45 * WIDTH)
        ball_y = (.82 * HEIGHT)

    tile_x = tile_x + tile_speedx
    ball_x = ball_x + ball_speedx
    ball_y = ball_y + ball_speedy
    sharksx = sharksx + sharks_speedx
    sharksx2 = sharksx2 - sharks_speedx
    sheldonx= sheldonx - constant_speed_inc
    turtlex= turtlex + constant_speed_inc
    screen.delete(turtle)


def endGame():
    global fish, ball, tile, text, time_text, time_text, timer
    if time_value <= 0:
        screen.delete(time_text)
        tryAgain_Button()
        text = screen.create_text(0.5*WIDTH, 0.15*HEIGHT, text="Thanks for Playing!!!", font="Times 40", fill= "blue")
        screen.delete(ball, tile, fish)

    elif collided_2 == True:
        screen.delete(time_text)
        tryAgain_Button()
        text = screen.create_text(0.5 * WIDTH, 0.1 * HEIGHT, text="You Found NEMO!!!", font="Times 40", fill="Blue")
        screen.delete(ball, tile, fish)

def tryAgain_pressed():
    global text
    prePlayScreen()
    screen.delete(text, timer, time_text, nemo)
    try_again_button.destroy()
    quit_game_button.destroy()

def tryAgain_Button():
    setInitialValues(tryagain)
    global  try_again_button, quit_game_button, nemo, nemo_pic
    nemo_pic = PhotoImage(file="nemo.gif")
    nemo = screen.create_image(0.5*WIDTH, 0.45*HEIGHT, image=nemo_pic)
    try_again_button = Button(tk, text="Try Again", font="Times 25", command= tryAgain_pressed, anchor=CENTER)
    try_again_button.pack()
    try_again_button.place(x=(0.45 * WIDTH), y=(0.4 * HEIGHT))

    setInitialValues(quitgame)
    quit_game_button = Button(tk, text="Quit Game", font="Times 25", command= tk.destroy, anchor=CENTER)
    quit_game_button.pack()
    quit_game_button.place(x=(0.45 * WIDTH), y=(0.55 * HEIGHT))


def playScreen():
    global time_value
    countDown()
    while True:
        time_value -= 0.2
        DrawSharks()
        main_fish()
        drawObject()
        drawSheldon()
        updateBallPosition()
        deleteSharks()
        detectColision()
        endGame()


def runGame():
    # based on states go to different screens
    if state == INTRO:
        introScreen()
    elif state == INST:
        pass
    elif state == PLAY:
        playScreen()

    screen.update()
    sleep(0.03)

def keyPressedHandler(event):
    global ball_speedy, ball_speedx, tile_speedx, tile_speedy, ball_launched, sharks_speedx
    if event.keysym == "Left":
        tile_speedx = - constant_speed_inc

    elif event.keysym == "Right":
        tile_speedx = constant_speed_inc

    elif event.keysym == "Up" and not ball_launched:
        ball_speedx = - constant_speed_inc
        ball_speedy = - constant_speed_inc

    updateBallPosition()

def keyReleasedHandler(event):
    global tile_speedx, tile_speedy, ball_speedx, ball_speedy
    tile_speedx = 0
    tile_speedy = 0

def main():
    global tk, screen, state
    state = INTRO
    tk = Tk()
    screen = Canvas(tk, width=WIDTH, height=HEIGHT, background="skyBlue")
    tk.after(0, runGame)
    screen.bind("<Key>", keyPressedHandler)
    screen.bind("<KeyRelease>", keyReleasedHandler)
    screen.pack()
    screen.focus_set()
    tk.mainloop()

if __name__ == '__main__':
    main()
