import copy
# Question 7: What is the score?

def whatsTheScore(grid):
    n = len(grid)

    def scan(x, y):
        if x < 0 or y < 0 or x >= n or y >= n or grid[x][y] == '.':
            return 0
        return 1
    
    def calcScore(grid):
        count = 0
        score = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 'X':
                    score += (2**count)
                count += 1
        return score
    seen = set()
    grid_updates = [['.' for i in range(n)] for j in range(n)]
    dirs = [[0,1], [1,0], [-1,0], [0,-1]]

    while True:
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
        grid = copy.deepcopy(grid_updates)
        if key in seen:
            return calcScore(grid)
        seen.add(key)


test = ['....X', 'X..X.', 'X..XX', '..X..', 'X....']

grid = ['XXXX.', 'X....', 'X..X.', '.X.X.', 'XX.XX']
# 32509983
print(whatsTheScore(grid))