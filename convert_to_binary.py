""" creating a program that can convert a decimal to binary number using stack"""
from stack import Stack

dec_number = int(input("Please input a decimal number."))
s = Stack()
while dec_number> 0:
    reminder = dec_number % 2
    s.push(reminder)
    dec_number = dec_number//2

bin_num = ""
for item in range(s.size()):
    bin_num = bin_num +str(s.pop())

print(bin_num)
