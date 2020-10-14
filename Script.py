from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import FeatureLocation
from Bio.SeqRecord import SeqRecord
import os.path

filename = "/Users/juditharce/Desktop/sequence.gb"
def summarize_contents(filename):
        record = SeqIO.read(filename, "genbank")
        path = os.path.dirname(filename)
        
        print(record.name)
        print('path:', path)
        print(record.id)
        

