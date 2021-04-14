def test(lst1, lst2):
	res = lst1 + lst2
	r = quick(res)
	return r


def quick(lst):
	if len(lst) <= 1:
		return lst
	a = lst[0]
	lstl = [x for x in lst if x < a]
	mid = [x for x in lst if x == a]
	lstr = [x for x in lst if x > a]
	left = quick(lstl)
	right = quick(lstr)
	return left + mid + right


print(test([1, 3, 5], [2, 4, 6]))


# [1,2],[3,4]
# [],[]
# 非法(非lst类型) lst里非int类型
# [1,2],[]
# [],[1,2]
# [1,3],[2,4]
# [2,4],[1,3]

def test2(lst1, lst2):
	res = []
	m1 = 0
	n1 = 0
	m = len(lst1)
	n = len(lst2)
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
	return list(set(res))

print(test2([1,1,3,5],[2,4,6,7,8,9]))