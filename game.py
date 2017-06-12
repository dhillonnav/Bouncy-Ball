from math import *
from tkinter import *
from random import *
from time import *

# game constants
WIDTH = 1000
HEIGHT = 750
PLAY = 0
INST = 1
INTRO = 2
EASY = 3
MEDIUM = 4
HARD = 5


def playPressed():
    state = PLAY
    prePlayScreen()


def instPressed():
    state = INST
    instructionScreen()


def introScreen():
    global background, start_message, play_button, instruction_label, bac_img

    bac_img = PhotoImage(file="back1.gif")
    background = screen.create_image(500, 400, image=bac_img)

    start_message = screen.create_text((0.35 * WIDTH), (0.05 * WIDTH), text="Rescue The Fish", font="Times 38",
                                       fill="red", anchor=W)

    play_button = Button(tk, text="Play", font="Times 30", command=playPressed, anchor=CENTER)
    play_button.pack()
    play_button.place(x=(0.45 * WIDTH), y=(0.35 * HEIGHT))

    instruction_label = Button(tk, text="Instructions", command=instPressed, font="Times 30")
    instruction_label.pack()
    instruction_label.place(x=(0.40 * WIDTH), y=(0.50 * HEIGHT))


def instructionScreen():
    play_button.destroy()
    instruction_label.destroy()
    screen.delete(start_message,background)
    screen.create_text(500,100, text= "Instructions", font= "Times 40")


def delete_pre_play():
    easy_level_button.destroy()
    medium_level_button.destroy()
    hard_level_button.destroy()
    back_to_intro_button.destroy()


def easyButton():
    setInitialValues(EASY)
    delete_pre_play()
    playScreen()


def mediumButton():
    setInitialValues(MEDIUM)
    delete_pre_play()
    playScreen()


def hardButton():
    setInitialValues(HARD)
    delete_pre_play()
    playScreen()


def backToIntroButton():
    state = INTRO
    delete_pre_play()
    introScreen()


def prePlayScreen():
    global easy_level_button, medium_level_button, hard_level_button, back_to_intro_button

    # delete previous buttons
    instruction_label.destroy()
    play_button.destroy()
    screen.delete(start_message)

    # draw new buttons
    easy_level_button = Button(tk, text="Easy", command=easyButton, font="Times 30")
    easy_level_button.pack()
    easy_level_button.place(x=(0.45 * WIDTH), y=(0.35 * HEIGHT))

    medium_level_button = Button(tk, text="Medium", command=mediumButton, font="Times 30")
    medium_level_button.pack()
    medium_level_button.place(x=(0.425 * WIDTH), y=(0.50 * HEIGHT))

    hard_level_button = Button(tk, text="Hard", command=hardButton, font="Times 30")
    hard_level_button.pack()
    hard_level_button.place(x=(0.45 * WIDTH), y=(0.65 * HEIGHT))

    back_to_intro_button = Button(tk, text="Back", font="Times 25", command=backToIntroButton, anchor=CENTER)
    back_to_intro_button.pack()
    back_to_intro_button.place(x=(0.05 * WIDTH), y=(0.05 * HEIGHT))


def setInitialValues(level):
    global ball_launched, ball_x, ball_y, ball_speedx, ball_speedy, ball_colour, ball_radius, constant_speed_inc, tile_x, tile_y, \
        tile_speedx, tile_speedy, tile_width, tile_height, coins_x, coins_y, coins_colour, coins_radius, game_running

    # ball variables
    ball_colour = "black"
    ball_x = (.45 * WIDTH)
    ball_y = (.82 * HEIGHT)
    ball_radius = 57
    constant_speed_inc = 15
    ball_launched= False

    # tile variables
    tile_width = (0.2 * WIDTH)
    tile_height = (0.15 * HEIGHT)
    tile_x = (.45 * WIDTH)
    tile_y = (.87 * HEIGHT)

    # coins variables
    coins_x = []
    coins_y = []
    coins_colour = []
    coins_radius = 23

    # game variables
    game_running = True
    collided = False
    WinMessage = 0
    gameRunning = True

    if level == EASY:
        tile_speedx = 0
        tile_speedy = 0
        ball_speedx = 0
        ball_speedy = 0
    elif level == MEDIUM:
        tile_speedx = 0
        tile_speedy = 0
        ball_speedx = 0
        ball_speedy = 0
    elif level == HARD:
        tile_speedx = 0
        tile_speedy = 0
        ball_speedx = 0
        ball_speedy = 0


def drawObject():
    global ball, tile, ball_pic, tile_pic

    ball_pic = PhotoImage(file="fishthenet.gif")
    ball = screen.create_image(ball_x, ball_y, image=ball_pic)
    tile_pic = PhotoImage(file = "boat.gif")
    tile = screen.create_image(tile_x, tile_y, image=tile_pic)
    screen.delete(background)
    screen.update()
    sleep(0.03)

def getDistance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def DrawCoins():
    global coinx, coiny, Coins
    for m in range(15):
        distance_right = False
        while distance_right == False:
            coinx = randint(0, 1200)
            coiny = randint(0, 300)

            colison = 0

            for i in range(0, len(coins_x)):
                d = getDistance(coins_x[i], coins_y[i], coinx, coiny)

                if d <= 2 * coins_radius:
                    colison = colison + 1

            if colison == 0:
                distance_right = True

        coins_x.append(coinx)
        coins_y.append(coiny)
        coins_colors = choice(["red", "yellow", "green", "blue"])
        Coins = screen.create_oval(coinx - coins_radius, coiny - coins_radius, coinx + coins_radius, coiny + coins_radius, fill=coins_colors,
                         outline= coins_colors)

def updateBallPosition():
    global Coins,  tile_x, tile_y, ball_x, ball_y, ball_speedx, ball_speedy, ball_radius, tile_speedx, tile_speedy

    if ball_x + 250 >= WIDTH:
        ball_speedx += constant_speed_inc

    elif ball_x + 50 <= 0:
        ball_speedx += constant_speed_inc

    if ball_y + 50 >= tile_y:
        if ball_x <= tile_x - 100 and ball_x + 150 >= tile_x - 50:
            ball_speedy += constant_speed_inc

        if ball_y + 100 <= tile_y:
            ball_speedx += constant_speed_inc

    elif ball_y - 30 <= 0:
        ball_speedy += constant_speed_inc

    if tile_x + 150 >= WIDTH:
        tile_speedx += constant_speed_inc - 10

    elif tile_x - 150 <= 0:
        tile_speedx += constant_speed_inc + 10

    elif ball_x >= coinx + coins_radius and ball_y + ball_radius >= coiny + coins_radius and ball_x + ball_radius >= coinx:
        print("heeeee")
        collided = True
        if collided == True:
            screen.delete(Coins)

        ball_speedy = constant_speed_inc

    if ball_y >= HEIGHT:
        ball_speedx = 0
        ball_speedy = 0
        tile_speedx = 0
        tile_speedy = 0
        tile_x = (0.50 * WIDTH)
        tile_y = (.90 * HEIGHT)
        ball_x = (.50 * WIDTH)
        ball_y = (.80 * HEIGHT)

    tile_x = tile_x + tile_speedx
    tile_y = tile_y + tile_speedy
    ball_x = ball_x + ball_speedx
    print(ball_x, " ", ball_speedx)
    ball_y = ball_y + ball_speedy
    print(ball_y, "     ", ball_speedy)

def playScreen():
    print("hello")
    drawObject()
    DrawCoins()
    updateBallPosition()


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
    global ball_speedy, ball_speedx, tile_speedx, tile_speedy, ball_launched
    if event.keysym == "Left":
        print("Left")
        tile_speedx -= constant_speed_inc
        updateBallPosition()

    elif event.keysym == "Right":
        print("Right")
        tile_speedx += constant_speed_inc
        updateBallPosition()

    elif event.keysym == "Up" and not ball_launched:
        print("UP")
        ball_launched = True
        ball_speedy = constant_speed_inc
        ball_speedx = constant_speed_inc
        updateBallPosition()
    #
    # elif event.keysym == "Q" and "q":
    #     print("ddd")
    #     screen.delete(ball, tile)



def keyReleasedHandler(event):
    print("yellow")


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
