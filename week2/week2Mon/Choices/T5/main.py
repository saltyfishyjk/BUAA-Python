# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

class TestFather:
    def __init__(self):
        self.attr = 100
    def do(self):
        print("choose AC!")

class TestChild(TestFather):
    def do(self):
        print("choose BD!")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = TestChild()
    test.do()
    print(test.attr)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
