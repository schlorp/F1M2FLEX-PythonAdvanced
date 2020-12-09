class classA :
    speed = 10
    lives = 0
    points = 0
    deaths = 1

    def walk(self):
        print("classA loopt zo snel", self.speed)
    def jump(self):
        print("het karakter springt")

class classB (classA) :
    sneak = 100
    combat = 42

    def __init__(self) :
        self.lives = 30
        self.points = 3
    def walk(self):
        print("classB loopt zo snel", self.speed)
    def jump(self):
        super().jump()
        print("het karakter dubbel jumped")

gert = classA()
bert = classB()

gert.walk()
bert.walk()
bert.jump()
