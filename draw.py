import pgzrun

    screen.clear()
    screen.blit('blackground',(0,0))
    pu.draw()
    pu.pos = 100,100
    for LETTER in ON_SCREEN_LETTERS:
        screen.draw.text(LETTER["letter"], (LETTER["x"], LETTER["y"]), fontsize=50, color=WHITE)
    screen.draw.text("RIGHT: " + str(SCORE["RIGHT"]), (WIDTH - 130, 10), fontsize=30, color=WHITE)
    screen.draw.text("WRONG: " + str(SCORE["WRONG"]), (WIDTH - 130, 40), fontsize=30, color=WHITE)
    screen.draw.text("TEXT: " + str(keyin), (200, HEIGHT - 50), fontsize=30, color=WHITE)

pgzrun.go()