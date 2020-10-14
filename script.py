#!/usr/bin/python

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import FeatureLocation
from Bio.SeqRecord import SeqRecord
import os.path

filename = input ("ingrese la dirección de su archivo genbank: ")
def summarize_contents(filename):
        record = SeqIO.read(filename, "genbank")
        path = os.path.dirname(filename)
        records = list(SeqIO.parse (filename, "genbank"))

        print("name: ", record.name)
        print("path:", path)
        print("num_records: %i records" % len(records))
        print("ID: ", record.id)

summarize_contents(filename)        

