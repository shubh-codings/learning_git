def factorial(n):
	if n==1:
		return 1;

	result = n*factorial(n-1)
	return result


def TOH(n,source, target, aux):
	global count
	if n>=1:
		TOH(n-1,source,aux,target)
		target.append(source.pop())
		count= count+1
		TOH(n-1,aux,target,source)



def fib(n):
	if n==1 or n==2:
		return 1
	else :
		return fib(n-1)+fib(n-2)

		
#print(factorial(3))
n = 6
source = list(range(n,0,-1))
target = []
aux = []
count = 0

print(source)
print(target)
print('-----------------')
TOH(n,source,target,aux)
print(source)
print(target)
print('count is' ,count)
print(fib(6))



