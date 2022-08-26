if __name__ == '__main__':
	fruits = ["grape", "cherry", "orange", "lemon", "kiwifruit", "tomato", "peach", "pineapple", "coconut", "watermelon", "WATERMELON"]
	inStrs = input().split(" ")
	n = int(inStrs[0])
	m = int(inStrs[1])
	stack = []

	win = False
	stop = False
	for i in range(0, m):
		if stop:
			break
		fruit = input()
		stack.append(fruit)
		while True:
			flag = True
			toDel = 0
			for index in range(0, len(stack) - 1):
				if stack[index] == stack[index + 1]:
					flag = False
					toDel = index
					break
			if len(stack) > n:
				win = False
				stop = True
				stack.pop(n)
				break
			if flag:
				break
			else:
				fr = stack.pop(toDel)
				stack.pop(toDel)
				stack.insert(toDel, fruits[fruits.index(fr) + 1])
				if fruits.index(fr) == 9:
					win = True
					stop = True
					break


	if win:
		print("You win!")
	else:
		print("You lose!")
	space = " "
	print(space.join(stack))
