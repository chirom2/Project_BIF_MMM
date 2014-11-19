#Indexation functions (SA 
#SA

import tools_MMM

def INV(s,sa):
	n = len(s)
	inv = [0 for i in range(n)]
	for i in  range(n):
		inv[sa[i]]=i
	return inv

def LCP_linear(s,sa,inv):
	lg=0
	n = len(s)
	depth =0
	lcp= [0 for i in range(n)]
	for k in range(0,n):
		s1 = k		
		s2 = sa[inv[k]-1]
		l = LCP_from_depth(s,depth, s1, s2)
		depth = max(l-1,0)
		lcp[inv[k]] = l
	return lcp	
		
		
def LCP_from_depth(s,depth,pos_s1,pos_s2):
	res = depth
	while (s[pos_s1 + res] == s[pos_s2 + res]):
		res+=1
	return res	
	

	
def GET_I (q,s,sa):
	deb = 0
	fin = len(s)
	size_q= len(q)
	while( (fin-deb) > 0):
		i = (deb+fin)/2
		occ = sa[i:i+size_q]
		if(q == occ):
			return sa[i]
		elif(occ>q):
			fin=i-1
		else:
			de=i+1
	return -1
	


def SA(s):##SA whith LCP LINEAR	
	toolsMMM=tools_MMM
	sa=toolsMMM.simple_kark_sort(s) 
	inv=INV(s,sa)
	LCP_linear(s,sa,inv)
