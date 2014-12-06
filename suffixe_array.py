#Indexation functions (SA 
#SA

import tools_MMM
import alignement


###########################################################################

	
#return the suffixe array for a sequence s
def getSA(s):
	toolsMMM=tools_MMM
	sa=toolsMMM.simple_kark_sort(s)
	return sa
	

	
def GET_ALLpos(q,s,sa):
	deb = 0
	fin = len(s)
	size_q= len(q)
	size_s= len(s)
	size_sa= len(sa)#CHeck that!!!
	pos = []
	while( (fin-deb) >= 0):
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
	


#Print the suffixe array of the sequence s
def printSA(sa, s):
	for i in range (0, len(sa)):
		print(sa[i], s[sa[i]:])
	
def SAmethod(s, read, sizeK, dmax):
	align = alignement
	sa = getSA(s)	
	align.alignement(read, dmax, sizeK,s, sa)



