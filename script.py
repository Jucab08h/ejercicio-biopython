#!/usr/bin/python

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import os.path

filename = " "
# ingrese dentro de las comillas la dirección de su archivo genbank

def summarize_contents(filename):
        file = os.path.basename(filename)
        path = os.path.dirname(filename)

      #comienza la cadena
        cadena = " "
        cadena = ("file: "+ file)
        cadena += ("\npath: " + path)
        num_records = list(SeqIO.parse(filename, "genbank"))
        cadena += ("\nnum_records: " + str(len(num_records)))
        cadena += ("\nrecords: ")

        for Seq_Record in SeqIO.parse(filename, "genbank"):
                num_records.append(Seq_Record) #agregamos otro a la lista
                cadena += ("\n\n- id:" + str(Seq_Record.id))
                cadena += ("\nname:" + Seq_Record.name)
                cadena += ("\ndescription:" + str(Seq_Record.description))
        return cadena

result = summarize_contents(filename)
print(result)
