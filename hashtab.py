#Indexation functions (Hash Table)
import tools_MMM
import alignement
import reverse

#############################

revrs = reverse
align=alignement
tools = tools_MMM

#############################


#Indexation in hashmap chaining
#s = sequence
#k = size of Kmer
#T[ [i, kmer], [i, kmer]... ]
def chain_index(s,k):
	m = len(s)
	found=0
	tools = tools_MMM
	T=[]
	kmer=None
	Ksize=k
	st=""
	for i in range(0,m-1):
		T[i]=T.append(None)		#Init of an empty Table
	for i in range(0,(m - Ksize)):
		st = s[i:(i+Ksize)]
		pos=[i]
		objectkmer=[pos,st]#POS or I [ [list, of ,postion] , "kmer"] => element of the hashtable
		adr = tools.basicHash(objectkmer[1],m)
		if (T[adr] == None):
			T[adr] = [objectkmer]
		else: #the kmer is not present
			for j in range(0,len(T[adr])):				
				k = T[adr][j]
				if (objectkmer[1] == k[1]):#append
					if k[0].count(objectkmer[0][0]) == 0:#the position is not present we add it
						k[0].append(objectkmer[0][0])#add just a postion
					found=1
				if (found==0):
					T[adr].append(objectkmer)						
	return T
	
#found an occcur of w in an hashtab 
#Param: T = HashTab, w = string to found, sSize = size of the indexed text 
#Return: position's list of w, None if w is not present in the hashtab
#hash looks like T[ ]
def chain_query(T,w,sSize,dmax):
	adr= tools.basicHash(w,sSize)
	listPos = []
	if(T[adr] != None):				
		for j in range(0,len(T[adr])):#We don't compare the first postition
			if (align.diffBetween2S(T[adr][j][1],w,dmax)):
				listPos.append(T[adr][j][0])
		return listPos
	return None			

