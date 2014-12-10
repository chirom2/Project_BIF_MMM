

def reverse(r):
	rev=""
	for i in range(0,len(r)-1):
		if r[i]=='A':
			rev+='T'
		elif r[i]=='T':
			rev+='A'
		elif r[i]=='C':
			rev+='G'
		elif r[i]=='G':
			rev+='C'
	return rev
