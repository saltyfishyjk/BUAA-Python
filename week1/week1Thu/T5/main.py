# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())
    k = []
    ans = []

    for i in range(0, n):
        k.append(int(input()))

    for i in range(10, 10000):
        leftStr = str(i)
        rightStr = leftStr[::-1]
        tempStr = leftStr + rightStr
        num = int(tempStr)
        if num <= 100000000:
            flag = True
            for j in range(0, n):
                if num % k[j] != 0:
                    flag = False
                    break
            if flag:
                ans.append(num)
        rightStr = leftStr[-2::-1]
        tempStr = leftStr + rightStr
        num = int(tempStr)
        flag = True
        if num <= 100000000:
            for j in range(0, n):
                if num % k[j] != 0:
                    flag = False
                    break
            if flag:
                ans.append(num)
    ans = sorted(ans)
    if len(ans) == 0:
        print("None")
    else:
        for i in ans:
            print(i)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
