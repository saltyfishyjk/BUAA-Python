# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputStrs = input().split(" ")
    m = int(inputStrs[0])
    n = int(inputStrs[1])
    t = int(inputStrs[2])
    arr = []
    cnt = 0
    for i in range(1, t + 1):
        for j in range(1, m + 1):
            cnt += 1
            if cnt % n == 0 or str(n) in str(cnt):
                arr.append(j)
    flag = False
    for index in range(1, m + 1):
        if index not in arr:
            flag = True
            print(index, end=" ")
    if not flag:
        print("NO")