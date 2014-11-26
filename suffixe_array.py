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

def SA(s):##SA whith LCP LINEAR	
	toolsMMM=tools_MMM
	sa=toolsMMM.simple_kark_sort(s) 
	inv=INV(s,sa)
	LCP_linear(s,sa,inv)
###########################################################################


		

#Return the list of all the kmer present in the genome
#return list of position
def find_kmers(s, sa,kmer_size):
	
	kmersPresent = []#list of kmer present in the genome 
	kmer=""
	for i in range(0, len(s)-kmer_size+1):
		kmer += s[i:i+kmer_size]
		pos = GET_I(kmer, s, sa)
		if(pos != -1):
			kmersPresent.append( pos )		
		kmer=""
	return kmersPresent
      
#Param list of pos      
def printKmer(kmerl):
	for i in range(0, len(kmerl)):
		print kmerl[i]

#param size of kmer
#Return the list of the present kmer in s
def listOfposition(s,k):
	lk = []
	sa = getSA(s)
	print(sa)
	print("SA is ready!")
	kmer = find_kmers(s, k)#TODO change the size of kmer
	print(kmer)
	print("List of kmer is ready!")
	kk = kmer[0:25]
	#print(kk)
	#for i in range(0, len(kmer)):
	pos = GET_I(kk,s,sa)
	if(pos != -1):
		lk = lk.append(pos)
	return lk
	
#return the suffixe array for a sequence s
def getSA(s):
	toolsMMM=tools_MMM
	sa=toolsMMM.simple_kark_sort(s)
	return sa
	
#return the position of a query if it exists else return -1	
def GET_I (q,s,sa):
	deb = 0
	fin = len(s)
	size_q= len(q)
	while( (fin-deb) > 0):
		i = (deb+fin)/2
		occ = s[sa[i]:sa[i]+size_q]
		if(q == occ):
			return sa[i]
		elif(occ>q):
			fin=i-1
		else:
			deb=i+1
	return -1
	
#return the position of a query if it exists else return -1	
def GET_ALL (q,s,sa):
	deb = 0
	fin = len(s)
	size_q= len(q)
	while( (fin-deb) > 0):
		i = (deb+fin)/2
		occ = s[sa[i]:sa[i]+size_q]
		
		if(q == occ):
			return sa[i]
		elif(occ>q):
			fin=i-1
		else:
			deb=i+1
	return -1
	
#Print the suffixe array of the sequence s
def printSA(sa, s):
	for i in range (0, len(sa)):
		print(sa[i], s[sa[i]:])
	
def SAmethod(s,ksize):
	sa = getSA(s)
	print("Sa termine")
	pos = find_kmers(s,sa,ksize)
	printKmer(pos)	

