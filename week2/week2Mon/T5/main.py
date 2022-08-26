import numpy as np

he = np.zeros([105, 105], dtype=int, order='C')
dp = np.zeros([105, 105], dtype=int, order='C')
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
global n
global m

def search(x, y):
    if not dp[x][y] == 0:
        return dp[x][y]
    for i in range(0, 4):
        newX = x + dx[i]
        newY = y + dy[i]
        if newX >= 0 and newX < n and newY >= 0 and newY < m:
            if he[x][y] > he[newX][newY]:
                dp[x][y] = max(search(newX, newY) + 1, dp[x][y])
    return dp[x][y]

if __name__ == '__main__':
    # input

    arr = input().split(" ")
    n = int(arr[0])
    m = int(arr[1])
    for i in range(0, n):
        arr = input().split(" ")
        for j in range(0, m):
            he[i][j] = arr[j]

    # calc
    for i in range(0, n):
        for j in range(0, m):
            search(i, j)

    max_ = 0

    for i in range(0, n):
        for j in range(0, m):
            max_ = max(max_, dp[i][j])

    print(max_ + 1)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
