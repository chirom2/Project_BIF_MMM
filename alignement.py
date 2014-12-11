import suffixe_array
import hashtab
import tools_MMM
import reverse

revrs = reverse


#Content all functions which could align a kmer with part of the genomez
#param:
#pos = list of pos / indexGen = genome is index / read = read / dmax = substitution numbers
#
def alignementSA(read, dmax, sizeK,s, sa, strand):
	suffixeArray = suffixe_array
	#Empty list of position
	pos = []
	kRead = ""
	sRead = ""
	sMatch = ""
	sGen = ""
	numAlign = 0
	i=0
	#the sizeK first char ex:acgtgtttcca
	if strand == -1:
		read= revrs.reverse(read)
		read = read[1:]
	kRead = read[i:sizeK]
	#list of position
	pos = suffixeArray.GET_ALLpos(kRead,s,sa,dmax)
	size = ((len(read))-1)
	while (i <= len(pos)-1):
		sRead = ""
		sMatch = ""
		sGen = ""
		j=0
		#counter of Gap
		d=0
		#Position on the genome
		x=pos[i]
		while(j < size and d < dmax):
			sRead += read[j]
			sGen += s[x]
			#MissMatch
			if(read[j] != s[x]):				
				sMatch += ':'			
				d += 1
			#Match
			else:
				sMatch += '|'
			j+=1
			x+=1
		#forward in pos
		print " alignement>>",numAlign	
		print " #pos",pos[i]
		print " #strand=",strand
		print " #d=",d	
		print " ",sRead
		print " ",sMatch
		print " ",sGen
		print("\n") 
		i+=1
		numAlign += 1
#
#Alignement for the hashtab
#
def alignementHT(read, dmax, sizeK,s, T, strand):
	ht = hashtab
	kRead = ""
	sRead = ""
	sMatch = ""
	sGen = ""
	numAlign = 0
	i=0
	sSize=len(s)
	pos = []
	if strand == -1:
		read= revrs.reverse(read)
		read = read[1:]
	kRead = read[0:sizeK]#the sizeK first char ex:acgtgtttcca
	pos = ht.chain_query(T,kRead,sSize,dmax)#return a list of list
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
			print " #strand=",strand
			print " #d=",d	
			print " ",sRead
			print " ",sMatch
			print " ",sGen
			print("\n") 
			i+=1	
			numAlign += 1

#return a boolean if the difference between s1 & s2
def diffBetween2S(s1,s2,dmax):
	count=0
	j=0
	i=0
	while(j<len(s2)-1):
		if(s1[i]!=s2[j]):
			count+=1
		j+=1
		i+=1
	if(count<=dmax and i==len(s1)-1):
		return True
	return False
		
def printPos(listPos):
	for i in range(0, len(listPos)):
		print listPos[i]		

