#Alignement functions
import suffixe_array
import hashtab
import tools_MMM
import reverse
import os

#############################

revrs = reverse
suffixeArray = suffixe_array

#############################

#Content all functions which could align a kmer with part of the genomez
#param:
#pos = list of pos / indexGen = genome is index / read = read / dmax = substitution numbers
def alignementSA(read, dmax, sizeK,s, sa, strand):
	#Empty list of position
	pos = []
	#initializing of local variables
	sRead = ""
	sMatch = ""
	sGen = ""
	currentAling = ""
	toPrint = ""
	numAlign = 0
	#indice to traverse the table
	#first position of the read in the genome
	i=0
	#reverse complement of the read
	if strand == -1:
		read = revrs.reverse(read)
		read = read[1:]+'$'
	#the sizeK first char ex:acgtgtttcca
	kRead = read[0:sizeK]
	#list of position
	pos = suffixeArray.getAllPos(read,s,sa,dmax)
	#size of the read
	RSize = ((len(read))-1)
	while (i <= len(pos)-1):
		sRead = ""
		sMatch = ""
		sGen = ""
		currentAling = ""
		j=0
		#counter of Gap
		d=0
		#Position on the genome
		x=pos[i]
		while(j < RSize and d < dmax):
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
		
		if j == RSize and d <= dmax:
			currentAling += " alignement>> "+str(numAlign)+"\n"	
			currentAling += " #pos"+str(pos[i])+"\n"
			currentAling += " #strand="+str(strand)+"\n"
			currentAling += " #d="+str(d)+"\n"
			currentAling += " "+str(sRead)+"\n"
			currentAling += " "+str(sMatch)+"\n"
			currentAling += " "+str(sGen)+"\n"
			currentAling +=("\n")
			toPrint += currentAling
		#forward in pos
		i+=1
		numAlign += 1
	return toPrint
#
#Alignement for the hashtab
#
def alignementHT(read, dmax, sizeK,s, T, strand):
	#initializing of local variables
	currentAling = ""
	toPrint = ""
	ht = hashtab
	kRead = ""
	sRead = ""
	sMatch = ""
	sGen = ""
	numAlign = 0
	#indice to traverse the table
	#first position of the read in the genome
	i=0
	#genome's size
	sSize=len(s)
	pos = []
	#reverse complement of the read
	if strand == -1:
		read= revrs.reverse(read)
		read = read[1:]+'$'
	kRead = read[0:sizeK]#the sizeK first char ex:acgtgtttcca
	pos = ht.chain_query(T,kRead,sSize,dmax)#return a list of list
	RSize = ((len(read))-1)
	if (pos != None and pos != []):
		sizePos = len(pos[0])
		#print "sizePOs ", sizePos
		while(i < sizePos):	
			sRead = ""
			sMatch = ""
			sGen = ""
			currentAling = ""
			j=0
			d=0 #counter of Gap
			x=pos[0][i]#the position ofthe kmer
			while(j < RSize and d < dmax):#skip the car '$' 
				sRead += read[j]
				sGen += s[x]	
				if(read[j] != s[x]):				
					sMatch += ':'#misMatch				
					d += 1
				else:
					sMatch += '|'#Match
				j+=1
				x+=1
			if j == RSize and d <= dmax:
				currentAling += " alignement>> "+str(numAlign)+"\n"	
				currentAling += " #pos"+str(pos[0][i])+"\n"
				currentAling += " #strand="+str(strand)+"\n"
				currentAling += " #d="+str(d)+"\n"
				currentAling += " "+str(sRead)+"\n"
				currentAling += " "+str(sMatch)+"\n"
				currentAling += " "+str(sGen)+"\n"
				currentAling +=("\n")
				toPrint += currentAling
			#forward in pos
			i+=1	
			numAlign += 1
	return toPrint		


#return a boolean if the difference between s1 & s2 is in the interval [0,dmax]
def diffBetween2S(s1,s2,dmax):
	#counter of gap
	count=0
	j=0
	i=0
	#chearching difference
	while(j<len(s2)-1):
		if(s1[i]!=s2[j]):
			count+=1
		j+=1
		i+=1
	if(count<=dmax and i==len(s1)-1):
		return True
	return False

#methode toString for pos
def printPos(listPos):
	for i in range(0, len(listPos)):
		print listPos[i]		
