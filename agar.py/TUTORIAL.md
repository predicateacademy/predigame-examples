# Agar.py Tutorial

Start with setting the window dimensions and title.
```python
WIDTH = 30
HEIGHT = 20
TITLE = 'Agar.py'
```

Next, create the player. We'll scale the image to 1.5 of a grid space, set the speed to 10, then use the arrow keys to move 2 grid spaces in each direction.
```python
WIDTH = 30
HEIGHT = 20
TITLE = 'Agar.py'

p1 = image('kenny').scale(1.5).speed(10).keys(spaces = 2)
```

Let's create some food for our player to eat. Here we're using a pizza image floating half a grid space at a speed of 1.
```python
WIDTH = 30
HEIGHT = 20
TITLE = 'Agar.py'

p1 = image('kenny').scale(1.5).speed(10).keys(spaces = 2)

for i in range(25):
    f = image('pizza').speed(1).float(0.5)
```

We need to be able to eat the food, so let's check for collisions between the player and food.
```python
WIDTH = 30
HEIGHT = 20
TITLE = 'Agar.py'

p1 = image('kenny').scale(1.5).speed(10).keys(spaces = 2)

for i in range(25):
    f = image('pizza').speed(1).float(0.5)
    p1.collides(f, eat)
```

Now we'll create the "eat" callback function we just referenced. When called, it will be passed the player and food object which collided. First, make the player a little larger. Then trigger our "eat" sound. And finally, destroy the food object.
```python
def eat(p, f):
    p.scale(1.05)
    sound('eat')
    f.destroy()
```
We'll add this above the for loop.
```python
WIDTH = 30
HEIGHT = 20
TITLE = 'Agar.py'

p1 = image('kenny').scale(1.5).speed(10).keys(spaces = 2)

def eat(p, f):
    p.scale(1.05)
    sound('eat')
    f.destroy()

for i in range(25):
    f = image('pizza').speed(1).float(0.5)
    p1.collides(f, eat)
```

We have a functional game now, but we still need a way to end it. Our end goal will be for the player to grow to 3 grid spaces, which will reveal their final time and pause the game window. Let's add this check to the eat function.
```python
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
```

Finally, instead of re-opening the game on every win, we can reset the game when the spacebar is pressed.
```python
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

```

## 2 Player

Now we can take our single player agar.py game and make it two player.

First, we'll create a second player. We use a different image here, and set the movement keys to WASD instead of the default arrow keys. Then we flip the image so that it's facing the opposite direction of our first player.
```python
WIDTH = 30
HEIGHT = 20
TITLE = 'Agar2.py'

p1 = image('kenny').scale(1.5).speed(10).keys(spaces = 2)
p2 = image('kurt').scale(1.5).speed(10).keys('d', 'a', 'w', 's', spaces = 2).flip()
```

Just like with the single player agar.py, we need an end goal. In this version, that will be to eat the other player. To implement this, we'll need to use "collides" once again. Once we know there's a collision, our callback will compare the player sizes and have the larger of the two eat the other.
```python
WIDTH = 30
HEIGHT = 20
TITLE = 'Agar2.py'

p1 = image('kenny').scale(1.5).speed(10).keys(spaces = 2)
p2 = image('kurt').scale(1.5).speed(10).keys('d', 'a', 'w', 's', spaces = 2).flip()

def win(p1, p2):
    if p1.size > p2.size:
        p1.size += p2.size
        p2.destroy()

    if p2.size > p1.size:
        p2.size += p1.size
        p1.destroy()

p1.collides(p2, win)
```

Our code should now look like:
```python
WIDTH = 30
HEIGHT = 20
TITLE = 'Agar2.py'

p1 = image('kenny').scale(1.5).speed(10).keys(spaces = 2)
p2 = image('kurt').scale(1.5).speed(10).keys('d', 'a', 'w', 's', spaces = 2).flip()

def win(p1, p2):
    if p1.size > p2.size:
        p1.size += p2.size
        p2.destroy()

    if p2.size > p1.size:
        p2.size += p1.size
        p1.destroy()

p1.collides(p2, win)

def eat(p, f):
    p.scale(1.05)
    sound('eat')
    f.destroy()

for i in range(25):
    f = image('pizza').speed(1).float(0.5)
    p1.collides(f, eat)

keydown('space', reset)
```

The last addition we need to make is ensuring the second player collides with the food by calling the "collides" method.
```python
for i in range(25):
    f = image('pizza').speed(1).float(0.5)
    p1.collides(f, eat)
    p2.collides(f, eat)
```
