if __name__ == '__main__':
	s1 = "Brave "
	s2 = "nothing "
	s3 = "fear "
	s4 = "niu "
	print("{0}{3}{2}{1}".format(s1, s2, s3, s4 * 2))
	print("{0}{1}{3}{2}".format(s1, s2, s3, s4[0:-1] * 2 + " "))
	print("{0}{3}{2}{1}".format(s1, s2, s3, s4[0:3] * 2 + " "))
	#print("{0}{3[0:3]*2+" "}{2}{1}".format(s1, s2, s3, s4))