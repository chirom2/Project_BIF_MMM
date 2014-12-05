#Indexation functions (SA 
#SA

import tools_MMM
import alignement


###########################################################################
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
	pos = GET_ALLpos(kk,s,sa)
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
		if(q == occ):#We found an occur // we need continue to search around this occur
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
	
def GET_ALLpos(q,s,sa):
	deb = 0
	fin = len(s)
	size_q= len(q)
	size_s= len(s)
	size_sa= len(sa)#CHeck that!!!
	pos = []
	while( (fin-deb) > 0):
		i = (deb+fin)/2
		occ = s[sa[i]:sa[i]+size_q]
		#print(occ)	
		if(q == occ):
			pos.append(sa[i])
			endUp = i+1
			endDown = i-1		
			if(endUp < size_sa):#Look Up
				occUp = s[sa[endUp]:sa[endUp]+size_q]
				while(q == occUp and endUp<size_sa):
					pos.append(sa[endUp])
					endUp = endUp+1
					occUp = s[sa[endUp]:sa[endUp]+size_q]
			if(endDown > 0):#Look Down
				occDown = s[sa[endDown]:sa[endDown]+size_q]			
				while(q == occDown and endDown>0):
					pos.append(sa[endDown])
					endDown = endDown-1
					occDown = s[sa[endDown]:sa[endDown]+size_q]
				endUp = 0
				endDown = 0
				occDown = ""
				occUp = ""					
			if(occ>q):
				fin=i-1
			else:
				deb=i+1					
		elif(occ>q):
			fin=i-1
		else:
			deb=i+1
				
	return pos	
	
def printPos(pos):
	for i in range (0, len(pos)):
		print("i",pos[i])	
	
#Return the list of all the kmer present in the genome
#return list of position
def find_kmers(s, sa,kmer_size):	
	kmersPresent = []#list of kmer present in the genome 
	kmer=""
	for i in range(0, len(s)-kmer_size):
		kmer = s[i:i+kmer_size]
		pos = GET_ALLpos(kmer,s,sa)#pos = all occurences of kmer in s
		if(len(pos)==1):#TODO append = extend 
			kmersPresent.append(pos)
		else:			
			kmersPresent.extend(pos)		
	return kmersPresent



#Print the suffixe array of the sequence s
def printSA(sa, s):
	for i in range (0, len(sa)):
		print(sa[i], s[sa[i]:])
	
def SAmethod(s, read, sizeK, dmax):
	align = alignement
	sa = getSA(s)		
	align.alignement(read, dmax, sizeK,s, sa)


file_name = "test1/reference2.fasta"
#raw_input("Saisir le nom du ficher a indexer\n")
file_s = open(file_name, 'r')
s = file_s.readline()	
while(s[0]=='>'):
	s = file_s.readline()
	s = s.replace("\n",'$')#change the last chararcter in $	
tools = tools_MMM
kmer = "TCTGATGTAATGCGGTTTCCCTTGAAGGATAGGCATAATTTGATTGATCACTTCACTGCGATCTAGCTATGTTTAGAGTAATAGTTTCCAACCCACTGAG"
sa =  getSA(s)
pos = GET_ALLpos(kmer, s, sa)
print(pos)




