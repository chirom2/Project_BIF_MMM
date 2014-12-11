
#reverse all the string
def reverse(r):
	rev=""
	for i in range(0,len(r)-1):
		rev += reverseAux(r[i])
	return rev

#reverse one car
def reverseAux(i):
	if i=='A':
		i='T'
	elif i=='T':
		i='A'
	elif i=='C':
		i='G'
	elif i=='G':
		i='C'
	return i