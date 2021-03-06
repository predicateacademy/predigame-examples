WIDTH = 30
HEIGHT = 20
TITLE = 'Agar.py'

p1 = image('kenny').scale(1.5).speed(10).keys(spaces = 2)

def eat(p, f):
    p.scale(1.05)
    sound('eat')
    f.destroy()

    if p.size > 3:
        text(time(), PURPLE)
        pause()

for i in range(25):
    f = image('pizza').speed(1).float(0.5)
    p1.collides(f, eat)

keydown('space', reset)
