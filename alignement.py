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
	#suffixeArray.printPos(pos)
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

def alignementHT(read, dmax, sizeK,s, T):
	ht = hashtab
	kRead = ""
	pos = []
	sRead = ""
	sMatch = ""
	sGen = ""
	i=0
	sSize=len(s)
	kRead = read[0:sizeK]#the sizeK first char ex:acgtgtttcca
	print("**********************************************************************")
	print(kRead)
	print("**********************************************************************")

	pos = ht.chain_query(T,kRead,sSize)
	print(pos)
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