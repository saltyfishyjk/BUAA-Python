# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    essay = input()
    #if essay[0] == 'u':
    #   essay = "You" + essay[1:]
    if 'a' <= essay[0] <= 'z':
        essay = str(chr(ord("A") + ord(essay[0]) - ord("a"))) + essay[1:]

    essay = essay.replace(" u ", " you ")
    #essay = essay.replace("u ", "you ")
    #essay = essay.capitalize()
    essay = essay.replace("...", "==")
    essay = essay.replace("..", ".")
    essay = essay.replace("==", "...")
    #essay = essay.replace("english", "English")
    essayLen = len(essay)
    for i in range(0, essayLen):
        if essay[i] == 'u' or essay[i] == 'U':
            #print("i = " + str(i))
            if i == 0 and not((ord('a') <= ord(essay[i + 1]) <= ord('z')) or (ord('A') <= ord(essay[i + 1]) <= ord('Z'))):
                essay = 'You' + essay[1:]
                #print(essay)
                essayLen = len(essay)
            elif i < essayLen - 1 and (not('a' <= essay[i - 1] <= 'z' or 'A' <= essay[i - 1] <= 'Z') and not('a' <= essay[i + 1] <= 'z' or 'A' <= essay[i + 1] <= 'Z')):
                essay = essay[:i] + "you" + essay[i + 1: essayLen]
                essayLen = len(essay)
            elif i == essayLen - 1 and not ('a' <= essay[i - 1] <= 'z' or 'A' <= essay[i - 1] <= 'Z'):
                essay = essay[:i] + "you"
    for i in range(0, essayLen):
        if essay[i] == '.' or essay[i] == '?' or essay[i] == '!':
            #flag = False
            for j in range(i + 1, essayLen):
                if essay[j] == ' ':
                    continue
                else:
                    if 'a' <= essay[j] <= 'z':
                        essay = essay[0:j] + str(chr(ord("A") + ord(essay[j]) - ord("a")))  + essay[j + 1 : essayLen]
                        break
    essayLen = len(essay)
    i = 0
    while essay[i:essayLen].find('english') != -1 and i < essayLen:
        i = essay[i:essayLen].find('english')
        if (i + 7 < essayLen and (not ('a' <= essay[i+7] <= 'z' or 'A' <= essay[i + 7] <= 'Z'))) or (i + 7 >= essayLen):
            essay = essay[:i] + essay[i:i + 8].replace('english', 'English') + essay[i + 8:]
            essayLen = len(essay)
        i += 7


    print(essay)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
