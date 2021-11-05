import pygame
from imagerect import ImageRect
from logger import LogLevel, Logger
from portal import Portal
from vector import Vector
# from character import Character
# from direction import Direction


class Maze:
    RED = (255, 0, 0)
    BRICK_SIZE = 15

    def __init__(self, screen, expand_by, mazefile, brickfile, shieldfile, pointfile):
        self.screen = screen
        self.expand_by = expand_by
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []
        self.shields = []
        self.points = []
        self.nodes = {}    # dictionary
        self.nodercs = []

        sz = Maze.BRICK_SIZE
        self.brick = ImageRect(screen, brickfile, sz, sz)
        self.shield = ImageRect(screen, shieldfile, sz, sz)
        self.point = ImageRect(screen, pointfile, int(sz), int(sz))

        self.deltax = self.deltay = Maze.BRICK_SIZE

        Logger.level = LogLevel.KEY
        Logger.key = 'collision'
        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def droppoint(self, x, y):
        xmin, ymin, xmax, ymax = 6, 8, int(47 * self.expand_by), int(51 * self.expand_by)
        if y < ymin or y > ymax or x < xmin or x > xmax:
            return False
        if 42 < y < 70 or 72 < y < 100 and x < 30 or x > 106:
            return False
        elif ((x - 2) % 3 == 2 and (y - 1) % 3 == 1) and (self.colnearby_clear(x, y, -3, 3)) and (self.rownearby_clear(x, y, -3, 3)):
            return True
        return False

    def scaletochars(self, character):
        return int(character.posn.x/self.deltax), int(character.posn.y/self.deltay)

    def collisionif(self, character):
        c = character
        scaled_posn = self.scaletochars(c)
        return not self.infront_clear(scaled_posn[0], scaled_posn[1], c.velocity)

    def infront_clear(self, x, y, velocity):
        intvx = int(velocity.x)
        intvy = int(velocity.y)
        Logger.log('===========intvs is:' + str(intvx))
        if intvx != 0:
            return self.rowinfront_clear(x, y, 2 * intvx)
        else:
            return self.colinfront_clear(x, y, 2 * intvy)

    def rowinfront_clear(self, x, y, nchars):
        nchars = int(nchars)
        Logger.log('*************************************  x:' + str(x) + ', y:' + str(y) + ', nchars:' + str(nchars))
        return self.rownearby_clear(x, y, nchars, 0, True) if nchars < 0 else self.rownearby_clear(x, y, 0, nchars, True)

    def colinfront_clear(self, x, y, nchars):
        nchars = int(nchars)
        Logger.log('*******************,  x:' + str(x) + ', y:' + str(y) + ', nchars:' + str(nchars))
        return self.colnearby_clear(x, y, nchars, 0, True) if nchars < 0 else self.colnearby_clear(x, y, 0, nchars, True)

    def rownearby_clear(self, x, y, deltaminus, deltaplus, log=False):
        row = self.rows[y]
        minx = max(x + deltaminus + 2, 0)
        maxx = min(x + deltaplus + 1, len(row) - 1)
        string = row[minx: maxx]
        ok = 'X' not in string
        Logger.log('+++++ minx:' + str(minx) + 'maxx:' + str(maxx))
        Logger.log('-----string|' + string + '|ok:' + str(ok))
        return ok

    def colnearby_clear(self, x, y, deltaminus, deltaplus, log=False):
        miny = max(y + deltaminus + 2, 0)
        maxy = min(y + deltaplus + 1, len(self.rows) + 1)
        string = []

        for i in range(miny, maxy):
            string.append(self.rows[i][x])
        ok = 'X' not in string and 'o' not in string
        Logger.log('+++++ miny:' + str(miny) + 'maxy:' + str(maxy), key='collision')
        Logger.log('-----string|' + str(string) + '|ok:' + str(ok))
        return ok

    def build(self):
        r = self.brick.rect
        rshield = self.shield.rect
        rpoint = self.point.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay
        self.nodercs.append([])    # first row
        nnodes = 0
        nnoderow = 0
        nodeprevrow = 0
        tmp = 0

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                last = len(row) - 1
                rest = row[ncol+1:] if ncol < last - 2 else row[last]
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 's':
                    self.shields.append(pygame.Rect(ncol * dx, nrow * dy, rshield.width, rshield.height))
                elif col == 'N':
                    if nnodes > 0 and nodeprevrow != nnoderow:  # new row
                        self.nodercs.append([])

                    v = Vector(ncol * dx, nrow * dy, 0)
                    self.nodes[nnodes] = v
                    self.nodercs[nnoderow].append(v)    # add node to row
                    nodeprevrow = nnoderow         # keep track of last row
                    nnodes += 1
                    if not 'N' in rest:
                        nnoderow += 1
                elif self.droppoint(ncol, nrow):
                    self.points.append(pygame.Rect(ncol * dx, nrow * dy, rpoint.width, rpoint.height))
                elif col == '\n':
                    tmp += 1

        nodedict = {}
        rowchar = 97
        for row in self.nodercs:
            rowname = chr(rowchar)
            colchar = 65
            for el in row:
                colname = chr(colchar)
                name = ('%02d' % (rowchar - 97)) + '_' + ('%02d' % (colchar - 65))
                print(name + ' ' + str(el))
                nodedict[name] = el
                colchar += 1
            print()
            rowchar += 1

        for key, value in nodedict.items():
            print(key, ' ', value)

        print()
        print('testing the dictionary...')
        self.node_location(nodedict, '00_00')
        self.node_location(nodedict, '00_02')
        self.node_location(nodedict, '01_03')
        self.node_location(nodedict, '02_03')
        self.node_location(nodedict, '11_00')
        self.node_location(nodedict, '04_01')

        rownodes = set()
        for row in self.nodercs:
            for val in row:
                rownodes.add(val.x)

        for el in rownodes:
            print(el, end=' ')
        lirownodes = list(rownodes)
        lirownodes.sort()
        for el in lirownodes:
            print(el, '-')

    def node_location(self, nodedict, node):
        print(str(node) + ' is at: ' + str(nodedict[node]))

    def nearest_node(self, posn):
        x, y = posn.x, posn.y

    def blit(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.shields:
            self.screen.blit(self.shield.image, rect)
        for rect in self.points:
            self.screen.blit(self.point.image, rect)
