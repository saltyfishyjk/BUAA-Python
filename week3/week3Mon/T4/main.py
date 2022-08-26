import re

if __name__ == '__main__':
    n = int(input())
    elements = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar"]
    for i in range(0, n):
        strNow = input()
        arr = []
        for element in elements:
            for match in re.finditer(element.lower(), strNow.lower()):
                s = match.start()
                e = match.end()
                for index in range(s, e):
                    arr.append(index)
        flag = True
        for j in range(0, len(strNow)):
            if j not in arr:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")