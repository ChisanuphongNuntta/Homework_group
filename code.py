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

VELOCITY = 5
SCORE = {"CORRECT": 0, "WRONG": 0}
inter = 0
stop = 0
pu2 = 0
b = 0
end = 0
reply = 0
play = Actor('play')
play.pos = (500,300)
pu = Actor('pause')
pu.pos = (100,90)
backpuu = Actor('backpu2')
start2 = Actor('start2')
endback = Actor('endback')
endgame = Actor('end')
replaygame = Actor('replay')
resumegame = Actor('resume')
backpu = Actor('backpu')
eazy = Actor('eazy')
eazy.pos = (250,200)
medium = Actor('medium')
medium.pos = (770,200)
hard = Actor('hard')
hard.pos = (540,500)
playagain = Actor('playagain')
playagain.pos = (540,500)
playagain2 = 0
eazy2 = 0
medium2 = 0
hard2 = 0
keyin = ''

if inter <= 0:
    music.play('manu')

def draw():
    global pu2,end
    screen.blit('start2',(0,0))
    play.draw()
    if inter == 1:
        screen.clear()
        screen.blit('backpu',(0,0))
        eazy.draw()
        medium.draw()
        hard.draw()
        if eazy2 == 1 or medium2 == 1 or hard2 == 1:
            screen.clear()
            screen.blit('blackground',(0,0))
            pu.draw()
            for LETTER in ON_SCREEN_LETTERS:
                screen.draw.text(LETTER["letter"], (LETTER["x"], LETTER["y"]), fontsize=50, color=WHITE)
            screen.draw.text("CORRECT: " + str(SCORE["CORRECT"]), (WIDTH - 140, 10), fontsize=30, color=WHITE)
            screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 130, 40), fontsize=30, color=WHITE)
            screen.draw.text("TEXT: " + str(keyin), (200, HEIGHT - 50), fontsize=30, color=WHITE)
    if pu2 == 1:
        screen.clear()
        screen.blit('backpu2',(0,0))
        resumegame.draw()
        resumegame.pos = 540,100
        endgame.draw()
        endgame.pos = 540,300
        replaygame.draw()
        replaygame.pos = 540, 500
    if end == 1:
        screen.clear()
        screen.blit('endback',(0,0))
        playagain.draw()
        screen.draw.text("CORRECT: " + str(SCORE["CORRECT"]), (WIDTH - 570, 200), fontsize=50, color=WHITE)
        screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 550, 300), fontsize=50, color=WHITE)
    if SCORE["WRONG"] == 3:
        pu2 = 1
        end = 1

        

def on_mouse_down(pos):
    global inter,stop,pu2,b,eazy2,medium2,hard2,ON_SCREEN_LETTERS,end,playagain2
    if stop != 1 and inter <= 1:
        if play.collidepoint(pos):
            if inter >= 0 and inter < 1:
                print("Enjoy!")
                inter += 1
                music.play('play')
    if eazy2 != 1 and  medium2 != 1 and hard2 != 1:
        if eazy.collidepoint(pos):
            if inter == 1 and eazy2 < 1:
                eazy2 += 1
                music.play('play')
        if medium.collidepoint(pos):
            if inter == 1 and medium2 < 1:
                medium2 += 1
                music.play('play')
        if hard.collidepoint(pos):
            if inter == 1 and hard2 < 1:
                hard2 += 1
                music.play('play')
    if inter == 1:
        if pu.collidepoint(pos):
            if pu2 >= 0 and pu2 < 1:
                pu2 += 1
                music.play('stop')
    if pu2 == 1:
        if resumegame.collidepoint(pos):
            if inter == 1 and end != 1:
                pu2 -= 1
                music.play('play')
    if pu2 == 1:
        if replaygame.collidepoint(pos):
            if inter == 1 and end != 1:
                SCORE["CORRECT"] = 0 
                SCORE["WRONG"] = 0
                ON_SCREEN_LETTERS = []
                pu2 -= 1
                music.play('play')
    if pu2 == 1:
        if endgame.collidepoint(pos):
            if end >= 0 and end < 1:
                end += 1
                music.play('end')
    if SCORE["WRONG"] == 3 or end == 1:
        if playagain.collidepoint(pos):
            if playagain2 >= 0 and playagain2 < 1:
                if inter == 1:
                    inter = 0
                if end == 1:
                    end -= 1
                    inter += 1
                if pu2 == 1:
                    pu2 -= 1
                if eazy2 == 1:
                    eazy2 = 0
                if medium2 == 1:
                    medium2 = 0
                if hard2 == 1:
                    hard2 = 0
                SCORE["CORRECT"] = 0 
                SCORE["WRONG"] = 0
                ON_SCREEN_LETTERS = []
                music.play('manu')
"""    
def overtime():
    global pu2,end
    end = 1
    pu2 = 1
    music.play('end')
    screen.draw.text("time: " + x, (WIDTH - 130, 40), fontsize=30, color=WHITE)

x = clock.schedule(overtime, 10.0)
"""
            
        
            

def update():
    if inter == 1 and pu2 != 1 and eazy2 == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
                if SCORE["WRONG"] == 3:
                    music.play('end')
        while len(ON_SCREEN_LETTERS) < 1:
            add_letter()
    if inter == 1 and pu2 != 1 and medium2 == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
                if SCORE["WRONG"] == 3:
                    music.play('end')
        while len(ON_SCREEN_LETTERS) < 1:
            add_letter()

    if inter == 1 and pu2 != 1 and hard2 == 1:
        for i, LETTER in enumerate(ON_SCREEN_LETTERS):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 5:
                SCORE["WRONG"] += 1
                delete_letter(i)
                if SCORE["WRONG"] == 3:
                    music.play('end')
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
            SCORE["CORRECT"] += 1
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
