import tools_MMM

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
	for i in range(0,(len(s)-k)):
		st = s[i:(i+Ksize)]
		pos=[i]
		objectkmer=[pos,st]#POS or I [ [list, of ,postion] , "kmer"] => element of the hashtable
		adr = tools.basicHash(objectkmer[1],m)
		if (T[adr] == None):
			T[adr] = [objectkmer]
		else: #the kmer is not present
			for j in range(0,len(T[adr])):				
				k = T[adr][j]
				#print "k0 ",k[0],"k[1] ",k[1]," kmer[0]",objectkmer[0]," objectkmer[1]", objectkmer[1]
				if (objectkmer[1] == k[1]):#append
					if k[0].count(objectkmer[0]) ==0:#the position is not present we add it
						k[0].append(objectkmer[0][0])#add just a postion
						#print "after append", k[0]
					found=1
				if (found==0):
					T[adr].append(objectkmer)						
	return T
	
#found an occcur of w in an hashtab 
#Param: T = HashTab, w = string to found, sSize = size of the indexed text 
#Return: position's list of w, None if w is not present in the hashtab
#hash looks like T[ ]
def chain_query(T,w,sSize):
	tools = tools_MMM
	adr= tools.basicHash(w,sSize)
	listPos = []
	if(T[adr] != None):		
		for j in range(0,len(T[adr])):
			if (T[adr][j][1]==w):#match exact
				listPos.append( T[adr][j][0])
			elif(diffS1S2withSub(T[adr][j][1],w,5)):
				listPos.append( T[adr][j][0])
				#check if w is in T[adr][j][1] with substitutions	
		printPos(listPos)		
	return listPos		
			

def diffS1S2withSub(s1,s2,sub):
	print "----------s1-----------",s1,"----------s2-----------",s2
	j = 0
	currentSub=0;#Ncurrent substitution in the string
	for i in range(0,len(s1)):
		if(s1[i] == s2[j] and currentSub <= sub):
			j+=1
		elif(s1[i] != s2[j] and currentSub <= sub):
			j+=1
			currentSub += 1		
		else:
			return False	
	return True		
	
def printPos(listPos):
	for i in range(0, len(listPos)):
		print listPos[i]






####################BACK UP#######################
#s = sequence
#k = size of Kmer
#T[ [i, kmer], [i, kmer]... ]
def chain_index222222(s,k):
	m = len(s)
	found=0
	tools = tools_MMM
	T=[]
	kmer=[]
	Ksize=k
	st=""
	
	#Init of an empty Table
	for i in range(0,m-1):
		T[i]=T.append(None)		
	for i in range(0,(len(s)-k)):
		st = s[i:(i+Ksize)]
		pos=i

		kmer=[pos,st]#

		#use of hash function
		adr = tools.basicHash(kmer[1],m)
		if (T[adr] == None):
			T[adr] = [kmer]
		else: #the kmer is not present
			for j in range(0,len(T[adr])):
				
				k = T[adr][j]
				#print "kmer[0] ",kmer[0]
				print "k0 ",k[0],"k[1] ",k[1]," kmer[0]",kmer[0]," kmer[1]", kmer[1]
				if (kmer[1] == k[1]):#append
										
					k[0] = (kmer[0])
					found=1
				if (found==0):
					T[adr].append(kmer)			
	return T
	




#To found position of w in the hashmap T
def chain_queryWHAT(T,w,sSize):
	tools = tools_MMM
	adr= tools.basicHash(w,sSize)
	if(T[adr]!=None):
		print(T[adr])
		for j in range(0,len(T[adr])):
			if (T[adr][j][1]==w):
				return T[adr][j][0]
	return -1
