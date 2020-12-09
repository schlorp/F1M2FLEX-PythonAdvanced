class gert :

    speed = 10
    sprite = None
    points = 0

    def __init__(self):
        print("de constructor van gert")

    def Walk(self) :
        print("gert loopt zo snel: ", self.speed)

class mario (gert) :
    lives = 3
    item = None

    def __init__ (self):
        super().__init__()
        self.speed = 30
    
    def Walk(self):
        print("mario loopt heel anders! Maar wel met snelheid", self.speed)

    def jump (self) :
        print("gert springt")

character = gert()
marioX = mario()

character.Walk()
marioX.Walk()
marioX.jump()

print(character.speed)
print(marioX.speed)
print(marioX.lives)
print(marioX)
