# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    value[goal[0]][goal[1]] = 0
    r = goal[0]
    c = goal[1]
    g = 0
    queue = [[g, r, c]]
    while (True):
        if len(queue) <= 0:
            break
        queue.sort()
        queue.reverse()
        top = queue.pop()
        r = top[1]
        c = top[2]
        g = top[0]
        for i in range(len(delta)):
            r2 = r - delta[i][0]
            c2 = c - delta[i][1]
            g2 = g + cost
            if r2 >= 0 and r2 < len(grid) and c2 >= 0 and c2 < len(grid[0]):
                if grid[r2][c2] != 1 and g2 < value[r2][c2]:
                    value[r2][c2] = g2
                    queue.append([g2, r2, c2])

    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 


ret = compute_value(grid, goal, cost)
for item in ret:
    print(item)