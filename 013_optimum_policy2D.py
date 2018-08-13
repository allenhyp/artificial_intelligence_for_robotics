# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------


def optimum_policy2D(grid, init, goal, cost):
    value = [[[999 for col in range(len(grid[0]))] for row in range(len(grid))] for orientation in range(4)]
    policy = [[[' ' for col in range(len(grid[0]))] for row in range(len(grid))] for orientation in range(4)]
    policy2D = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    change = True
    while change:
        change = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for direction in range(4):
                    if goal[0] == x and goal[1] == y:
                        if value[direction][x][y] > 0:
                            value[direction][x][y] = 0
                            policy[direction][x][y] = '*'
                            change = True
                    elif grid[x][y] == 0:
                        for a in range(3):
                            d2 = (direction + action[a]) % 4
                            x2 = x + forward[d2][0]
                            y2 = y + forward[d2][1]
                            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                                v2 = value[d2][x2][y2] + cost[a]
                                if v2 < value[direction][x][y]:
                                    change = True
                                    value[direction][x][y] = v2
                                    policy[direction][x][y] = action_name[a]

    x = init[0]
    y = init[1]
    d = init[2]
    policy2D[x][y] = policy[d][x][y]
    while policy[d][x][y] != '*':
        if policy[d][x][y] == '#':
            d2 = d
        elif policy[d][x][y] == 'R':
            d2 = (d - 1) % 4
        elif policy[d][x][y] == 'L':
            d2 = (d + 1) % 4
        x = x + forward[d2][0]
        y = y + forward[d2][1]
        d = d2
        policy2D[x][y] = policy[d][x][y]
    return policy2D


result = optimum_policy2D(grid, init, goal, cost)
for r in result:
    print(r)
