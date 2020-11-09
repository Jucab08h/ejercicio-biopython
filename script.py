#!/usr/bin/python

from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os.path

filename =  os.path.abspath("data/ls_orchid.gbk")
def summarize_contents(filename):
    file = os.path.basename(filename)
    path = os.path.dirname(filename)
    tipexten = os.path.splitext(filename)
    if(tipexten[1] == ".gbk"):
        tipo = "genbank"
    else:
        tipo = "fasta"
        pass
    num_records = list(SeqIO.parse(filename, "genbank"))
    
#el diccionario 
    Dic = {}    
    Dic['file:'] = file
    Dic['path:'] = path
    Dic['num_records:'] = len(num_records)
    
     #lista en el diccionario
    Dic['names:'] = []
    Dic['id:'] = []
    Dic['descriptions:'] = []
    for Seq_Record in SeqIO.parse(filename, "genbank"):
        Dic['names:'].append(Seq_Record.name)
        Dic['id:'].append(Seq_Record.id)
        Dic['descriptions:'].append(Seq_Record.description)
    return Dic
if __name__ == "__main__":
    resultado = summarize_contents(filename)
    print(resultado)


        #secuencias que se desean concatenar 
Seq1 = Seq("agtgagactcgaggg")
Seq2 = Seq("AgTgAGAaaTtT")

def concatenate_and_get_reverse_of_complement(Seq1, Seq2):
    secuencia = Seq1 + Seq2  #concatenar 
    inverso = secuencia.reverse_complement() #invertir 

    print(inverso)

concatenate_and_get_reverse_of_complement(Seq1, Seq2)
