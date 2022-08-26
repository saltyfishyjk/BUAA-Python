# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    str1 = input()
    list1 = [int(x) for x in str1.split()]
    str2 = input()
    list2 = [int(x) for x in str2.split()]
    str3 = input()
    list3 = [int(x) for x in str3.split()]
    str4 = input()
    list4 = [int(x) for x in str4.split()]
    D = np.array([list1, list2, list3, list4])
    #print(D)
    ans = np.linalg.det(D)
    print("%.0f" %(ans))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
