import random
num = random.randint(1,10)
while True:
	guess = input()
	i = int(guess)
	if i == num:
		print("你猜对了")
		break
	elif i < num:
		print("小了")
	elif i > num:
		print("大了")