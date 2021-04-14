class Solution:

	def __init__(self, lst):
		self.lst = lst

	def test(self):
		if len(self.lst) == 0:
			return 0
		else:
			for j in range(len(self.lst) - 1):
				for i in range(len(self.lst) - 1):
					if self.lst[i] > self.lst[i + 1]:
						self.lst[i], self.lst[i + 1] = self.lst[i + 1], self.lst[i]
			return self.lst


class Fibonacci:

	def __init__(self, num):
		self.num = num

	def test(self):
		if self.num <= 1:
			return 1
		else:
			return Fibonacci.test(Fibonacci(self.num - 1)) + Fibonacci.test(Fibonacci(self.num - 2))


class Add:

	def __init__(self, lst, target):
		self.target = target
		self.lst = lst

	def test(self):
		for i in range(len(self.lst)):
			for j in range(i + 1, len(self.lst)):
				for x in range(j + 1, len(self.lst)):
					if self.target - self.lst[i] - self.lst[j] == self.lst[x]:
						return self.lst[i], self.lst[j], self.lst[x]
					else:
						continue


if __name__ == '__main__':
	a = list(map(int, (input().split())))
	max = a[0]
	for i in a:
		if max < i:
			max = i
	print(max)
	# b = int(input())
	# for i in range(len(a)):
	# for j in range(len(a) - 1):
	# 	if a[j] > a[j + 1]:
	# 		a[j], a[j + 1] = a[j + 1], a[j]
	# for i in range(1, len(a) - 1):
	# 	if sum(a[0:i]) == sum(a[i + 1:]):
	# 		print(i)
	# 		break
	# old_x = c
	# rev = 0
	# while c != 0:
	# 	pop = c % 10
	# 	c = int(c / 10)
	# 	rev = rev * 10 + pop
	# print(rev)
# b = int(input())
# 	c = Add(a, b)
# 	print(c.test())
# print(sum(a[0:c]))
# print(sum(a[c + 1:]))
# b = Fibonacci(a)
# print(b.test())
# print(0xFFFFFFFF)
# print(a & 0xFFFFFFFF)
# print(bin(0xFFFFFFFF))
# if a < 0:
# 	print(bin(a & 0xFFFFFFFF).count('1'))
# else:
# 	print(bin(a).count('1'))
# print(len(a))
# print(len(set(a)))
# k = len(set(a))
# while k > 0:
# 	for i in range(len(a) - k + 1):
# 		if len(a[i:i + k]) == len(set(a[i:i + k])):
# 			print(k)
# 			break
# 	k -= 1
