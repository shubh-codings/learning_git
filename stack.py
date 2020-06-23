class Stack():
	def __init__(self):
		self.items = []
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def get_stack(self):
		return self.items
	def is_empty(self):
		return self.items==[]
	def peek(self):
		if not self.isEmpty:
			return self.items[-1]
"""
s = Stack()
s.push("ram")
s.push("sita")
print(s.get_stack())
s.pop()
print(s.get_stack())
"""
def rev_string(stack,input_string):
	for i in range(len(input_string)):
		stack.push(input_string[i])
	rev_string = ""
	while not stack.is_empty():
		rev_string += stack.pop()
	return rev_string


stack = Stack()
input_string = "shubham"
print(rev_string(stack,input_string))