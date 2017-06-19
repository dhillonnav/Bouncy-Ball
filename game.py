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

    bac_img = PhotoImage(file="back1.gif")
    background = screen.create_image(0.5 * WIDTH, 0.4 * HEIGHT, image=bac_img)

    start_message = screen.create_text((0.35 * WIDTH), (0.05 * WIDTH), text="Rescue The Fish", font="Times 38",
                                       fill="red", anchor=W)

    play_button = Button(tk, text="Play", font="Times 30", command=playPressed, anchor=CENTER)
    play_button.pack()
    play_button.place(x=(0.5 * WIDTH), y=(0.35 * HEIGHT))

    instruction_label = Button(tk, text="Instructions", command=instPressed, font="Times 30")
    instruction_label.pack()
    instruction_label.place(x=(0.44 * WIDTH), y=(0.50 * HEIGHT))
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
    back_to_intro_button.place(x=(0.05 * WIDTH), y=(0.05 * HEIGHT))
    instructions= screen.create_text(500,100, text= "Instructions", font= "Times 40")
    message= screen.create_text(500, 650, text= "Have Fun !!!", font= "Times 40")


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
    easy_level_button.place(x=(0.5 * WIDTH), y=(0.35 * HEIGHT))

    medium_level_button = Button(tk, text="Medium", command=mediumButton, font="Times 30")
    medium_level_button.pack()
    medium_level_button.place(x=(0.5 * WIDTH), y=(0.50 * HEIGHT))

    hard_level_button = Button(tk, text="Hard", command=hardButton, font="Times 30")
    hard_level_button.pack()
    hard_level_button.place(x=(0.5 * WIDTH), y=(0.65 * HEIGHT))

    back_to_intro_button = Button(tk, text="Back", font="Times 25", command=backToIntroButton, anchor=CENTER)
    back_to_intro_button.pack()
    back_to_intro_button.place(x=(0.1 * WIDTH), y=(0.05 * HEIGHT))


def setInitialValues(level):
    global time_value, time, timer_x, timer_y, detect, leftShark, sharks_y2, sharksy2,sharks2_speedx, sharks2, sharksx2,sharks_pic2, sharks, sharksx, sharks_x, sharks_y, sharksy, sharks_pic, sharks_speedx, sharks_speedy, ball_launched, ball_x, ball_y, ball_speedx, ball_speedy, ball_colour, ball_radius, constant_speed_inc, tile_x, tile_y, \
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
    sharks_y=[]
    sharks_y2= []
    leftShark= False
    sharks= []
    sharks2 = []
    sharks_pic = PhotoImage(file="sharks.gif")
    sharks_pic2 = PhotoImage(file="shark2.gif")
    fishx= 500
    sharksx = WIDTH / 2
    detect= False
    fishy= 50
    # game variables
    game_running = True
    collided = False
    WinMessage = 0
    gameRunning = True
    time = 60
    timer_x= 850
    timer_y= 0
    if level == EASY:
        sharks_speedy = 0
        tile_speedx = 0
        ball_speedx = 0
        ball_speedy = 0
        time_value = 60
        num_sharks = 1
        constant_speed_inc= 20
        for num_Sharks in range( num_sharks):
            sharksy = randint(80, 0.4 * HEIGHT)
            sharksy2 = randint(80, 0.4* HEIGHT)
            sharks_y.append(sharksy)
            sharks_y2 .append(sharksy2)
            sharks.append(0)
            sharks2.append(0)

    elif level == MEDIUM:
        sharks_speedx = 0
        sharks_speedy = 0
        tile_speedx = 0
        tile_speedy = 0
        ball_speedx = 0
        ball_speedy = 0
        sharks2_speedx= 0
        constant_speed_inc = 15
        time_value= 50
        num_sharks  = 2
        for num_Sharks in range(num_sharks):
            sharksy = randint(80, 0.4 * HEIGHT)
            sharks_y.append(sharksy)
            sharks.append(0)
            sharks2.append(0)

    elif level == HARD:
        sharks_speedx = 0
        sharks_speedy = 0
        tile_speedx = 0
        tile_speedy = 0
        ball_speedx = 0
        ball_speedy = 0
        time_value= 40
        num_sharks = 3
        constant_speed_inc = 10
        for num_Sharks in range(num_sharks):
            sharksy = randint(80, 0.4 * HEIGHT)
            while sharksy >= fishy:
                sharks_y.append(sharksy)
                sharks.append(0)
                sharks2.append(0)


def drawObject():
    global ball, tile, ball_pic, tile_pic, timer, timer_text, time_text
    ball_pic = PhotoImage(file="fishthenet.gif")
    ball = screen.create_image(ball_x, ball_y, image=ball_pic)
    tile_pic = PhotoImage(file = "boat.gif")
    tile = screen.create_image(tile_x, tile_y, image=tile_pic)
    timer= screen.create_rectangle(timer_x, timer_y, timer_x + 100, timer_y +50, fill="hot pink", outline= "hot pink")
    timer_text= screen.create_text(timer_x + 50, timer_y+ 70, text= "Time", font= "Times 20")
    time_text= screen.create_text(timer_x+25, timer_y+ 25, text= int(time_value), font= "times 25")
    screen.delete(background)
    screen.update()
    sleep(0.03)

def main_fish():
    global fish_pic, fish
    fish_pic = PhotoImage(file="fish.gif")
    fish = screen.create_image(fishx, fishy, image=fish_pic)

def DrawSharks():
    global sharks, sharks2

    for i in range (num_sharks):
        sharks[i] = screen.create_image(sharksx, sharks_y[i], image=sharks_pic)
        if leftShark == True:
                screen.delete(sharks[i])
                sharks2[i] = screen.create_image(sharksx, sharks_y[i], image=sharks_pic2)

def deleteSharks():
    global sharks, sharks2
    for i in range(num_sharks):
        screen.delete(sharks[i], sharks2[i])


def detectColision():
    global fish
    if leftShark and ball_x >= sharksx - 90 and ball_y >= sharksx - 90 + 183:
        print("Collided")
        screen.delete(fish)

def updateBallPosition():
    global fish, sharks, leftShark, sharksx2, sharks2_speedx, sharksx, sharks_speedy, sharks_speedx,  tile_x, tile_y, ball_x, ball_y, ball_speedx, ball_speedy, tile_speedx, tile_speedy

    if ball_x + 250 >= WIDTH:
        ball_speedx = -constant_speed_inc

    elif ball_x + 100 <= 0:
        ball_speedx = constant_speed_inc

    elif ball_y - 70 <= 0:
        ball_speedy = constant_speed_inc

    if ball_y + 50 >= tile_y:
        if ball_x <= tile_x-20  and ball_x + 150 >= tile_x - 100 :
            ball_speedy -= constant_speed_inc

    if tile_x + 170 >= WIDTH:
        tile_speedx = -constant_speed_inc

    elif tile_x - 160 <= 0:
        tile_speedx = constant_speed_inc

    # elif ball_x >= sharksx and ball_y >= sharksy and ball_x >= sharksx:
    #         screen.delete(fish)

    if sharksx - 91 <= 0:
        leftShark = True

    if sharksx + 91 >= WIDTH:
        leftShark = False

    # if ball_y - 70 <= sharksy:
    #     screen.delete(sharks)

    if leftShark:
        sharks_speedx = constant_speed_inc
    else:
        sharks_speedx = -constant_speed_inc

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


def endGame():
    global fish, ball, tile, text, time_text, time_text, timer
    if time_value <= 0:
        screen.delete(time_text)
        tryAgain_Button()
        text = screen.create_text(0.57*WIDTH, 0.1*HEIGHT, text="Thanks for Playing!!!", font="Times 30", fill= "red")
        screen.delete(ball, tile, fish)

def tryAgain_pressed():
    global text
    prePlayScreen()
    screen.delete(text, timer, time_text)
    try_again_button.destroy()
    quit_game_button.destroy()

def tryAgain_Button():
    setInitialValues(tryagain)
    global  try_again_button, quit_game_button
    try_again_button = Button(tk, text="Try Again", font="Times 25", command= tryAgain_pressed, anchor=CENTER)
    try_again_button.pack()
    try_again_button.place(x=(0.45 * WIDTH), y=(0.3 * HEIGHT))

    setInitialValues(quitgame)
    quit_game_button = Button(tk, text="Quit Game", font="Times 25", command= tk.destroy, anchor=CENTER)
    quit_game_button.pack()
    quit_game_button.place(x=(0.45 * WIDTH), y=(0.55 * HEIGHT))


def playScreen():
    global time_value
    while True:
        time_value -= 0.2
        DrawSharks()
        main_fish()
        drawObject()
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
