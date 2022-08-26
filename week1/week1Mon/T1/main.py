# -*- coding: utf-8 -*-
def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


def deal_even(num):
    for i in range(1, num + 1):
        for j in range(0, num-i):
            print(" ", end="")
        for j in range(0, i):
            print("\"", end="")
        print("")

def deal_odd(num):
    for i in range(1, num + 1):
        for j in range(0, num - i):
            print(" ", end="")
        for j in range(0, i):
            print("\\", end="")
        print("")

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    num = int(input())
    if num % 2 == 0:
        deal_even(num)
    else:
        deal_odd(num)
