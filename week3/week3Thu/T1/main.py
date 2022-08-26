import math
import itertools



def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

if __name__ == '__main__':
    n = int(input())
    inStrs = input().split(" ")
    x0 = float(inStrs[0])
    y0 = float(inStrs[1])
    loc = []
    for i in range(0, n):
        inStrs = input().split(" ")
        x = float(inStrs[0])
        y = float((inStrs[1]))
        loc.append((x, y))

    test = False
    if test:
        print(loc)

    ans = 10000000000
    for locs in itertools.permutations(loc):
        temp = dist(x0, y0, locs[0][0], locs[0][1])
        for i in range(0, n - 1):
            temp += dist(locs[i][0], locs[i][1], locs[i + 1][0], locs[i + 1][1])
        temp += dist(locs[n - 1][0], locs[n - 1][1], x0, y0)
        if test:
            print("temp : " + str(temp))
        ans = min(ans, temp)
    print("%.2f" %ans)

