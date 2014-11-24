import suffixe_array
import hashtab
import tools_MMM
from random import *
import os


def Index():
	typeIndex=raw_input("entrez le choix d'indexation, SA ou HT \n")
	file_name = "test2/reads_1K.fasta"#raw_input("Saisir le nom du ficher a indexer\n")
	file_s = open(file_name, 'r')
	
	s = file_s.readline()	
	while(s[0]=='>'):
		s = file_s.readline()
		s = s.replace("\n",'$')#change the last chararcter in $		
	if(typeIndex == "SA"):
		print("Indexation par la methode du SA")
		sa=tools.simple_kark_sort(s)
		#printSA(sa, s)
	elif(typeIndex == "HT"):
		print("Indexation par table de hash")
		k=5#raw_input("taille des kmer\n")
		n=len(s)
		sa=hashtab.chain_index(s,k,n)
	else:
		print("Error: Mauvaise commande")		


#For test: Generate a sequence of size n
def generate_seq(n):
	seq = ""
	for i in range(0, n):
		seq+=choice("acgt")
	seq+='$'
	return (seq)


#Print the suffixe array of the sequence s
def printSA(sa, s):
	for i in range (0, len(sa)):
		print(sa[i], s[sa[i]:])
	


suffixearray=suffixe_array
tools=tools_MMM
Index()

#for i in xrange(len(s)):
#		print i," ",sa[i]," ",LCP[i]," ",s[sa[i]:]," ",inv[i]	

