from stack import Stack


def conv_bin(dec_num):
	s = Stack()
	while dec_num>0:

		reminder= dec_num%2
		s.push(reminder)
		dec_num = dec_num//2

	bin_num =""
	while not s.is_empty():
		bin_num+= str(s.pop())
	return bin_num


print(conv_bin(55))
