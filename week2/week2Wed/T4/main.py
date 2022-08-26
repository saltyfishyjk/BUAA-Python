
if __name__ == '__main__':
    x = int(input())
    a = input()
    b = input()
    aReverse = a[::-1]
    bReverse = b[::-1]
    aLen = len(aReverse)
    bLen = len(bReverse)
    cLen = max(aLen, bLen)
    ansStr = ""
    added = 0
    for i in range(cLen):
        aNum = int(aReverse[i]) if i < aLen else 0
        bNum = int(bReverse[i]) if i < bLen else 0
        #print("aNum : " + str(aNum))
        #print("bNum : " + str(bNum))
        num = aNum + bNum + added
        added = num // x
        num = num % x
        ansStr = ansStr + str(num)
        #print("ansStr : " + ansStr)
    if added != 0:
        ansStr = ansStr + str(added)
    ansStr = ansStr[::-1]
    print(ansStr)
