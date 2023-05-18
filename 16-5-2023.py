import copy
# Question 7: What is the score?

def whatsTheScore(grid):
    n = len(grid)

    # Tells if a specific grid position contains or lifeform or not. 
    # Returns value 1 if there's a lifeform, 0 otherwise
    def scan(x, y):
        if x < 0 or y < 0 or x >= n or y >= n or grid[x][y] == '.':
            return 0
        return 1
    
    # Calculates the score of a grid using the 2**(the tile number) formula
    def calcScore(grid):
        count = 0
        score = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 'X':
                    score += (2**count)
                count += 1
        return score
    
    # Keep track of all the grid layouts we've seen so far, so we can determinte when a layout appears twice
    seen = set()

    # We can't update the original grid, since changes happen simultaneously all over the grid
    # This new grid is where we make updates to represent the death or birth of lifeforms
    grid_updates = [['.' for i in range(n)] for j in range(n)]

    # This represents the [x, y] change in direction of the four adjacent tiles we can move to
    dirs = [[0,1], [1,0], [-1,0], [0,-1]]

    while True:
        # This key is used to uniquely identify a grid layout
        key = ''
        for i in range(n):
            for j in range(n):
                count = 0
                for di, dj in dirs:
                    count += scan(i+di, j+dj)
                if grid[i][j] == 'X' and count != 1:
                    grid_updates[i][j] = '.'
                elif grid[i][j] == '.' and count in [1, 2]:
                    grid_updates[i][j] = 'X'
                else:
                    grid_updates[i][j] = grid[i][j]
            key += '-'.join(grid_updates[i])
        # After making updates, we copy back to the original grid in preparation for the next iteration
        grid = copy.deepcopy(grid_updates)

        # If we see a layoout twice, calculate and return the score
        if key in seen:
            return calcScore(grid)
        seen.add(key)

# 2129920
test = ['....X', 'X..X.', 'X..XX', '..X..', 'X....']

grid = ['XXXX.', 'X....', 'X..X.', '.X.X.', 'XX.XX']
# 32509983
print(whatsTheScore(grid))