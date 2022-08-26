# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def f(x):
    if x == 0:
        return 1
    elif x == 1:
        return 3
    elif x > 1:
        return (f(x - 2) + f(x - 1)) / (pow(1.01, f(x - 1)))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = int(input())
    print("%.2f" %(f(x)))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
