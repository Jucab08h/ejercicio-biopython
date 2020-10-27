#!/usr/bin/python

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os

#dentro de las comillas va la dirección del archivo genbank
filename =  "/Users/juditharce/Desktop/ls_orchid.gbk"

def summarize_contents(filename):
    file = os.path.basename(filename)
    path = os.path.dirname(filename)
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
