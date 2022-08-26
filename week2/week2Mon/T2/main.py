# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputStr = input()
    arr = []
    for ch in inputStr:
        ele = str(ord(ch)).rjust(3, "0")
        arr.append(ele)
    for index in arr:
        print(index, end = "")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
