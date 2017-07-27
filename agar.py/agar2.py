WIDTH = 30
HEIGHT = 20
TITLE = 'Agar2.py'

def eat(p, f):
    p.scale(1.05)
    sound('eat')
    f.destroy()

def win(p1, p2):
    if p1.size > p2.size:
        p1.size += p2.size
        p2.destroy()

    if p2.size > p1.size:
        p2.size += p1.size
        p1.destroy()

p1 = image('kenny').scale(1.5).keys().speed(10).flip()
p2 = image('kurt').scale(1.5).keys('d', 'a', 'w', 's').speed(10)
p1.collides(p2, win)

for i in range(25):
    f = image('pizza').float(0.5).speed(1)
    p1.collides(f, eat)
    p2.collides(f, eat)

keydown('space', reset)
