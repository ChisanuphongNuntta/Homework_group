import pgzrun
from random import randint, choice
import string
import os
import random
from words import words
os.environ["SDL_VIDEO_CENTERED"] = "1"
WIDTH = 1600
HEIGHT = 900
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# LETTER = {"letter": "", "x": 0, "y": 0}
ON_SCREEN_LETTERS1 = []
ON_SCREEN_LETTERS2 = []
ON_SCREEN_LETTERS3 = []
ON_SCREEN_LETTERS4 = []
ON_SCREEN_LETTERS5 = []
ON_SCREEN_LETTERS6 = []
ON_SCREEN_LETTERS7 = []
ON_SCREEN_LETTERS8 = []
ON_SCREEN_LETTERS9 = []
ON_SCREEN_LETTERS10 = []


VELOCITY = 1
VELOCITY2 = 2
VELOCITY3 = 4
SCORE = {"RIGHT": 0, "WRONG": 0}
intafad = 0
stop1 = 0
e = 0
m = 0
h = 0
st = 0
end = 0

black1 = Actor('back1')
black1.pos = (150,100)
apple = Actor('apple')
apple.pos = (600,40)
stop = Actor('stop')
stop.pos = (200,100)
playcon = Actor('playcon')
playcon.pos = (800,230)
endgame = Actor('endgame')
endgame.pos = (800,630)
regame = Actor('regame')
regame.pos = (800,430)
back1 = Actor('back')
back1.pos = (800,450)
easy = Actor('easy')
easy.pos = (800,230)
hard = Actor('hard')
hard.pos = (800,630)
mid = Actor('mid')
mid.pos = (800,430)
playagain = Actor('playagain')
playagain.pos = (500,800)
home = Actor('home')
home.pos = (1000,800)


def draw():  # Pygame Zero draw function
    screen.clear()
    screen.fill(BLACK)
    apple.draw()
    screen.draw.text("PLAY", (600, 40), fontsize=200, color=WHITE)
    screen.draw.text("SCROE", (540, 240), fontsize=200, color=WHITE)
    screen.draw.text("OPTION", (500, 440), fontsize=200, color=WHITE)
    screen.draw.text("QUIT", (600, 640), fontsize=200, color=WHITE)
    if intafad == 1:
        screen.clear()
        back1.draw()
        black1.draw()
        easy.draw()
        mid.draw()
        hard.draw()
        
        if e == 1 or m == 1 or h == 1:

            screen.clear()
            stop.draw()
            for LETTER in ON_SCREEN_LETTERS1:
                screen.draw.text( LETTER["letter"] , (LETTER["x"]  , LETTER["y"]), fontsize=40, color=WHITE)
            for LETTER in ON_SCREEN_LETTERS2:
                screen.draw.text( LETTER["letter"] , (LETTER["x"]  , LETTER["y"]), fontsize=40, color=WHITE)
            for LETTER in ON_SCREEN_LETTERS3:
                screen.draw.text( LETTER["letter"] , (LETTER["x"]  , LETTER["y"]), fontsize=40, color=WHITE)
            for LETTER in ON_SCREEN_LETTERS4:
                screen.draw.text( LETTER["letter"] , (LETTER["x"]  , LETTER["y"]), fontsize=40, color=WHITE)
            for LETTER in ON_SCREEN_LETTERS5:
                screen.draw.text( LETTER["letter"] , (LETTER["x"]  , LETTER["y"]), fontsize=40, color=WHITE)
            if SCORE["RIGHT"] > 2:
                for LETTER in ON_SCREEN_LETTERS6:
                screen.draw.text( LETTER["letter"] , (LETTER["x"]  , LETTER["y"]), fontsize=40, color=WHITE)
            if SCORE["RIGHT"] > 5:
                for LETTER in ON_SCREEN_LETTERS7:
                screen.draw.text( LETTER["letter"] , (LETTER["x"]  , LETTER["y"]), fontsize=40, color=WHITE)
            if SCORE["RIGHT"] > 7:
                for LETTER in ON_SCREEN_LETTERS8:
                screen.draw.text( LETTER["letter"] , (LETTER["x"]  , LETTER["y"]), fontsize=40, color=WHITE)
            if SCORE["RIGHT"] > 9:
                for LETTER in ON_SCREEN_LETTERS9:
                screen.draw.text( LETTER["letter"] , (LETTER["x"]  , LETTER["y"]), fontsize=40, color=WHITE)
            if SCORE["RIGHT"] > 15:
                for LETTER in ON_SCREEN_LETTERS10:
                screen.draw.text( LETTER["letter"] , (LETTER["x"]  , LETTER["y"]), fontsize=40, color=WHITE)
            
            screen.draw.text("RIGHT: " + str(SCORE["RIGHT"]), (WIDTH - 130, 10), fontsize=30, color=WHITE)
            screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 130, 40), fontsize=30, color=WHITE)
    if stop1 == 1:
        back1.draw()
        playcon.draw()
        regame.draw()
        endgame.draw()
    
    if SCORE['WRONG'] >= 3 or end == 5:
        screen.clear()
        screen.draw.text("end: ", (WIDTH - 130, 10), fontsize=30, color=WHITE)
        playagain.draw()
        home.draw()
    
def update():
    global SCORE
    global stop1
    #ระดับง่าย
    if stop1 != 1 and intafad == 1 and e == 1:
        for i1, LETTER in enumerate(ON_SCREEN_LETTERS1):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter1(i1)
        while len(ON_SCREEN_LETTERS1) < 1:
            add_letter1()
    if stop1 != 1 and intafad == 1 and e == 1:
        for i2, LETTER in enumerate(ON_SCREEN_LETTERS2):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter2(i2)
        while len(ON_SCREEN_LETTERS2) < 1:
            add_letter2()
    if stop1 != 1 and intafad == 1 and e == 1:
        for i3, LETTER in enumerate(ON_SCREEN_LETTERS3):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter3(i3)
        while len(ON_SCREEN_LETTERS3) < 1:
            add_letter3()
    if stop1 != 1 and intafad == 1 and e == 1:
        for i4, LETTER in enumerate(ON_SCREEN_LETTERS4):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter4(i4)
        while len(ON_SCREEN_LETTERS4) < 1:
            add_letter4()
    if stop1 != 1 and intafad == 1 and e == 1:
        for i5, LETTER in enumerate(ON_SCREEN_LETTERS5):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter5(i5)
        while len(ON_SCREEN_LETTERS5) < 1:
            add_letter5()
    
    if stop1 != 1 and intafad == 1 and e == 1:
        for i6, LETTER in enumerate(ON_SCREEN_LETTERS6):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter6(i6)
        while len(ON_SCREEN_LETTERS5) < 1:
            add_letter6()
    
    if stop1 != 1 and intafad == 1 and e == 1:
        for i7, LETTER in enumerate(ON_SCREEN_LETTERS7):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter7(i7)
        while len(ON_SCREEN_LETTERS7) < 1:
            add_letter7()
    
    if stop1 != 1 and intafad == 1 and e == 1:
        for i8, LETTER in enumerate(ON_SCREEN_LETTERS8):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter8(i8)
        while len(ON_SCREEN_LETTERS8) < 1:
            add_letter5()
    if stop1 != 1 and intafad == 1 and e == 1:
        for i9, LETTER in enumerate(ON_SCREEN_LETTERS9):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter9(i9)
        while len(ON_SCREEN_LETTERS9) < 1:
            add_letter9()
    if stop1 != 1 and intafad == 1 and e == 1:
        for i10, LETTER in enumerate(ON_SCREEN_LETTERS10):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter10(i10)
        while len(ON_SCREEN_LETTERS10) < 1:
            add_letter10()
    #ระดับปานกลาง
    if stop1 != 1 and intafad == 1 and m == 1:
        for i1, LETTER in enumerate(ON_SCREEN_LETTERS1):
            LETTER["y"] += VELOCITY2
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter1(i1)
        while len(ON_SCREEN_LETTERS1) < 1:
            add_letter1()
    if stop1 != 1 and intafad == 1 and m == 1:
        for i2, LETTER in enumerate(ON_SCREEN_LETTERS2):
            LETTER["y"] += VELOCITY2
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter2(i2)
        while len(ON_SCREEN_LETTERS2) < 1:
            add_letter2()
    if stop1 != 1 and intafad == 1 and m == 1:
        for i3, LETTER in enumerate(ON_SCREEN_LETTERS3):
            LETTER["y"] += VELOCITY2    
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter3(i3)
        while len(ON_SCREEN_LETTERS3) < 1:
            add_letter3()
    if stop1 != 1 and intafad == 1 and m == 1:
        for i4, LETTER in enumerate(ON_SCREEN_LETTERS4):
            LETTER["y"] += VELOCITY2
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter4(i4)
        while len(ON_SCREEN_LETTERS4) < 1:
            add_letter4()
    if stop1 != 1 and intafad == 1 and m == 1:
        for i5, LETTER in enumerate(ON_SCREEN_LETTERS5):
            LETTER["y"] += VELOCITY2
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter5(i5)
        while len(ON_SCREEN_LETTERS5) < 1:
            add_letter5()
    if stop1 != 1 and intafad == 1 and e == 1:
        for i6, LETTER in enumerate(ON_SCREEN_LETTERS6):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter6(i6)
        while len(ON_SCREEN_LETTERS5) < 1:
            add_letter6()
    
    if stop1 != 1 and intafad == 1 and e == 1:
        for i7, LETTER in enumerate(ON_SCREEN_LETTERS7):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter7(i7)
        while len(ON_SCREEN_LETTERS7) < 1:
            add_letter7()
    
    if stop1 != 1 and intafad == 1 and e == 1:
        for i8, LETTER in enumerate(ON_SCREEN_LETTERS8):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter8(i8)
        while len(ON_SCREEN_LETTERS8) < 1:
            add_letter5()
    if stop1 != 1 and intafad == 1 and e == 1:
        for i9, LETTER in enumerate(ON_SCREEN_LETTERS9):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter9(i9)
        while len(ON_SCREEN_LETTERS9) < 1:
            add_letter9()
    if stop1 != 1 and intafad == 1 and e == 1:
        for i10, LETTER in enumerate(ON_SCREEN_LETTERS10):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter10(i10)
        while len(ON_SCREEN_LETTERS10) < 1:
            add_letter10()
    #ระดับยาก
    if stop1 != 1 and intafad == 1 and h == 1:
        for i1, LETTER in enumerate(ON_SCREEN_LETTERS1):
            LETTER["y"] += VELOCITY3
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter1(i1)
        while len(ON_SCREEN_LETTERS1) < 1:
            add_letter1()
    if stop1 != 1 and intafad == 1 and h == 1:
        for i2, LETTER in enumerate(ON_SCREEN_LETTERS2):
            LETTER["y"] += VELOCITY3
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter2(i2)
        while len(ON_SCREEN_LETTERS2) < 1:
            add_letter2()
    if stop1 != 1 and intafad == 1 and h == 1:
        for i3, LETTER in enumerate(ON_SCREEN_LETTERS3):
            LETTER["y"] += VELOCITY3    
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter3(i3)
        while len(ON_SCREEN_LETTERS3) < 1:
            add_letter3()
    if stop1 != 1 and intafad == 1 and h == 1:
        for i4, LETTER in enumerate(ON_SCREEN_LETTERS4):
            LETTER["y"] += VELOCITY3
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter4(i4)
        while len(ON_SCREEN_LETTERS4) < 1:
            add_letter4()
    if stop1 != 1 and intafad == 1 and h == 1:
        for i5, LETTER in enumerate(ON_SCREEN_LETTERS5):
            LETTER["y"] += VELOCITY3
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter5(i5)
        while len(ON_SCREEN_LETTERS5) < 1:
            add_letter5()
    if stop1 != 1 and intafad == 1 and e == 1:
        for i6, LETTER in enumerate(ON_SCREEN_LETTERS6):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter6(i6)
        while len(ON_SCREEN_LETTERS5) < 1:
            add_letter6()
    
    if stop1 != 1 and intafad == 1 and e == 1:
        for i7, LETTER in enumerate(ON_SCREEN_LETTERS7):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter7(i7)
        while len(ON_SCREEN_LETTERS7) < 1:
            add_letter7()
    
    if stop1 != 1 and intafad == 1 and e == 1:
        for i8, LETTER in enumerate(ON_SCREEN_LETTERS8):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter8(i8)
        while len(ON_SCREEN_LETTERS8) < 1:
            add_letter5()
    if stop1 != 1 and intafad == 1 and e == 1:
        for i9, LETTER in enumerate(ON_SCREEN_LETTERS9):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter9(i9)
        while len(ON_SCREEN_LETTERS9) < 1:
            add_letter9()
    if stop1 != 1 and intafad == 1 and e == 1:
        for i10, LETTER in enumerate(ON_SCREEN_LETTERS10):
            LETTER["y"] += VELOCITY
            if LETTER["y"] == HEIGHT - 400:
                SCORE["WRONG"] += 1
                delete_letter10(i10)
        while len(ON_SCREEN_LETTERS10) < 1:
            add_letter10()

def on_key_down(key, mod, unicode):
    global SCORE
    if stop1 != 1 and intafad == 1:
        if unicode:
            for i1, LETTER in enumerate(ON_SCREEN_LETTERS1):
                if LETTER["letter"] == unicode:
                    SCORE["RIGHT"] += 1
                    delete_letter1(i1)
                    return
    if stop1 != 1 and intafad == 1:
        if unicode:
            for i2, LETTER in enumerate(ON_SCREEN_LETTERS2):
                if LETTER["letter"] == unicode:
                    SCORE["RIGHT"] += 1
                    delete_letter2(i2)
                    return
    if stop1 != 1 and intafad == 1:
        if unicode:
            for i3, LETTER in enumerate(ON_SCREEN_LETTERS3):
                if LETTER["letter"] == unicode:
                    SCORE["RIGHT"] += 1
                    delete_letter3(i3)
                    return
    if stop1 != 1 and intafad == 1:
        if unicode:
            for i4, LETTER in enumerate(ON_SCREEN_LETTERS4):
                if LETTER["letter"] == unicode:
                    SCORE["RIGHT"] += 1
                    delete_letter4(i4)
                    return
    if stop1 != 1 and intafad == 1:
        if unicode:
            for i5, LETTER in enumerate(ON_SCREEN_LETTERS5):
                if LETTER["letter"] == unicode:
                    SCORE["RIGHT"] += 1
                    delete_letter5(i5)
                    return

    if stop1 != 1 and intafad == 1:
        if unicode:
            for i6, LETTER in enumerate(ON_SCREEN_LETTERS6):
                if LETTER["letter"] == unicode:
                    SCORE["RIGHT"] += 1
                    delete_letter5(i6)
                    return

    if stop1 != 1 and intafad == 1:
        if unicode:
            for i7, LETTER in enumerate(ON_SCREEN_LETTERS7):
                if LETTER["letter"] == unicode:
                    SCORE["RIGHT"] += 1
                    delete_letter5(i7)
                    return   

    if stop1 != 1 and intafad == 1:
        if unicode:
            for i8, LETTER in enumerate(ON_SCREEN_LETTERS8):
                if LETTER["letter"] == unicode:
                    SCORE["RIGHT"] += 1
                    delete_letter5(i8)
                    return

    if stop1 != 1 and intafad == 1:
        if unicode:
            for i9, LETTER in enumerate(ON_SCREEN_LETTERS9):
                if LETTER["letter"] == unicode:
                    SCORE["RIGHT"] += 1
                    delete_letter5(i9)
                    return
    if stop1 != 1 and intafad == 1:
        if unicode:
            for i10, LETTER in enumerate(ON_SCREEN_LETTERS9):
                if LETTER["letter"] == unicode:
                    SCORE["RIGHT"] += 1
                    delete_letter5(i10)
                    return

def on_mouse_down(pos):
    global intafad , stop1
    global SCORE
    global ON_SCREEN_LETTERS1,ON_SCREEN_LETTERS2,ON_SCREEN_LETTERS3,ON_SCREEN_LETTERS4,ON_SCREEN_LETTERS5,ON_SCREEN_LETTERS6,ON_SCREEN_LETTERS7,ON_SCREEN_LETTERS8,ON_SCREEN_LETTERS9,ON_SCREEN_LETTERS10
    global e ,m , h, st 
    global end
   
    if apple.collidepoint(pos):
        intafad += 1
    if e == 1 or m == 1 or h == 1:
        if stop.collidepoint(pos):
            if stop1 >= 0 and stop1 < 1:
                stop1 += 1
    
    if stop1 == 1:
        if playcon.collidepoint(pos):
            stop1 -= 1
    
    if stop1 == 1:   
        if regame.collidepoint(pos):
            SCORE["RIGHT"] = 0
            SCORE["WRONG"] = 0
            stop1 -= 1
            ON_SCREEN_LETTERS1 = []
            ON_SCREEN_LETTERS2 = []
            ON_SCREEN_LETTERS3 = []
            ON_SCREEN_LETTERS4 = []
            ON_SCREEN_LETTERS5 = []
            ON_SCREEN_LETTERS6 = []
            ON_SCREEN_LETTERS7 = []
            ON_SCREEN_LETTERS8 = []
            ON_SCREEN_LETTERS9 = []
            ON_SCREEN_LETTERS10 = []
    if stop1 == 1:    
        if endgame.collidepoint(pos):
            end += 5
            ON_SCREEN_LETTERS1 = []
            ON_SCREEN_LETTERS2 = []
            ON_SCREEN_LETTERS3 = []
            ON_SCREEN_LETTERS4 = []
            ON_SCREEN_LETTERS5 = []
            ON_SCREEN_LETTERS6 = []
            ON_SCREEN_LETTERS7 = []
            ON_SCREEN_LETTERS8 = []
            ON_SCREEN_LETTERS9 = []
            ON_SCREEN_LETTERS10 = []
    if intafad == 1 and st == 0:
        if easy.collidepoint(pos):
            e += 1
            st += 1
    if intafad == 1 and st == 0:
        if mid.collidepoint(pos):
            m += 1
            st += 1
    if intafad == 1 and st == 0:
        if hard.collidepoint(pos):
            h += 1
            st += 1
    if intafad == 1 and st == 0:
        if black1.collidepoint(pos):
            intafad -= 1
    
    if end == 5 or SCORE['WRONG'] >= 3:
        if home.collidepoint(pos):
            if end == 5:
                end -= 5
            intafad -= 1
            if stop1 == 1:
                stop1 -= 1
            if e == 1:
                e -= 1
                st -= 1
            if m == 1:
                m -= 1
                st -= 1
            if h == 1:
                h -= 1
                st -= 1
            SCORE["RIGHT"] = 0
            SCORE["WRONG"] = 0
            ON_SCREEN_LETTERS1 = []
            ON_SCREEN_LETTERS2 = []
            ON_SCREEN_LETTERS3 = []
            ON_SCREEN_LETTERS4 = []
            ON_SCREEN_LETTERS5 = []
            ON_SCREEN_LETTERS6 = []
            ON_SCREEN_LETTERS7 = []
            ON_SCREEN_LETTERS8 = []
            ON_SCREEN_LETTERS9 = []
            ON_SCREEN_LETTERS10 = []
           
    if SCORE['WRONG'] >= 3 or end == 5:
        if playagain.collidepoint(pos):
            if end == 5:
                end -= 5
            if stop1 == 1:
                stop1 -= 1
            SCORE["RIGHT"] = 0
            SCORE["WRONG"] = 0
            ON_SCREEN_LETTERS1 = []
            ON_SCREEN_LETTERS2 = []
            ON_SCREEN_LETTERS3 = []
            ON_SCREEN_LETTERS4 = []
            ON_SCREEN_LETTERS5 = []
            ON_SCREEN_LETTERS6 = []
            ON_SCREEN_LETTERS7 = []
            ON_SCREEN_LETTERS8 = []
            ON_SCREEN_LETTERS9 = []
            ON_SCREEN_LETTERS10 = []

##########################################################################
def add_letter1():
    #ตัวหนังสือตกง่าย
    if stop1 != 1 and intafad == 1 and e == 1:
        letter = random.choice(string.ascii_letters).lower()
        x1 = 400
        y1 = 1
        ON_SCREEN_LETTERS1.append({"letter": letter, "x": x1 , "y": y1})
    #ตัวหนังสือตกปานกลาง
    if stop1 != 1 and intafad == 1 and m == 1:
        letter = random.choice(string.ascii_letters).lower()
        x1 = 400
        y1 = 2
        ON_SCREEN_LETTERS1.append({"letter": letter, "x": x1 , "y": y1})
    #ตัวหนังสือตกยาก
    if stop1 != 1 and intafad == 1 and h == 1:
        letter = random.choice(string.ascii_letters).lower()
        x1 = 400
        y1 = 4
        ON_SCREEN_LETTERS1.append({"letter": letter, "x": x1 , "y": y1})
    #ของแแถวที่1 ตำแหน่ง x = 400
def add_letter2():
    #ตัวหนังสือตกง่าย
    if stop1 != 1 and intafad == 1 and e == 1:
        letter = random.choice(string.ascii_letters).lower()
        x2 = 700
        y2 = 1
        ON_SCREEN_LETTERS2.append({"letter": letter, "x": x2 , "y": y2})
    #ตัวหนังสือตกปานกลาง
    if stop1 != 1 and intafad == 1 and m == 1:
        letter = random.choice(string.ascii_letters).lower()
        x2 = 700
        y2 = 2
        ON_SCREEN_LETTERS2.append({"letter": letter, "x": x2 , "y": y2})
    #ตัวหนังสือตกยาก
    if stop1 != 1 and intafad == 1 and h == 1:
        letter = random.choice(string.ascii_letters).lower()
        x2 = 700
        y2 = 4
        ON_SCREEN_LETTERS2.append({"letter": letter, "x": x2 , "y": y2})
    #ของแแถวที่2 ตำแหน่ง x = 700
def add_letter3():
    #ตัวหนังสือตกง่าย
    if stop1 != 1 and intafad == 1 and e == 1:
        letter = random.choice(string.ascii_letters).lower()
        x3 = 900
        y3 = 1
        ON_SCREEN_LETTERS3.append({"letter": letter, "x": x3 , "y": y3})
    #ตัวหนังสือตกปานกลาง
    if stop1 != 1 and intafad == 1 and m == 1:
        letter = random.choice(string.ascii_letters).lower()
        x3 = 900
        y3 = 2
        ON_SCREEN_LETTERS3.append({"letter": letter, "x": x3 , "y": y3})
    #ตัวหนังสือตกยาก   
    if stop1 != 1 and intafad == 1 and h == 1:
        letter = random.choice(string.ascii_letters).lower()
        x3 = 900
        y3 = 4
        ON_SCREEN_LETTERS3.append({"letter": letter, "x": x3 , "y": y3})
    #ของแแถวที่2 ตำแหน่ง x = 900
def add_letter4():
    #ตัวหนังสือตกง่าย
    if stop1 != 1 and intafad == 1 and e == 1:
        letter = random.choice(string.ascii_letters).lower()
        x4 = 1100
        y4 = 1
        ON_SCREEN_LETTERS4.append({"letter": letter, "x": x4 , "y": y4})
    #ตัวหนังสือตกปานกลาง
    if stop1 != 1 and intafad == 1 and m == 1:
        letter = random.choice(string.ascii_letters).lower()
        x4 = 1100
        y4 = 2
        ON_SCREEN_LETTERS4.append({"letter": letter, "x": x4 , "y": y4})
    #ตัวหนังสือตกยาก
    if stop1 != 1 and intafad == 1 and h == 1:
        letter = random.choice(string.ascii_letters).lower()
        x4 = 1100
        y4 = 4
        ON_SCREEN_LETTERS4.append({"letter": letter, "x": x4 , "y": y4})
    #ของแแถวที่2 ตำแหน่ง x = 1100
def add_letter5():
    #ตัวหนังสือตกง่าย
    if stop1 != 1 and intafad == 1 and e == 1:
        letter = random.choice(string.ascii_letters).lower()
        x5 = 1300
        y5 = randint(1,3)
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x5 , "y": y5})
    #ตัวหนังสือตกปานกลาง
    if stop1 != 1 and intafad == 1 and m == 1:
        letter = random.choice(string.ascii_letters).lower()
        x5 = 1300
        y5 = 2
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x5 , "y": y5})
    #ตัวหนังสือตกยาก
    if stop1 != 1 and intafad == 1 and h == 1:
        letter = random.choice(string.ascii_letters).lower()
        x5 = 1300
        y5 = 4
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x5 , "y": y5})
    #ของแแถวที่2 ตำแหน่ง x = 1300
def add_letter6():
    #ตัวหนังสือตกง่าย
    if stop1 != 1 and intafad == 1 and e == 1:
        letter = random.choice(string.ascii_letters).lower()
        x6 = 1300
        y6 = 1
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x6 , "y": y6})
    #ตัวหนังสือตกปานกลาง
    if stop1 != 1 and intafad == 1 and m == 1:
        letter = random.choice(string.ascii_letters).lower()
        x6 = 1300
        y6 = 2
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x6 , "y": y6})
    #ตัวหนังสือตกยาก
    if stop1 != 1 and intafad == 1 and h == 1:
        letter = random.choice(string.ascii_letters).lower()
        x6 = 1300
        y6 = 4
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x6 , "y": y6})
    #ของแแถวที่2 ตำแหน่ง x = 1300
def add_letter7():
    #ตัวหนังสือตกง่าย
    if stop1 != 1 and intafad == 1 and e == 1:
        letter = random.choice(string.ascii_letters).lower()
        x7 = 1300
        y7 = 1
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x7 , "y": y7})
    #ตัวหนังสือตกปานกลาง
    if stop1 != 1 and intafad == 1 and m == 1:
        letter = random.choice(string.ascii_letters).lower()
        x7 = 1300
        y7 = 2
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x7 , "y": y7})
    #ตัวหนังสือตกยาก
    if stop1 != 1 and intafad == 1 and h == 1:
        letter = random.choice(string.ascii_letters).lower()
        x7 = 1300
        y7 = 4
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x7 , "y": y7})
    #ของแแถวที่2 ตำแหน่ง x = 1300
def add_letter8():
    #ตัวหนังสือตกง่าย
    if stop1 != 1 and intafad == 1 and e == 1:
        letter = random.choice(string.ascii_letters).lower()
        x8 = 1300
        y8 = 1
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x8 , "y": y8})
    #ตัวหนังสือตกปานกลาง
    if stop1 != 1 and intafad == 1 and m == 1:
        letter = random.choice(string.ascii_letters).lower()
        x8 = 1300
        y8= 2
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x8 , "y": y8})
    #ตัวหนังสือตกยาก
    if stop1 != 1 and intafad == 1 and h == 1:
        letter = random.choice(string.ascii_letters).lower()
        x8 = 1300
        y8 = 4
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x8 , "y": y8})
    #ของแแถวที่2 ตำแหน่ง x = 1300
def add_letter9():
    #ตัวหนังสือตกง่าย
    if stop1 != 1 and intafad == 1 and e == 1:
        letter = random.choice(string.ascii_letters).lower()
        x9 = 1300
        y9 = 1
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x9 , "y": y9})
    #ตัวหนังสือตกปานกลาง
    if stop1 != 1 and intafad == 1 and m == 1:
        letter = random.choice(string.ascii_letters).lower()
        x9 = 1300
        y9 = 2
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x9 , "y": y9})
    #ตัวหนังสือตกยาก
    if stop1 != 1 and intafad == 1 and h == 1:
        letter = random.choice(string.ascii_letters).lower()
        x9 = 1300
        y9 = 4
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x9 , "y": y9})
    #ของแแถวที่2 ตำแหน่ง x = 1300
def add_letter10():
    #ตัวหนังสือตกง่าย
    if stop1 != 1 and intafad == 1 and e == 1:
        letter = random.choice(string.ascii_letters).lower()
        x10 = 1300
        y10 = 1
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x10 , "y": y10})
    #ตัวหนังสือตกปานกลาง
    if stop1 != 1 and intafad == 1 and m == 1:
        letter = random.choice(string.ascii_letters).lower()
        x10 = 1300
        y10 = 2
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x10 , "y": y10})
    #ตัวหนังสือตกยาก
    if stop1 != 1 and intafad == 1 and h == 1:
        letter = random.choice(string.ascii_letters).lower()
        x10 = 1300
        y10 = 4
        ON_SCREEN_LETTERS5.append({"letter": letter, "x": x10 , "y": y10})
    #ของแแถวที่2 ตำแหน่ง x = 1300
##########################################################################   

def delete_letter1(i):
    if stop1 != 1 and intafad == 1:
        del ON_SCREEN_LETTERS1[i]
        add_letter1()
def delete_letter2(i):
    if stop1 != 1 and intafad == 1:
        del ON_SCREEN_LETTERS2[i]
        add_letter2()
def delete_letter3(i):
    if stop1 != 1 and intafad == 1:
        del ON_SCREEN_LETTERS3[i]
        add_letter3()
def delete_letter4(i):
    if stop1 != 1 and intafad == 1:
        del ON_SCREEN_LETTERS4[i]
        add_letter4()
def delete_letter5(i):
    if stop1 != 1 and intafad == 1:
        del ON_SCREEN_LETTERS5[i]
        add_letter5()
def delete_letter6(i):
    if stop1 != 1 and intafad == 1:
        del ON_SCREEN_LETTERS6[i]
        add_letter6()
def delete_letter7(i):
    if stop1 != 1 and intafad == 1:
        del ON_SCREEN_LETTERS7[i]
        add_letter7()
def delete_letter8(i):
    if stop1 != 1 and intafad == 1:
        del ON_SCREEN_LETTERS8[i]
        add_letter8()
def delete_letter9(i):
    if stop1 != 1 and intafad == 1:
        del ON_SCREEN_LETTERS9[i]
        add_letter9()
def delete_letter10(i):
    if stop1 != 1 and intafad == 1:
        del ON_SCREEN_LETTERS10[i]
        add_letter10()
    

pgzrun.go()