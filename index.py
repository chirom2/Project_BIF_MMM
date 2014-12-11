import suffixe_array
import hashtab
import alignement
import tools_MMM
from random import *
import os

suffixearray=suffixe_array
hashTable = hashtab
tools=tools_MMM
align = alignement

#strand
strand =-1
#Size of seeds
Ksize=20
#Numbers of Gap
dmax=5

def Index():
	typeIndex=raw_input("entrez le choix d'indexation, SA ou HT \n")
	file_name = "test1/reference2.fasta"
	#raw_input("Saisir le nom du ficher a indexer\n")
	
	#Opening Genome's file
	file_s = open(file_name, 'r')
	s = file_s.readline()	
	while(s[0]=='>'):
		s = file_s.readline()
		s = s.replace("\n",'$')#change the last chararcter in $
		
	#Opening Read's file
	file_name = "test1/reads.fasta"
	file_r = open(file_name, 'r')
		
	#Indexation Sufixe Array
	if(typeIndex == "SA" or typeIndex == "sa"):
		print("Indexation par la methode du SA")
		all_reads(file_r, s, Ksize, dmax, 0, "SA",strand)
		
	#Indexation Hashtab
	elif(typeIndex == "HT" or typeIndex == "ht"):
		print("Indexation par table de hash")
		T=hashTable.chain_index(s,Ksize)
		all_reads(file_r, s,Ksize, dmax, T, "HT",strand)
		file_r.close()
		file_s.close()
		
	#Wrong command
	else:
		print("Error: Mauvaise commande")
			
	#Close files
	file_r.close()
	file_s.close()	

#Treat all reads of file_r
def all_reads(f, s, Ksize, dmax, T, Mode, strand):
	while 1:
		lines = f.readline()
		if not lines:
			break			
		if(lines[0] == '>'):
			print(lines)
			lines = f.readline()
			lines = lines.replace("\n",'$')#lines = reads
			if(Mode == "SA"):
				suffixearray.SAmethod(s,lines, Ksize, dmax)
			elif(Mode == "HT"):
				align.alignementHT(lines ,dmax , Ksize, s, T, strand)


Index()
