# -*- coding :utf-8 -*-
"""
Auther: YJK
Date: 20222022/7/5
"""
if __name__ == '__main__':
    n = int(input())
    fenzi = 0.0
    fenmu = 0.0
    for i in range(0, n):
        score, credit = map(float, input().split())
        if credit < 1.0:
            continue
        fenmu += credit
        if score < 60.0:
            fenzi += 0.0
        else:
            gp = 4 - 3 * (100-score) * (100 - score) / 1600
            fenzi += gp * credit
    print("%.2f"%(fenzi/fenmu))