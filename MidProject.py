from tkinter import *
import random
from time import sleep

# x = column
# y = row

y = int(input('rows: '))
x = int(input('columns: '))


class SimulationGame:
    def __init__(self, cls, row, column, width, height):
        self.cls = cls
        self.row = row
        self.column = column
        self.width = width
        self.height = height
        self.array = [[random.choice([0, 1]) for _ in range(self.column)] for _ in range(self.row)]
        self.draw_simulation()

    neighbours = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    def print_item(self):
        for item in self.array:
            print(item)

    # Checks is the cell inside of array
    def __check_cell(self, field, x, y):
        return 0 <= y < self.column \
               and 0 <= x < self.row \
               and field[y][x] == 1

    # Get cells neighbours
    # c = column
    # r = row
    def _get_neighbours(self, x, y):
        for c, r in self.neighbours:
            yield x + c, y + r

    def simulation_rule(self):
        temporary_array = [[0 for _ in range(self.column)] for _ in range(self.row)]

        for item_y in range(self.row):
            for item_x in range(self.column):
                curren_cell = self.array[item_y][item_x]
                alive = 0

                for x_neighbour, y_neighbour in self._get_neighbours(item_x, item_y):
                    if self.__check_cell(self.array, x_neighbour, y_neighbour):
                        alive += 1
                    else:
                        alive += 0

                # if cell is dead
                if curren_cell == 0:
                    if 5 <= alive < 9:
                        temporary_array[item_y][item_x] = 1
                    else:
                        temporary_array[item_y][item_x] = 0

                # if cell is alive
                else:
                    if 4 <= alive < 9:
                        temporary_array[item_y][item_x] = 1
                    else:
                        temporary_array[item_y][item_x] = 0

        self.array = temporary_array

    def draw_simulation(self):
        y_size = self.width // self.row
        x_size = self.height // self.column

        for y_item in range(self.row):
            for x_item in range(self.column):
                if self.array[y_item][x_item] == 1:
                    color = 'green'
                else:
                    color = 'white'
                self.cls.create_oval((y_item + 1) * y_size, (x_item + 1) * x_size, y_item *
                                     y_size, x_item * x_size, fill=color)

        self.simulation_rule()
        sleep(1)
        self.cls.after(100, self.draw_simulation)
        self.print_item()


tkinterr = Tk()
tkinterr.geometry('800x600')
canva = Canvas(tkinterr, width=800, height=600)
canva.pack()
field = SimulationGame(canva, y, x, 800, 600)
tkinterr.mainloop()
