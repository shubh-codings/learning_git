colors = ['red', 'blue', 'white', 'green', 'purple']
bases = ['delhi','mumbai','agra','dehradun']
for o ,color in enumerate(colors):
	print( o ,' : ', colors[o])
for base ,color in zip(bases,colors):
	print(base,' : ',color)
print(type(zip(bases,colors)))