x = 2048
ct = 0
while True:
    x -= 3
    if x % 16 == 0:
        break
    elif x % 2 == 0:
        continue
    else:
        pass
    print(x)
    ct += 1
print("ct = " + str(ct))