import sys
import time
from inspect import currentframe


class DebugTool:
    def __init__(self):
        try:
            self.fd = open(r"input.txt")
        except (ImportError, OSError):
            self.debug_mode = False
        else:
            import matplotlib.pyplot as plt
            self.plt = plt
            self.fg = None
            self.ax = None
            self.debug_mode = True
            self.timer = None

    def input(self):
        if self.debug_mode:
            data = self.fd.readline()
        else:
            data = input()
        print(data, file=sys.stderr, flush=True)
        return data

    def start_timer(self):
        self.timer = time.time()

    def elapsed_time(self):
        end_time = time.time()
        interval = end_time - self.timer
        self.stderr(interval * 1000, "m sec")

    @staticmethod
    def stderr(*args):
        cf = currentframe()
        print(*args, "@" + str(cf.f_back.f_lineno), file=sys.stderr, flush=True)

    def plot_vector_clock(self, vct, clr="b", txt=""):
        # todo: refactor in OO style
        self.plt.plot((0, vct[0]), (0, vct[1]), color=clr)
        self.plt.text(vct[0], vct[1], txt)


#######################################
# Classes for the contest
#######################################
class Map:
    None


class Unit:
    def __init__(self, x, y, owner):
        self.x = int(x)
        self.y = int(y)
        self.owner = int(owner)


#######################################
# Debugger Instantiation
#######################################
DT = DebugTool()

#######################################
# Constant Values
#######################################
DOT = "."
GOAL_HEIGHT = 3

#######################################
# Parameters to be adjusted
#######################################
# STRATEGY

#######################################
# Global Initialization
#######################################
grid_size = int(DT.input())
units_per_player = int(DT.input())

#######################################
# Game Loop
#######################################
while True:
    # Initialization for turn
    grid_map = []
    units = []

    for i in range(grid_size):
        row = DT.input()
        grid_map.append(row)

    for i in range(units_per_player):
        unit_owner = 0
        unit_x, unit_y = [int(j) for j in DT.input().split()]
        units.append(Unit(unit_x, unit_y, unit_owner))
    for i in range(units_per_player):
        unit_owner = 1
        unit_x, unit_y = [int(j) for j in DT.input().split()]
        units.append(Unit(unit_x, unit_y, unit_owner))
    legal_actions = int(DT.input())
    for i in range(legal_actions):
        atype, index, dir_1, dir_2 = DT.input().split()
        index = int(index)

    # Main
    command = "{0} {1} {2} {3}".format(atype, index, dir_1, dir_2)

    print(command)
