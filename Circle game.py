import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

print("Print your username:")
username=input()
print("Good luck, ", username)
score0 = 0
k0 = 0
sscore0 = 0
sk0 = 0
n = 6
ball_x = [0]*n
ball_y = [0]*n
ball_r = [0]*n
ball_vx = [0]*n
ball_vy = [0]*n
ball_c = [RED]*n
#ball_t = [0]*n

sball_x = [0]*n
sball_y = [0]*n
sball_r = [0]*n
sball_vx = [0]*n
sball_vy = [0]*n
sball_c = [RED]*n
#sball_t = [0]*n

def new_ball(i):
    '''рисует новый шарик '''
    global ball_x, ball_y, ball_r, ball_vx, ball_vy, ball_t
    x = randint(100, 800)
    ball_x[i] = x
    y = randint(100, 500)
    ball_y[i] = y
    r = randint(10, 100)
    ball_r[i] = r
    vx = randint(-10, 10)
    ball_vx[i] = vx
    vy = randint(-10, 10)
    ball_vy[i] = vy
    color = COLORS[randint(0, 5)]
    ball_c[i] = color
    ball_t[i] = 0

def new_sball(i):
    '''рисует новый шарик '''
    global sball_x, sball_y, sball_r, sball_vx, sball_vy
    x = randint(100, 800)
    sball_x[i] = x
    y = randint(100, 500)
    sball_y[i] = y
    r = randint(10, 100)
    sball_r[i] = r
    vx = randint(-10, 10)
    sball_vx[i] = vx
    vy = randint(-10, 10)
    sball_vy[i] = vy
    color = COLORS[randint(0, 5)]
    sball_c[i] = color
    sball_t[i] = 0

def move_ball(i):
    global ball_x, ball_y, ball_r, ball_vx, ball_vy, ball_t
    ball_x[i] += ball_vx[i]
    ball_y[i] += ball_vy[i]
    if (ball_x[i]-ball_r[i] <= 0):
        ball_vx[i] *= -1*randint(5, 14)/10
        ball_x[i] = ball_r[i]+1
    if (ball_x[i]+ball_r[i] >= 900):
        ball_vx[i] *= -1*randint(5, 14)/10
        ball_x[i] = 899 - ball_r[i]
    if (ball_y[i]-ball_r[i] <= 0):
        ball_vy[i] *= -1*randint(5, 14)/10
        ball_y[i] = ball_r[i]+1
    if (ball_y[i]+ball_r[i] >= 600):
        ball_vy[i] *= -1*randint(5, 14)/10
        ball_y[i] = 599 - ball_r[i]
    ball_t[i] += 1
    r = randint (0, 150)
    if (r<ball_t[i]):
        new_ball(i)

def move_sball(i):
    global sball_x, sball_y, sball_r, sball_vx, sball_vy, sball_t
    sball_x[i] += sball_vx[i]
    sball_y[i] += sball_vy[i]
    if (sball_x[i]-sball_r[i] <= 0):
        sball_vx[i] *= -1*randint(5, 14)/10
        sball_x[i] = sball_r[i]+1
    if (sball_x[i]+sball_r[i] >= 900):
        sball_vx[i] *= -1*randint(5, 14)/10
        sball_x[i] = 899 - sball_r[i]
    if (sball_y[i]-sball_r[i] <= 0):
        sball_vy[i] *= -1*randint(5, 14)/10
        sball_y[i] = sball_r[i]+1
    if (sball_y[i]+sball_r[i] >= 600):
        sball_vy[i] *= -1*randint(5, 14)/10
        sball_y[i] = 599 - sball_r[i]
    sball_t[i] += 1
    r = randint(0, 200)
    if (r < sball_t[i]):
        new_sball(i)


def draw(n):
    global ball_x, ball_y, ball_r, ball_c
    for i in range(n):
        color = COLORS[randint(0, 5)]
        ball_x[i] = round(ball_x[i])
        ball_y[i] = round(ball_y[i])
        ball_r[i] = round(ball_r[i])
        circle(screen, ball_c[i], (ball_x[i], ball_y[i]), ball_r[i])

def sdraw(n):
    global sball_x, sball_y, sball_r, sball_c
    for i in range(n):
        color = COLORS[randint(0, 5)]
        sball_x[i] = round(sball_x[i])
        sball_y[i] = round(sball_y[i])
        sball_r[i] = round(sball_r[i])
        sr = round(2*sball_r[i]/3)
        circle(screen, sball_c[i], (sball_x[i], sball_y[i]), sball_r[i])
        circle(screen, (0, 0, 0), (sball_x[i], sball_y[i]), sr)

def score(hit):
    global score0, k0
    if hit:
        k0 += 0.05
        score0 += 0.25+k0
    else:
        k0 = 0
    draw_score(score0)

def sscore(hit):
    global sscore0, sk0
    if hit:
        sk0 += 0.05
        sscore0 += 0.25+sk0
    else:
        sk0 = 0
    draw_score(sscore0)

def draw_score(a):
    global score0, sscore0
    a = score0
    b = sscore0
    a = round(a, 2)
    b = round(b, 2)
    line = "Score: " + str(a) +"+"+str(b)+"i"
    print(line)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
hit = [False]*n
shit = [False]*n
for i in range(n):
    new_ball(i)
    new_sball(i)
draw(n)
sdraw(n)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = event.pos
            for i in range(n):
                hit[i] = False
                if ((x-ball_x[i])**2+(y-ball_y[i])**2<=ball_r[i]**2):
                    hit[i] = True
            for i in range(n):
                shit[i] = False
                if ((x-sball_x[i])**2+(y-sball_y[i])**2<=sball_r[i]**2):
                    if((x-sball_x[i])**2+(y-sball_y[i])**2>=4/9*sball_r[i]**2):
                        shit[i] = True
                    else:
                        shit[i] = False
                        sscore = 0
                        sk0 = 0
                        print("GAME OVER")
                        print("You played so badly that game couldn't handle it")
                        f = open("list_of_losers.txt", "a")
                        username += " :(; "
                        f.write(username)
                        f.close()
                        Kill_All_Humans

            hit_click = False
            for i in range(n):
                if (hit[i]):
                    hit_click = True
            score(hit_click)
            for i in range(n):
                hit[i] = False

            shit_click = False
            for i in range(n):
                if (shit[i]):
                    shit_click = True
            sscore(shit_click)
            for i in range(n):
                shit[i] = False

    for i in range(n):
        move_ball(i)
        move_sball(i)
    draw(n)
    sdraw(n)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()