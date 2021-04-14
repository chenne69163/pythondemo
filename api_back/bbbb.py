# 2、两个有序数组 a=[11,22,33,33,33,44,44,55] b=[22,33,33,44,44,55,55,77,77,88,88],
# 将2个数组进行合并，保证合并后有序，且去重，尽量考虑算法复杂度

# 1、一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）


# 1:
def test1(n):
	if n <= 0:
		return 0

	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
	return b


# 2:
def test2(lst1, lst2):
	res = lst1 + lst2
	set1 = set(res)
	lst = list(set1)
	return quick_sort(lst)


def quick_sort(lst):
	if len(lst) <= 1:
		return lst
	a = lst[0]
	lstl = [x for x in lst if x < a]
	mid = [x for x in lst if x == a]
	lstr = [x for x in lst if x > a]
	left = quick_sort(lstl)
	right = quick_sort(lstr)
	return left + mid + right


def test3(a):
	length = len(a)
	l = int(length / 2)
	left = 0
	while l >= 1:
		while left + l + l <= len(a):
			if a[left:left + l] == a[left + l:left + l + l]:
				return l + l
			left += 1
		l -= 1
	return 0


def test4(ss):
	n = len(ss)
	i = 1
	for j in range(1, n + 1):
		i = i * j
	return i


def nums(s):
	start = 0
	maxlen = 0
	for i in range(len(s)):
		if '0' <= s[i] <= '9':
			length = 0
			tmp = i
			while '0' <= s[i] <= '9':
				i += 1
				length += 1
				if i == len(s):
					break
			if length > maxlen:
				maxlen = length
				start = tmp
	return maxlen, s[start:start + maxlen]


print(nums("abc123de1234f34225671asd123456789"))
