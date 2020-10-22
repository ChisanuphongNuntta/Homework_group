import pgzrun
from random import randint, choice,random
import string
from vocabulary import *
WIDTH = 1000
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# LETTER = {"letter": "", "x": 0, "y": 0}
ON_SCREEN_LETTERS = []
VELOCITY = 1
SCORE = {"RIGHT": 0, "WRONG": 0}
inter = 0
stop = 0
pu2 = 0
b = 0
reply = 0
toyo = Actor('play')
toyo.pos = (500,300)
pu = Actor('pause')
pu.pos = (50,50)
back = Actor('backg')
endgame = Actor('end')
replaygame = Actor('replay')
resumegame = Actor('resume')
backbub = Actor('backbub')
eazy = Actor('eazy')
eazy.pos = (500,100)
medium = Actor('medium')
medium.pos = (500,400)
hard = Actor('hard')
hard.pos = (500,500)
eazy2 = 0
medium2 = 0
hard2 = 0
keyin = ''
mm = ''

def draw():
    toyo.draw()
    if inter == 1:
        screen.clear()
        eazy.draw()
        medium.draw()
        hard.draw()
        if eazy2 == 1 or medium2 == 1 or hard2 == 1:
            screen.clear()
            screen.blit('blackground',(0,0))
            pu.draw()
            for LETTER in ON_SCREEN_LETTERS:
                screen.draw.text(LETTER["letter"], (LETTER["x"], LETTER["y"]), fontsize=50, color=WHITE)
            screen.draw.text("RIGHT: " + str(SCORE["RIGHT"]), (WIDTH - 130, 10), fontsize=30, color=WHITE)
            screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 130, 40), fontsize=30, color=WHITE)
            screen.draw.text("TEXT: " + str(keyin), (200, HEIGHT - 50), fontsize=30, color=WHITE)
    if pu2 == 1:
        back.draw()
        back.pos = 500,300
        resumegame.draw()
        resumegame.pos = 500,100
        endgame.draw()
        endgame.pos = 500,300
        replaygame.draw()
        replaygame.pos = 500, 500
        

def on_mouse_down(pos):
    global inter,stop,pu2,b,eazy2,medium2,hard2,ON_SCREEN_LETTERS
    if stop != 1 and inter <= 1:
        if toyo.collidepoint(pos):
            if inter >= 0 and inter < 1:
                print("yes")
                inter += 1
    if eazy2 != 1 and  medium2 != 1 and hard2 != 1:
        if eazy.collidepoint(pos):
            if inter == 1 and eazy2 < 1:
                eazy2 += 1
        if medium.collidepoint(pos):
            if inter == 1 and medium2 < 1:
                medium2 += 1
        if hard.collidepoint(pos):
            if inter == 1 and hard2 < 1:
                hard2 += 1
    if inter == 1:
        if pu.collidepoint(pos):
            if pu2 >= 0 and pu2 < 1:
                pu2 += 1
    if resumegame.collidepoint(pos):
        if inter == 1:
            pu2 -= 1
    if pu2 == 1:
        if replaygame.collidepoint(pos):
            SCORE["RIGHT"] = 0 
            SCORE["WRONG"] = 0
            ON_SCREEN_LETTERS = []
            pu2 -= 1
    
            

def update():
    if inter == 1 and pu2 != 1 and eazy2 == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 1:
            add_letter()
        
    if inter == 1 and pu2 != 1 and medium2 == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 1:
            add_letter()

    if inter == 1 and pu2 != 1 and hard2 == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
        while len(ON_SCREEN_LETTERS) < 1:
            add_letter()

def on_key_down(key, mod, unicode):
    global keyin
    if keyboard.BACKSPACE:
        keyin = keyin[:-1]
    else:
        keyin += unicode

    
    for i,LETTER in enumerate(ON_SCREEN_LETTERS):
        if LETTER["letter"] == keyin:
            SCORE["RIGHT"] += 1
            delete_letter(i)
            keyin = ''
            return

        

def add_letter():
    if inter == 1 and eazy2 == 1:
        letter = choice(string.ascii_letters).lower()
        x = randint(10, WIDTH - 100)
        y = 1
        ON_SCREEN_LETTERS.append({"letter": letter, "x": x, "y": y})
    if inter == 1 and medium2 == 1:
        letter = choice(vocabulary2)
        x = randint(10, WIDTH - 100)
        y = 1
        ON_SCREEN_LETTERS.append({"letter": letter, "x": x, "y": y})
    if inter == 1 and hard2 == 1:
        letter = choice(vocabulary3)
        x = randint(10, WIDTH - 100)
        y = 1
        ON_SCREEN_LETTERS.append({"letter": letter, "x": x, "y": y})


def delete_letter(i):
    del ON_SCREEN_LETTERS[i]
pgzrun.go()