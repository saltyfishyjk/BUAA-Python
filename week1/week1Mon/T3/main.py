# -*- coding :utf-8 -*-

if __name__ == '__main__':
    # input
    hour, minute = map(int, input().split())
    targetMinutes = int(input())

    # calc
    if (hour * 60 + minute + targetMinutes) > ((23 * 60) + 30):
        print("23:30")
    else:
        ansHour = (hour * 60 + minute + targetMinutes) / 60
        ansMinute = (hour * 60 + minute + targetMinutes) % 60
        print('%02d:%02d' %(ansHour, ansMinute))