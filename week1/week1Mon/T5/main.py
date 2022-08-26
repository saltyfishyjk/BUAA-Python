# -*- coding :utf-8 -*-
if __name__ == '__main__':
    n, k = map(int, input().split())
    A = 0
    B = 0
    Anum = 0
    Bnum = 0
    for i in range(1, n + 1):
        if i % k == 0:
            A += i
            Anum += 1
        else:
            B += i
            Bnum += 1
    print("%.1f %.1f" %(float(A / Anum), float(B / Bnum)))