#!/usr/bin/python

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os.path

filename = input ("ingrese la dirección de su archivo genbank: ")

def summarize_contents(filename):
        file = os.path.basename(filename)
        path = os.path.dirname(filename)
        print("file:", file)
        print("path:", path)
       
        num_records = list(SeqIO.parse (filename, "genbank"))
        print("num_records: %i records" % len(num_records))
        print("records: ")
	



summarize_contents(filename)        

