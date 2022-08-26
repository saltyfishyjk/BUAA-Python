if __name__ == '__main__':
    n = int(input())
    xStrs = input().split(" ")
    #print(xStrs)
    yStrs = input().split(" ")
    #print(yStrs)
    ans = 0
    ySum = []
    for i in range(0, n):
        if i == 0:
            ySum.append(int(yStrs[i]))
        else:
            ySum.append(ySum[i - 1] + int(yStrs[i]))
    for i in range(0, n):
        if i == 0:
            ans += int(xStrs[i]) * ySum[n - 1]
        else:
            ans += int(xStrs[i]) * (ySum[n - 1] - ySum[i - 1])
    print(ans)