def binary_search(arr, l, r, x):
	if r >= l:
		mid = int(l + (r - l) / 2)
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, l, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, r, x)
	else:
		return l - 1


if __name__ == '__main__':
	dic_words = input().split(" ")
	article = input().split(" ")
	ans = []
	dic_words.sort()
	#print(dic_words)
	for word in article:
		index = binary_search(dic_words, 0, len(dic_words) - 1, word)
		ans.append(dic_words[index])
	space = " "
	print(space.join(ans))