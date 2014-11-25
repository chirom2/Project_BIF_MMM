import tools_MMM

def chain_index(s,k,m):
	#first elem = str
	#second elem = pos
	found=0
	tools = tools_MMM
	T=[]
	for i in range(0,m-1):
		T[i]=T.append(None)		#Init of an empty Table
	for i in range(0,(len(s)-k)):
		st = s[i:(i+k)]
		#print(st)
		kmer = {'str':st, 'pos':i}
		adr = tools.basicHash(kmer['str'],m)
		if (T[adr] == None):
			T[adr] = [kmer]
		else: #(found = 0)
			for j in range(0,len(T[adr])):
				k = T[adr][j]
				print(k)
				if (kmer['str'] == k['str']):
					k['pos'] = (kmer['pos'])
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
