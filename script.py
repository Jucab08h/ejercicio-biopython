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
       
        num_records = list(SeqIO.parse(filename, "genbank"))
        print("num_records: %i " % len(num_records))
        print("records: ")
        
        records = []
        for Seq_Record in SeqIO.parse(filename, "genbank"):
                records.append(Seq_Record) #agregamos otro a la lista
                print("- id: ", Seq_Record.id)
                print("  name: ", Seq_Record.name)
                print("  description: ", Seq_Record.description)

summarize_contents(filename)

