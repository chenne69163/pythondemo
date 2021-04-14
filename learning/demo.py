def char_count():
	str = input()
	a = {}
	for i in str:
		if i in a.keys():
			a[i] += 1
		else:
			a[i] = 1

	print(a)


def char_reverse():
	str = input()

	print(str[-1:-len(str) - 1:-1])


if __name__ == "__main__":
	char_count()
	# char_reverse()
