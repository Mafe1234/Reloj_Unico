one = 0
two = 0
def setup():
    size(800,100)
def draw():
    background(250,10,10)
    fill(10,10,250)
    ellipse(one, height / 2, 80, 80)
    fill(250,250,10)
    ellipse(two, height / 2, 45, 45)
    if two > width:
       two = 0
    else:
        two = map(second(), 0, 59, 0, width)
    if one > width:
        one = 0
    else:
        one = map(minute(), 0, 59, 0, width)
    global two
    global one    
