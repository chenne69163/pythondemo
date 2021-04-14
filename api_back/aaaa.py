# 快排，反转链表，二分查找，二维数组排序

def quickSort(listx):
	if len(listx) <= 1:
		return listx
	pivot = listx[0]  # 取一个基准值pivot
	listl = [x for x in listx if x < pivot]  # <pivot的放在一个列表
	listm = [x for x in listx if x == pivot]  # =pivot的放在一个列表
	listr = [x for x in listx if x > pivot]  # >pivot的放在一个列表
	left = quickSort(listl)  # 递归进行该函数
	right = quickSort(listr)  # 递归进行该函数
	return left + listm + right  # 整合


def ListNode(pHead):
	a = pHead
	b = None
	while a:
		tmp = a.next
		a.next, b = b, a
		a = tmp
	return b


def cntest(lst):
	if len(lst) <= 1:
		return lst
	pivot = lst[0]
	lstl = [x for x in lst if x < pivot]
	lstm = [x for x in lst if x == pivot]
	lstr = [x for x in lst if x > pivot]
	left = cntest(lstl)
	right = cntest(lstr)
	return left + lstm + right


def search(nums, target):
	if target not in nums:
		return -1
	left, right = 0, len(nums) - 1
	index = -1
	while left <= right:
		mid = left + (right - left) // 2
		if nums[mid] == target:
			index = mid
		if nums[mid] < target:
			left = mid + 1
		if nums[mid] >= target:
			right = mid - 1
	return index


def twoSort(ls1, ls2):
	ls1 = ls1 if type(ls1) is list else [ls1]
	result = []
	len1, len2, i, j = len(ls1), len(ls2), 0, 0
	while i < len1 and j < len2:
		if ls1[i] <= ls2[j]:
			result.append(ls1[i])
			i += 1
		else:
			result.append(ls2[j])
			j += 1
	result += ls1[i:] + ls2[j:]
	return result


# 递归操作
def merge_sort(c):
	if len(c) <= 1:
		return c
	mid = len(c) // 2  # 除法取整
	a = merge_sort(c[:mid])
	b = merge_sort(c[mid:])
	return twoSort(a, b)


def two_sum(lst, n):
	length = len(lst)
	for i in range(length):
		for j in range(i + 1, length):
			if lst[i] + lst[j] == n:
				return True
	return False


def max_str(s):
	st = {}
	i, ans = 0, 0
	for j in range(len(s)):
		if s[j] in st:
			i = max(st[s[j]], i)
		ans = max(ans, j - i + 1)
		st[s[j]] = j + 1
	return ans


def strtest(s):
	dic = {}
	i, ans = 0, 0
	for j in range(len(s)):
		if s[j] in dic:
			i = max(i, dic[s[j]])
		ans = max(ans, j - i + 1)
		dic[s[j]] = j + 1
	return ans


def easy_dp(array):
	n = len(array)
	m = array[0]
	res = array[0]
	for i in range(1, n):
		m = max(m + array[i], array[i])
		if res <= m:
			res = m
	return res


def add2(lst1, lst2):
	res = []
	m = len(lst1)
	n = len(lst2)
	m1, n1 = 0, 0
	while m1 < m and n1 < n:
		if lst1[m1] < lst2[n1]:
			res.append(lst1[m1])
			m1 += 1
		else:
			res.append(lst2[n1])
			n1 += 1
	while m1 < m:
		res.append(lst1[m1])
		m1 += 1
	while n1 < n:
		res.append(lst2[n1])
		n1 += 1
	return res


# 丢手绢问题：
# 在幼儿园小红、小花以及其他同学，
# 共21个小朋友围成一个圈玩游戏，
# 第一个人从1开始报数，报6的将被淘汰掉，
# 下一个人接着从1开始报。如果最终剩下小红和小花，
# 那么他们俩应该在哪个位置


def queue(m, n):
	a = list(range(1, m + 1))
	count = 0
	while True:
		if len(a) == 2:
			break
		count += 1
		x = a.pop(0)
		if count == n:
			count = 0
			continue
		a.append(x)
	return a


if __name__ == "__main__":
	print(merge_sort([1, 9, 7, 3, 5, 2, 6, 7, 100, 1, 3]))
	a = [1, 2, 3, 2, 3, 2, -2]
	print(two_sum(a, 0))
	print(max_str("abcbcdaabcdewsfr"))
	print(search([1, 2, 3, 5], 1))
	print(strtest("abcbcdaabcdewsfr"))

	# 选出所有课成绩都大于80分的 select distinct name from class where score not in (select distinct name from class where score < 80)
	# m*n的矩阵从右上到左下打印出来，
	# 例：[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	# 输出 4 3 8 2 7 12 1 6 11 16 5 10 15 9 14 13,
	b = [
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9, 10, 11, 12],
		[13, 14, 15, 16]
	]
	c = [
		[1, 2, 3],
		[5, 6, 7],
		[9, 10, 11],
	]
	m = len(b)
	n = len(b[0])
	l = m * n
	res = []
	for k in range(l):
		for i in range(m):
			for j in range(m):
				if j - i == m - k - 1:
					res.append(b[i][j])
	print(res)

	res1 = []
	top, left = 0, 0
	right = n - 1
	bot = m - 1
	while left <= right + 1 & top <= bot + 1:
		for i in range(left, right + 1):
			res1.append(b[top][i])
		top += 1
		for i in range(top, bot + 1):
			res1.append(b[i][right])
		right -= 1
		for i in range(right, left - 1, -1):
			res1.append(b[bot][i])
		bot -= 1
		for i in range(bot, top - 1, -1):
			res1.append(b[i][left])
		left += 1
	print(res1)

	print(easy_dp([1, -2, 3, 10, -4, 7, 2, -5]))

	print(add2([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))
