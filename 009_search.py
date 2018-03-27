# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

import heapq

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']
checked = [[False for _ in range(len(grid[0]))] for __ in range(len(grid))]


def check_validiy(x, y):
    if(x >= 0 and x < len(grid) and
       y >= 0 and y < len(grid[0])):
        if not checked[x][y] and grid[x][y] == 0:
            checked[x][y] = True
            return True
    return False

def search(grid, init, goal, cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    heap = []
    print("initial open list:\n {0}".format([0, init[0], init[1]]))
    heapq.heappush(heap, (0, [0, init[0], init[1]]))
    checked[init[0]][init[1]] = True
    while len(heap) != 0:
        state = (heapq.heappop(heap))[1]
        print("take list item\n{0}".format(state))
        if goal == state[1:]:
            print("###### Search successful")
            print(state)
            return
        next_cost = state[0] + cost
        print("new open list")
        for d in delta:
            next_state = [next_cost, state[1] + d[0], state[2] + d[1]]
            if check_validiy(next_state[1], next_state[2]):
                heapq.heappush(heap, (next_cost, next_state))
                print("    {0}".format(next_state))
    path = 'fail'
    return path
