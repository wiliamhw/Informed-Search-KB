from os import close
import time
import random
from guppy import hpy; h = hpy()
from colorama import Fore
from colorama import Style
import colorama
from config import rows, cols

rand_input = True
 
class Node:
    def __init__(self, y, x, _input = '\0'):
        self.x = x
        self.y = y
        self.fScore = 0
        self.hScore = 0
        self.neighbors = []
        self.previous = None
        self.isWall = False
        self.char = ""
        self.resolveWall(_input)
 
    def addNeighbors(self, grid):
        if not self.x + 1 == cols:
            self.neighbors.append(grid[self.y][self.x + 1])
        if self.x - 1 >= 0:
            self.neighbors.append(grid[self.y][self.x - 1])
        if not self.y + 1 == rows:
            self.neighbors.append(grid[self.y + 1][self.x])
        if self.y - 1 >= 0:
            self.neighbors.append(grid[self.y - 1][self.x])
 
        return self.neighbors
 
    def resolveWall(self, _input):
        if rand_input:
            temp = random.randint(1, 20)
            if (self.x == 0 and self.y == 0 or self.x == cols-1 and self.y == rows-1) or temp <= 17:
                self.isWall = False
                self.char = "-"
            else:
                self.isWall = True
                self.char = "#"
            
        else:
            if _input == '#' or _input == '-':
                self.isWall = True if _input == '#' else False
                self.char = _input
            else:
                raise Exception("Input only allows '#' and '-'.")

def heuristic(node):
    currentRow = node.y
    currentColumn = node.x
    targetRow = rows - 1
    targetColumn = cols -1
    manhattanDist = abs(currentRow - targetRow) + abs(currentColumn - targetColumn)
    return manhattanDist
 
def removeFromArray(arr, element):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == element:
            arr.pop(i)
 
def getBoard(grid):
    path = []
    for i in range(rows):
        pathTemp = []
        for j in range(cols):
            pathTemp.append(grid[i][j].char)
        path.append(pathTemp)
    print("==BOARD==")
    for i in range(rows):
        for j in range(cols):
            if (path[i][j] == '#'):
                    print(f'{Fore.RED}{path[i][j]}{Style.RESET_ALL}', end=" ")
            else:
                print(path[i][j], end=" ")
        print("")
    print("")
    return path
 
 
def printState(current):
    for i in range(0, rows):
        for j in range(0, cols):
            if current.x is j and current.y is i:
                print(".", end=" ")
            else:
                print("#", end=" ")
        print("")
    # print("= = = = = = = = = =")

def is_in_set(x, y, set):
    for element in set:
        if x == element.x and y == element.y:
            return True
    return False

def findPath(grid, start, goal):
 
    openSet = [start]
    closedSet = []
 
 
    for i in range(rows):
        for j in range(cols):
            grid[i][j].addNeighbors(grid)
 
    while not len(openSet) == 0:
        winner = 0
        # print("openSet length ", len(openSet), end=" ")
        # print("")
        for i in range(winner, len(openSet)):
            # print(openSet[i].fScore, end=" ")
            if openSet[i].fScore < openSet[winner].fScore:
                winner = i
        # print("")
        current = openSet[winner]
 
        # printState(current)
        # print("winner fScore ", current.fScore)
 
        if current == goal:
            node = current
            path = getBoard(grid)
            fScore = -1
 
            print("==PATH==")
            while node:
                fScore += 1
                path[node.y][node.x] = "."
                # print(node.y, node.x)
                node = node.previous
 
            return path, openSet, closedSet, fScore
 
        neighbors = current.neighbors
        for i in range(len(neighbors)):
            neighbor = neighbors[i]
            # print("y ", neighbor.y, "x ", neighbor.x)
            if not neighbor in closedSet and not neighbor.isWall:
                # print("y ", neighbor.y, "x ", neighbor.x)
                if neighbor not in openSet:
                    neighbor.hScore = heuristic(neighbor)
                    neighbor.fScore = neighbor.hScore
                    neighbor.previous = current
                    openSet.append(neighbor)
 
        removeFromArray(openSet, current)
        closedSet.append(current)
 
    getBoard(grid)
    return None, 0, 0, 0
 
def main():
    grid = []
    colorama.init(True)

    print("1. Randomized input")
    print("2. Customized input")
    _input = input("Input type: ")
    global rand_input
    rand_input = True if _input == '1' else False

    for i in range(rows):
        nodeCols = []
        if not rand_input:
            _input = input().split()
        for j in range(cols):
            if not rand_input:
               nodeCols.append(Node(i, j, _input[j]))
            else:
                nodeCols.append(Node(i, j))
        grid.append(nodeCols)
 
 
    start = grid[0][0]
    goal = grid[rows-1][cols-1]
 

    t0 = time.time()
    node, openSet, closedSet, f_x = findPath(grid, start, goal)
    t1 = time.time()
    if node:
        for i in range(rows):
            for j in range(cols):
                if (node[i][j] == '.'):
                    print(f'{Fore.GREEN}{node[i][j]}', end=" ")
                elif (node[i][j] == '#'):
                    print(f'{Fore.RED}{node[i][j]}', end=" ")
                else:
                    if is_in_set(j, i, openSet):
                        print(f'{Fore.BLUE}{node[i][j]}', end=" ")
                    elif is_in_set(j, i, closedSet):
                        print(f'{Fore.CYAN}{node[i][j]}', end=" ")
                    else:
                        print(node[i][j], end=" ")
            print("")

        print("Time elapsed: ", t1 - t0)
        print("Path Cost: ", f_x)
        print("Open Nodes:", len(openSet))
        print("Closed Nodes :", len(closedSet))
        print("Total Memory Sizes: " + str(h.heap().size) + " bytes")
 
if __name__ == "__main__":
    main()