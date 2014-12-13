import suffixe_array
import hashtab
import alignement
import tools_MMM
import reverse
import time
import sys
from random import *
import os

suffixeArray=suffixe_array
hashTable = hashtab
tools=tools_MMM
align = alignement
revrs = reverse

# Sequence name's file 
file_nameS = sys.argv[1]
# Reads name's file 
file_nameR = sys.argv[2]
# type of index
typeIndex = sys.argv[3]
#Size of seeds
Ksize = int(sys.argv[4])
#Numbers of Gap
dmax = int(sys.argv[5])
#strand
strand = int(sys.argv[6])

def Index():
	#Start time counting
	debut = time.time()
	
	#Opening Genome's file
	file_s = open(file_nameS, 'r')
	s = file_s.readline()	
	if(s[0]=='>'):
		s = file_s.readline()
		s = s.replace("\n",'$')#change the last chararcter in $
		
	#Opening Read's file
	file_r = open(file_nameR, 'r')
		
	#Indexation Sufixe Array
	if(typeIndex == "SA" or typeIndex == "sa"):
		print("Indexation par la methode du SA")
		sa = tools.simple_kark_sort(s)
		all_reads(file_r, s, Ksize, dmax, sa, "SA",strand)
		
	#Indexation Hashtab
	elif(typeIndex == "HT" or typeIndex == "ht"):
		print("Indexation par table de hash")
		T=hashTable.chain_index(s,Ksize)
		all_reads(file_r, s,Ksize, dmax, T, "HT",strand)
		
	#Wrong command
	else:
		print("Error: Mauvaise commande")
			
	#Close files
	file_r.close()
	file_s.close()
	
	#End time counting
	fin = time.time()
	print (fin-debut)


#Dispatch all reads of file_r to alignement
def all_reads(f, s, Ksize, dmax, array, Mode, strand):
	fileRes = open("resAlignement.txt", "w")
	toPrint = ""
	while 1:
		lines = f.readline()
		if not lines:
			break			
		if(lines[0] == '>'):
			toPrint += lines
			lines = f.readline()
			lines = lines.replace("\n",'$')#lines = reads
			
			if(Mode == "SA"):
				if(strand==0):
					toPrint += align.alignementSA(lines, dmax, Ksize, s, array, 1)
					toPrint += align.alignementSA(lines, dmax, Ksize, s, array, -1)
				else:
					toPrint += align.alignementSA(lines, dmax, Ksize, s, array, strand)
			elif(Mode == "HT"):
				if(strand==0):
					toPrint += align.alignementHT(lines ,dmax , Ksize, s, array, 1)
					toPrint += align.alignementHT(lines ,dmax , Ksize, s, array, -1)
				else:
					toPrint += align.alignementHT(lines ,dmax , Ksize, s, array, strand)
	fileRes.write(toPrint)
	print toPrint	
	fileRes.close()


Index()
