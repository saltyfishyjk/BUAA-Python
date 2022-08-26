import numpy as np
if __name__ == '__main__':
    n = int(input())
    b = []
    s = []
    m = []

    inStrs = input().split(" ")
    for i in range(0, n):
        b.append(int(inStrs[i]))

    inStrs = input().split(" ")
    for i in range(0, n):
        s.append(int(inStrs[i]))

    inStrs = input().split(" ")
    for i in range(0, n):
        m.append(int(inStrs[i]))

    # f[i][j] : year i now and year j since bought the bike
    f = np.zeros([1005, 1005])


    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i == 1:
                f[i][j] = b[0] + m[0]
            else:
                if j == 1:
                    temp = f[i-1][1] - s[0]
                    for k in range(2, i):
                        temp = min(temp, f[i - 1][k] - s[k - 1])
                    f[i][j] = temp + b[i - 1] + m[0]
                else:
                    f[i][j] = f[i - 1][j - 1] + m[j - 1]



    '''
    for j in range(1, n + 1):
        for i in range(1, j + 1):
            if i == 1:
                if j == 1:
                    f[i][j] = b[0] + m[0]
                else:
                    temp = 1000000000
                    for k in range(2, j):
                        temp = min(temp, f[k][j - 1] - s[j - 2] + b[j - 1] + m[0])
                    f[i][j] = temp
            else:
                f[i][j] = f[i - 1][j - 1] + m[i - 1]
    '''

    temp = 1000000000
    for i in range(1, n + 1):
        temp = min(temp, f[n][i] - s[i - 1])
    print("%.0f" %temp)

    '''
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("f[" + str(i) + "][" + str(j) + "] = " + str(f[i][j]))
    '''