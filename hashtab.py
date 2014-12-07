import tools_MMM

def chain_index(s,k,m):
	#first elem = str
	#second elem = pos
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
				print(k)
				if (kmer[1] == k[1]):
					k[0] = (kmer[0])
					found=1
				if (found==0):
					T[adr].append(kmer)					

def chain_query(T,w):
	tools = tools_MMM
	adr= tools.basicHash(w,len(T))
	for j in range(0,len(T[adr])):
		if (T[adr][j].str==w):
			return [adr][j].pos
	return -1
