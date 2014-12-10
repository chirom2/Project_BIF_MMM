import suffixe_array
import hashtab
import tools_MMM



#Content all functions which could align a kmer with part of the genomez
#param:
#pos = list of pos / indexGen = genome is index / read = read / dmax = substitution numbers
#
def alignementSA(read, dmax, sizeK,s, sa):
	suffixeArray = suffixe_array
	kRead = ""
	pos = []
	sRead = ""
	sMatch = ""
	sGen = ""
	i=0
	kRead = read[i:sizeK]#the sizeK first char ex:acgtgtttcca
	pos = suffixeArray.GET_ALLpos(kRead,s,sa)
	size = ((len(read))-1)
	while (i <= len(pos)-1):
		sRead = ""
		sMatch = ""
		sGen = ""
		j=0
		d=0 #counter of Gap
		x=pos[i]
		while(j < (size) and d < dmax):#skip the car '$' 
			sRead += read[j]
			sGen += s[x]	
			if(read[j] != s[x]):				
				sMatch += ':'#misMatch				
				d += 1
			else:
				sMatch += '|'#Match
			j+=1
			x+=1
		i+=1
		print(sRead)
		print(sMatch)
		print(sGen)	
#
#Alignement for the hashtab
#
def alignementHT(read, dmax, sizeK,s, T):
	ht = hashtab
	kRead = ""
	sRead = ""
	sMatch = ""
	sGen = ""
	numAlign = 0
	i=0
	sSize=len(s)
	pos = []
	kRead = read[0:sizeK]#the sizeK first char ex:acgtgtttcca
	pos = ht.chain_query(T,kRead,sSize)#return a list of list
	size = ((len(read))-1)

	if (pos != None and pos != []):
		sizePos = len(pos[0])
		#print "sizePOs ", sizePos
		while(i < sizePos):	
			sRead = ""
			sMatch = ""
			sGen = ""
			j=0
			d=0 #counter of Gap
			x=pos[0][i]#the position ofthe kmer
			#print "len pos", len(pos)
			while(j < (size) and d < dmax):#skip the car '$' 
				sRead += read[j]
				sGen += s[x]	
				if(read[j] != s[x]):				
					sMatch += ':'#misMatch				
					d += 1
				else:
					sMatch += '|'#Match
				j+=1
				x+=1
				
			print " alignement>>",numAlign	
			print " #pos",pos[0][i]
			print " #strand=+",-1#TODO check this parameter
			print " #d=",d	
			print " ",sRead
			print " ",sMatch
			print " ",sGen
			print("\n") 
			i+=1	
			numAlign += 1
		
def printPos(listPos):
	for i in range(0, len(listPos)):
		print listPos[i]		
