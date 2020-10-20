import pgzrun
from random import randint, choice, random
import string

WIDTH = 800
HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#NUMSA = ["birde","cat","rad"]
# LETTER = {"letter": "", "x": 0, "y": 0}
ON_SCREEN_LETTERS = []
VELOCITY = 3
SCORE = {"RIGHT": 0, "WRONG": 0}
inter = 0
stop = 0
toyo = Actor('play',(400,250))
st = Actor('stop')


def draw():
    toyo.draw()
    if inter == 1:
        screen.clear()
        screen.blit('blackground',(0,0))
        st.draw()
        for LETTER in ON_SCREEN_LETTERS:
            screen.draw.text(LETTER["letter"], (LETTER["x"], LETTER["y"]), fontsize=50, color=WHITE)
        screen.draw.text("RIGHT: " + str(SCORE["RIGHT"]), (WIDTH - 130, 10), fontsize=30, color=WHITE)
        screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 130, 40), fontsize=30, color=WHITE)
    if stop == 1:
        screen.clear()
        

def on_mouse_down(pos):
    global inter
    global stop
    if toyo.collidepoint(pos):
        print("yes")
        inter += 1
    if st.collidepoint(pos):
        print("stop")
        stop += 1
        print(stop)
        

def update():
    if inter == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 5:
            add_letter()
    if stop == 1:
        screen.clear()
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 0:
            add_letter()


def on_key_down(key, mod, unicode):
    if unicode:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            if LETTER["letter"] == unicode:
                SCORE["RIGHT"] += 1
                delete_letter(i)
                return
        else:
            SCORE["WRONG"] += 1


def add_letter():
    letter = choice(string.ascii_letters).lower()
    x = randint(10, WIDTH - 5)
    y = 3
    ON_SCREEN_LETTERS.append({"letter": letter, "x": x, "y": y})


def delete_letter(i):
    del ON_SCREEN_LETTERS[i]
    add_letter()


pgzrun.go()