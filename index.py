import suffixe_array
import hashtab
import alignement
import tools_MMM
from random import *
import os


def Index():
	typeIndex=raw_input("entrez le choix d'indexation, SA ou HT \n")
	file_name = "test1/reference2.fasta"
	#raw_input("Saisir le nom du ficher a indexer\n")
	file_s = open(file_name, 'r')
	s = file_s.readline()	
	while(s[0]=='>'):
		s = file_s.readline()
		s = s.replace("\n",'$')#change the last chararcter in $		
	if(typeIndex == "SA"):
		print("Indexation par la methode du SA")
		file_name = "test1/reads.fasta"
		file_r = open(file_name, 'r')
		all_reads(file_r, s)
		file_r.close()
		file_s.close()
	elif(typeIndex == "HT"):
		print("Indexation par table de hash")
		k=19
		#raw_input("taille des kmer\n")
		n=len(s)
		sa=hashTable.chain_index(s,k,n)
	else:
		print("Error: Mauvaise commande")		

def all_reads(f,s):
	while 1:
		lines = f.readline()
		if not lines:
			break			
		if(lines[0] == '>'):
			print(lines)
			lines = f.readline()
			lines = lines.replace("\n",'$')#lines = reads
			suffixearray.SAmethod(s,lines, 20,5)
#For test: Generate a sequence of size n
def generate_seq(n):
	seq = ""
	for i in range(0, n):
		seq+=choice("acgt")
	seq+='$'
	return (seq)


suffixearray=suffixe_array
hashTable = hashtab
tools=tools_MMM
align = alignement
Index()
