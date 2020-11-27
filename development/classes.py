
class Mario :
    _lives = 4
    _speed = 30.0
    deaths = 1
    levens = 0

    def __init__(self) :
        print("wassup")
        #_lives.-deaths=levens


    def test(self):
        print("hallo")
        print("speed is: ", self._speed)

instanceMario = Mario()
extraMario = Mario()
print( instanceMario._lives )

print(Mario)

instanceMario.test()

instanceMario._speed = 10.0

print("instanceMario snelheid: ", instanceMario._speed)
print("extraMario snelheid: ", extraMario._speed)
