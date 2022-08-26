# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())
    chinese = 0.0
    math = 0.0
    english = 0.0
    for i in range(0, n * 3):
        arr = input().split(" ")
        a = float(arr[0])
        b = arr[1]
        if b == "Chinese":
            chinese += a
        elif b == "Math":
            math += a
        else:
            english += a
    print("%.2f" %(chinese / n))
    print("%.2f" %(math / n))
    print("%.2f" %(english / n))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
