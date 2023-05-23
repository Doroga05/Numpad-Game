import random
import pygame as p

#Skärmen
Swidth = 900
Sheight = 950
p.init()
screen = p.display.set_mode((Swidth,Sheight))
p.display.set_caption("Numpad game (TS)")

#Färger 
white=(255,255,255)#röd,grön,blå
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

def PreDef():
    global Game_over, count,speed,Time_Counter,Key_x,Key_y,answer,Lost
    Game_over = False
    count = 0
    speed = 2000
    Time_Counter = 0
    Key_x = 0
    Key_y = 0
    answer = False
    Lost = False

def Grid():
    #Grid och bakgrund
    gridcolor = white
    screen.fill(black)
    line_width = 1

    for TS in range (1,3):
        p.draw.line(screen, gridcolor, (0, TS * 300 + 50), (Swidth, TS * 300 + 50), line_width)
        p.draw.line(screen, gridcolor, (TS * 300, 50), (TS * 300, Sheight), line_width)
    #linjen högst upp
    p.draw.line(screen, gridcolor, (0, 50), (Swidth,50), line_width)

def Point_count():
    global my_font
    p.font.init()
    my_font = p.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render(str(count), False, (0, 255, 0))
    screen.blit(text_surface, (10,0))

def Random_Green_Square():
    global Green_Square_x,Green_Square_y
    Green_Square_x = random.randint(0,2)
    Green_Square_y = random.randint(0,2)

def square():
    global Time_Counter
    p.draw.rect(screen, green, (Green_Square_x * 300 + 2, 50 + Green_Square_y * 300 + 2, 297, 297))
    Time_Counter += 1
    if Time_Counter == speed:
        Time_Counter = 0
        Random_Green_Square()

def Game():
    if Key_x == Green_Square_x and Key_y == Green_Square_y:
        global count,Time_Counter
        count += 1
        Time_Counter = speed - 1
    else:                   #BROKEN   BROKEN   BROKEN   BROKEN   BROKEN   BROKEN   BROKEN   BROKEN   BROKEN   BROKEN   
        global Lost
        Lost = True

def Event():
    global Key_x,Key_y,event
    for event in p.event.get():
        #Key
        if event.type == p.KEYDOWN:
            if event.key == p.K_KP1:
                Key_x = 0
                Key_y = 2
                Game()
            if event.key == p.K_KP2:
                Key_x = 1
                Key_y = 2
                Game()
            if event.key == p.K_KP3:
                Key_x = 2
                Key_y = 2
                Game()
            if event.key == p.K_KP4:
                Key_x = 0
                Key_y = 1
                Game()
            if event.key == p.K_KP5:
                Key_x = 1
                Key_y = 1
                Game()
            if event.key == p.K_KP6:
                Key_x = 2
                Key_y = 1
                Game()
            if event.key == p.K_KP7:
                Key_x = 0
                Key_y = 0
                Game()
            if event.key == p.K_KP8:
                Key_x = 1
                Key_y = 0
                Game()
            if event.key == p.K_KP9:
                Key_x = 2
                Key_y = 0
                Game()

def lost():
    global Game_over,Lost
    screen.fill(black)
    #Starta om/lämna text
    p.font.init()
    my_font = p.font.SysFont('Comic Sans MS', 50)
    text_surface = my_font.render(str("To RESTART Press ENTER"), False, (white))
    screen.blit(text_surface, (160,415))
    my_font = p.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render(str("To EXIT Press ESC"), False, (white))
    screen.blit(text_surface, (340,515))
    
    p.display.update()
    #Tangent för avsluta eller börja om
    for event in p.event.get():
        if event.type == p.KEYDOWN:
            if event.key == p.K_ESCAPE:
                Game_over = True
            elif event.key == p.K_RETURN:
                PreDef()
                Lost = False
        if(event.type == p.QUIT):
            Game_over = True
PreDef()
Random_Green_Square()
#Main LOOP
while(Game_over == False):
    if Lost == False:
        Grid()
        Point_count()
        square()
        Event()
    elif Lost == True:
        lost()



    #Rita alla förändringar.
    p.display.update()
    #quit
    if(event.type == p.QUIT):
        Game_over = True
print("Loop end")
p.quit()
