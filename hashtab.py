import tools_MMM

def chain_index(s,k,m):
	tools = tools_MMM
	kmer={'st':"",'pos':0}
	T=[m]#table vide de m élément
	for i in range(0,(len(s)-k)):
		kmer.st = s[i:(i+k)]
		kmer[pos] = i
		adr = tools.basicHash(kmer,m)
		if (T[adr] == ""):
			T[adr] = [kmer]
		else: #(found = 0)
			for j in range(0,len(t[adr])):
				if (T[adr][j].str==kmer.str):
					T[adr][j].pos.append(kmer.pos)
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
