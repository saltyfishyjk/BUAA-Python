# -*- coding: utf-8 -*-
def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
import math
def calc_dist(x1, y1, x2, y2):
    ret = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    ret = math.sqrt(ret)
    return ret

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    x = []
    y = []
    for i in range(0, 3):
        a, b = map(int, input().split())
        x.append(float(a))
        y.append(float(b))

    ans = 0.0

    for i in range(0, 3):
        for j in range(i + 1, 3):
            ans += float(calc_dist(float(x[i]), float(y[i]), float(x[j]), float(y[j])))

    print("%.2f"%ans)