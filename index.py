import suffixe_array
import hashtab
import tools_MMM
from random import *
import os


def Index():
	typeIndex=raw_input("entrez le choix d'indexation, SA ou HT \n")
	file_name = "test1/reference1.fasta"
	#raw_input("Saisir le nom du ficher a indexer\n")
	file_s = open(file_name, 'r')
	s = file_s.readline()	
	while(s[0]=='>'):
		s = file_s.readline()
		s = s.replace("\n",'$')#change the last chararcter in $		
	if(typeIndex == "SA"):
		print("Indexation par la methode du SA")		
		#klist = suffixearray.find_kmers(s, 15)
		#suffixearray.printKmer(klist)
		#sa = suffixearray.getSA(klist)		
		#print(klist)
		#lk = suffixearray.listOfposition(s,25)
		print(lk)
	elif(typeIndex == "HT"):
		print("Indexation par table de hash")
		k=25
		#raw_input("taille des kmer\n")
		n=len(s)
		sa=hashTable.chain_index(s,k,n)
	else:
		print("Error: Mauvaise commande")		


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
Index()

#for i in xrange(len(s)):
#		print i," ",sa[i]," ",LCP[i]," ",s[sa[i]:]," ",inv[i]	

