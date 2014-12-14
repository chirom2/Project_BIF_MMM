import suffixe_array
import hashtab
import alignement
import tools_MMM
import reverse
import time
import sys
from random import *
import os

#############################

suffixeArray=suffixe_array
hashTable = hashtab
tools=tools_MMM
align = alignement
revrs = reverse

#############################

# Sequence name's file 
file_nameG = sys.argv[1]
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
	file_G = open(file_nameG, 'r')
	s = file_G.readline()	
	if(s[0]=='>'):
		s = file_G.readline()
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
	file_G.close()
	
	#End time counting
	fin = time.time()
	print (fin-debut)


#Dispatch all reads of file_r to alignement
def all_reads(f, s, Ksize, dmax, array, Mode, strand):
	#Result of matching
	fileRes = open("resAlignement.txt", "w")
	toPrint = ""
	#while there are read
	while 1:
		lines = f.readline()
		if not lines:
			break			
		if(lines[0] == '>'):
			toPrint += lines
			lines = f.readline()
			lines = lines.replace("\n",'$')#lines = reads
			#Suffixe array methode
			if(Mode == "SA"):
				#Strand = 0; for both version ,original and reverse complement, of the read
				if(strand==0):
					toPrint += align.alignementSA(lines, dmax, Ksize, s, array, 1)
					toPrint += align.alignementSA(lines, dmax, Ksize, s, array, -1)
				else:
					toPrint += align.alignementSA(lines, dmax, Ksize, s, array, strand)
			#HashTable methode
			elif(Mode == "HT"):
				#Strand = 0, for original and reverse complement of the read
				if(strand==0):
					toPrint += align.alignementHT(lines ,dmax , Ksize, s, array, 1)
					toPrint += align.alignementHT(lines ,dmax , Ksize, s, array, -1)
				else:
					toPrint += align.alignementHT(lines ,dmax , Ksize, s, array, strand)
	#print results to file
	fileRes.write(toPrint)
	print toPrint
	#close file	
	fileRes.close()


Index()
