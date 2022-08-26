# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dict = {}
    n = int(input())
    for i in range(0, n):
        arr = input().split(" ")
        if arr[0] == '1':
            # dict[arr[1]] = int(arr[2])
            dict[arr[1]] = arr[2]
        elif arr[0] == '2':
            if dict.__contains__(arr[1]): # has_key() is abandoned in python 3.x
                print(dict[arr[1]])
            else:
                print("9999")
        elif arr[0] == '3':
            cnt = 0
            time = int(arr[2])
            for j in dict.values():
                if int(j) <= time:
                    cnt += 1
            print(cnt)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
