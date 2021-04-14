class linkNode:

	def __init__(self, data):
		self.data = data
		self.next = None


class sigLink:
	"""
	链表3要素：长度，head，tail
	"""

	def __init__(self, item):
		self.length = len(item)
		if self.length <= 0:
			return
		i = 0
		self.head = linkNode(item[i])
		self.tail = self.head
		i += 1
		while i < self.length:
			self.tail.next = linkNode(item[i])
			self.tail = self.tail.next
			i += 1

	def printlink(self):
		if self.head == None:
			print("空")
		p = self.head
		while p != None:
			print(p.data, end=" ")
			p = p.next

	def printlength(self):
		print("长度为", self.length)

	def linkAppend(self, num):
		self.tail.next = linkNode(num)
		self.tail = self.tail.next
		self.length += 1

	def insertNode(self, index, num):
		"""
			在链表中间插入节点
			index：插入节点的序号
			num：插入点的值
		"""
		if index > self.length:
			print("index参数超出范围")
			return
		if index == self.length:
			self.linkAppend(num)
			return
		if index == 0:
			p = linkNode(num)
			p.next = self.head
			self.head = p
			self.length += 1
			return
		ptemp = self.head
		while index > 1:
			ptemp = ptemp.next
			index -= 1
		p = linkNode(num)
		p.next = ptemp.next
		ptemp.next = p
		self.length += 1


if __name__ == "__main__":
	a = sigLink([1, 2, 3, 4])
	a.printlink()
	print("")
	a.insertNode(2,10)
	a.printlink()
	print("")
	a.printlength()
	print("")
	a.linkAppend(15)
	a.printlink()
