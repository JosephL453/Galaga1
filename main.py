import pgzrun
import random

WIDTH = 1200
HEIGHT = 600

bullet = Actor('bullet')
ship = Actor('galaga')
bug = Actor('bug')

enemies = []
bullets = []

ship.pos = (WIDTH/2, HEIGHT - 60)

speed = 5

enemies.append(Actor('bug'))

enemies[-1].xpos = 10
enemies[-1].ypos = -100

score = 0

def display_score():
    screen.draw.text(str(score), (50,50), fontsize = 40)


def on_key_down(key):
    if key == keys.SPACE():
        bullets.append(Actor('bullet'))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50


def update():
    global score
    if keyboard.left:
        ship.x -= 5
        if ship.x <= 0:
            ship.x = 0
    if keyboard.right:
        ship.x += 5
        if ship.x >= WIDTH:
            ship.x = WIDTH
    

    for i in bullets:
        if i.y <= 0:
            bullets.remove(i)
        else: 
            i.y -= 10

    for i in enemies:
        i.y += 5
        if i.y >= HEIGHT:
            i.y = -100
            i.x = random.randint(50, WIDTH - 50)
        
        for j in bullets:
            if i.colliderect(j):
                score += 100
                bullets.remove(j)
                enemies.remove(i)

def draw():
    screen.clear()
    screen.fill[(0,0,255)]

    for i in bullets:
        i.draw()
    for i in enemies:
        i.draw()
    ship.draw()
    display_score()

pgzrun.go