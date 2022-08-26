if __name__ == '__main__':
    jerry = list(input())
    tom = list(input())
    table = []

    while True:
        jerryNow = jerry[0]
        del jerry[0]
        table.append(jerryNow)
        for index in range(0, len(table) - 1):
            if table[index] == table[len(table) - 1]:
                temp = table[index:len(table)]
                for kk in temp:
                    jerry.append(kk)
                del table[index:len(table)]
                break
        str = ""
        if len(jerry) == 0:
            print("Oh, no!")
            print(str.join(tom))
            break
        tomNow = tom[0]
        del tom[0]
        table.append(tomNow)
        for index in range(0, len(table) - 1):
            if table[index] == table[len(table) - 1]:
                temp = table[index:len(table)]
                for kk in temp:
                    tom.append(kk)
                del table[index:len(table)]
                break
        if len(tom) == 0:
            print("Hahaha~")
            print(str.join(jerry))
            break
