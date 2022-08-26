b = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]


if __name__ == '__main__':
    n = int(input())
    x = 0
    y = 0
    arr = input().split(" ")
    year = int(arr[0])
    month = int(arr[1])
    day = int(arr[2])

    for i in range(0, n):
        citId = input()
        s = 0
        for j in range(0, len(citId) - 1):
            s += int(citId[j]) * b[j]
        if citId[17] != check[s % 11]:
            y += 1
        stuYear = int(citId[6:10])
        stuMonth = int(citId[10:12])
        stuDay = int(citId[12:14])
        if stuYear + 18 < year:
            x += 1
        elif stuYear + 18 == year:
            if stuMonth < month:
                x += 1
            elif stuMonth == month:
                if stuDay <= day:
                    x += 1

    print(str(x) + " " + str(y))
