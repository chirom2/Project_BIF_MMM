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
	


#Param d=substitution
def GET_ALLpos(q,s,sa):
	deb = 0
	fin = len(s)
	size_q= len(q)
	size_s= len(s)
	size_sa= len(sa)#CHeck that!!!
	pos = []
	currentSub = 0
	
	while( (fin-deb) >= 0):
		i = (deb+fin)/2
		occ = s[sa[i]:sa[i]+size_q]
		#print(occ)	q == occ
		if(diffS1S2withSub(q,occ,5)):
			pos.append(sa[i])
			endUp = i+1
			endDown = i-1		
			if(endUp < size_sa):#Look Up
				occUp = s[sa[endUp]:sa[endUp]+size_q]
				while( diffS1S2withSub(q,occUp,5) and endUp<size_sa):#(q == occUp or
					print "----------q-----------",q,"----------occUp-----------",occUp
					pos.append(sa[endUp])
					endUp = endUp+1
					occUp = s[sa[endUp]:sa[endUp]+size_q]
			if(endDown > 0):#Look Down
				occDown = s[sa[endDown]:sa[endDown]+size_q]			
				while(diffS1S2withSub(q,occDown,5)  and endDown>0):#(q == occDown or 
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
	
	
def SAmethod(s, read, sizeK, dmax):
	align = alignement
	sa = getSA(s)	
	align.alignementSA(read, dmax, sizeK,s, sa)


def diffS1S2withSub(s1,s2,sub):	
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