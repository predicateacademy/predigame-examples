WIDTH = 30
HEIGHT = 20
TITLE = 'Agar.py'

def eat(p, f):
    p.scale(1.05)
    sound('eat')
    f.destroy()

    if p.size > 3:
        text(time(), PURPLE)
        pause()

p1 = image('kenny').scale(1.5).keys(spaces = 2).speed(10)

for i in range(25):
    f = image('pizza').float(0.5).speed(1)
    p1.collides(f, eat)

keydown('space', reset)
