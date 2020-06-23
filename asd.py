m = 5
#left lower triangle
for x in range(m):
	for y in range(m):
		if y<=x:
			print('*',' ', end='')

	print()

print()

#left upper triangle with desc range logic
for i in range(m,0,-1):
	for j in range(i):

	     print('*',' ', end='')
	print()
	


print()
# square
for i in range(m):
	for j in range(m):
		print('*',' ',end='')
	print()

print()


#left upper triangle
for i in range(m):
	for j in range(m):
		if i<=j :
			
			print('*',' ', end='')
	print()

print()


#forward arrow with m+m rows
for i in range(m):
	for j in range(i+1):
		print("*", end=' ')
	print()
for i in range(m-1,0,-1):
	for j in range(i):
		print('*', end=' ')
	print()




print()
	

#right triangle upper
for i in range(m):
	for j in range(m+1):
		if j < m-i:
			print(' ', end='')
		else:
			print('*', end='')
	print()



print()

# backward arrow with m+m rows
for i in range(m):
	for j in range(m+1):
		if j < m-i:
			print(' ', end='')
		else:
			print('*', end='')
	print()
for i in range(m-1,0,-1):
	for j in range(m+1):
			if j <= m-i:
				print(' ', end='')
			else:
				print('*', end='')
	print()

print()


#right triangle lower
for i in range(m):
	for j in range(m,0,-1):
		if j<=m-i:
			print('*',end='')
		else :
			print(end=' ')
	

	print()
print()


#up arrow with column = m+m
d =m+m
for i in range(m):
	for j in range(m+1):
		if j<m-i:
			print(end=' ')
		else :
			print('*', end='')
	for j in range(m,d):
		if j<m+i:
			print('*', end='')

	print()
	
print()

# down arrow with coloumn = m+m
d = m+m
for i in range(m):
	for j in range(m+1):
		if j <i+1:
			print(' ', end='')
		else:
			print('*', end='')
	for j in range(m+1,d):
		if j< d-i:
			print('*', end='')
		else:
			print(' ', end='') 
		
	print()

print()


# down arrow
if m%2==1:
	m = m+1
for i in range(m):
	for j in range(m):
		if i<j<m-i:
			print('*',end='')
		else:
			print(end=' ')
	print()

print()


# uo arrow
for i in range(m+1):
	for j in range(m):
		if m-j<i>j:
			print('*',end='')
		else:
			print(end=' ')
	print()