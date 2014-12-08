import tools_MMM


#s = sequence
#k = size of Kmer
def chain_index(s,k):
	m = len(s)
	found=0
	tools = tools_MMM
	T=[]
	kmer=[]
	Ksize=k
	st=""
	for i in range(0,m-1):
		T[i]=T.append(None)		#Init of an empty Table
	for i in range(0,(len(s)-k)):
		st = s[i:(i+Ksize)]
		pos=i
		kmer=[i,st]
		adr = tools.basicHash(kmer[1],m)
		if (T[adr] == None):
			T[adr] = [kmer]
		else: #(found = 0)
			for j in range(0,len(T[adr])):
				k = T[adr][j]
				if (kmer[1] == k[1]):
					k[0] = (kmer[0])
					found=1
				if (found==0):
					T[adr].append(kmer)
	return T

def chain_query(T,w,sSize):
	print(T)
	tools = tools_MMM
	adr= tools.basicHash(w,sSize)
	print(adr)
	for j in range(0,len(T[adr])):
		if (T[adr][j][1]==w):
			return T[adr][j][0]
	return -1
