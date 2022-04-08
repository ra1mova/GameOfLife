from tkinter import *
import random
from time import sleep
from copy import deepcopy

# x = column
# y = row

y = int(input('rows: '))
x = int(input('columns: '))


class SimulationGame:
    def __init__(self, cls, n, column, width, height):
        self.cls = cls
        self.n = n
        self.m = column
        self.width = width
        self.height = height
        self.array = [[random.choice([0, 1]) for _ in range(self.m)] for _ in range(self.n)]
        self.neighbours = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        self.draw_simulation()


    def print_item(self):
        for item in self.array:
            print(' '.join(map(str, item)))
        print('==================================')

    # Checks is the cell inside of array
    def __check_cell(self, field, x, y):
        return 0 <= y < self.m \
               and 0 <= x < self.n \
               and field[y][x] == 1

    # Get cells neighbours
    # c = column
    # r = row
    def _get_neighbours(self, x, y):
        for c, r in self.neighbours:
            yield x + c, y + r

    def simulation_rule(self):
        temporary_array = deepcopy(self.array)

        for i in range(self.n):
            for j in range(self.m):
                neib_alive = 0
                for y, x in self.neighbours:
                    y = (i + y) % self.n
                    x = (j + x) % self.m

                    neib_alive += temporary_array[y][x]

                if neib_alive not in (2, 3):
                    self.array[i][j] = 0
                elif neib_alive == 3:
                    self.array[i][j] = 1
                print(neib_alive)
                # break



    def draw_simulation(self):
        y_size = self.height / self.n
        x_size = self.width / self.m
        self.cls.delete('all')
        for y_item in range(self.n):
            for x_item in range(self.m):
                color = 'white'
                if self.array[y_item][x_item] == 1:
                    color = 'green'
                self.cls.create_oval(x_item * x_size,y_item * y_size, (x_item + 1) * x_size, y_size*(y_item+1), fill=color)

        self.simulation_rule()
        self.cls.after(300, self.draw_simulation)
        self.print_item()


tkinterr = Tk()
tkinterr.geometry('800x600')
tkinterr.resizable(False, False)
canva = Canvas(tkinterr, width=800, height=600)
canva.pack()
field = SimulationGame(canva, y, x, 800, 600)
tkinterr.mainloop()
