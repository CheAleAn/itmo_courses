import numpy as np
import random

class Ship(object):
    def __init__(self, x, y, length, direction):
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction

    def get_coordinates(self):
        cord = []
        for i in range(self.length):
            cord.append({})
        if self.direction == 0: # Восток
            for i in range(self.length):
                cord[i] = [self.x + i, self.y]
        if self.direction == 1: # Север
            for i in range(self.length):
                cord[i] = [self.x, self.y + i]
        if self.direction == 2: # Запад
            for i in range(self.length):
                cord[i] = [self.x - i, self.y]
        if self.direction == 3: # Юг
            for i in range(self.length):
                cord[i] = [self.x, self.y - i]
        return cord


class Field(object):
    def __init__(self):
        self.coord = np.zeros( (10, 10) )
    def placing(self):
        ships = [4,3,3,2,2,2,1,1,1,1]
        for j in range(10):
            installed = False
            while not installed:
                x = round(random.random()*9)
                y = round(random.random()*9)
                dir = round(random.random()*3)
                installed = False
                print(ships[j], x, y, dir)
                ship = Ship(x, y, ships[j], dir)
                coordinates = ship.get_coordinates()
                print(coordinates)
                check = True
                for i in coordinates:
                    if 0<=i[0]<10 & 0<=i[1]<10:
                        if self.coord[i[0]][i[1]] == 1:
                            check = False
                    else:
                        check = False
                if check:
                    for i in coordinates:
                        self.coord[i[0]][i[1]] = 1
                    ships[j] = 0
                    installed = True

    def attack(self):
        shots = 0
        while shots < 50:
            x = int(input("Координата x"))
            y = int(input("Координата y"))
            if self.coord[x][y] == 1:
                self.coord[x][y] = 2
                print('Меткий гад')
                if self.check_ships():
                    break
            else:
                print('Мазила')
            shots += 1

    def check_ships(self):
        batlle_continue = False
        for i in range(10):
            for j in range(10):
                if self.coord[i][j] == 1:
                    batlle_continue = True
        return batlle_continue


field = Field()
field.placing()
print(field.coord)
