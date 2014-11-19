
import suffixe_array
from random import *
import os


def Index():
	typeIndex=raw_input("entrez le choix d'indexation, SA ou HT \n")
	file_name = raw_input("Saisir le nom du ficher a indexer\n")
	file_s = open(file_name, 'r')
	
	s = file_s.readline()	
	while(s[0]=='>'):
		s = file_s.readline()
	s += '$'		
	if(typeIndex == "SA"):
		print("Indexation par la methode du SA")
		suffixearray.SA(s)
	elif(typeIndex == "HT"):
		print("Indexation par table de hash")
	else:
		print("Error: Mauvaise commande")		

def generate_seq(taille):
	seq = ""
	for i in range(0, taille):
		seq+=choice("acgt")
	seq+='$'
	return (seq)


suffixearray=suffixe_array
s = generate_seq(20)
Index()

#for i in xrange(len(s)):
#		print i," ",sa[i]," ",LCP[i]," ",s[sa[i]:]," ",inv[i]	

