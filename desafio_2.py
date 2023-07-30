#!/usr/bin/env python3

#pra tratar de dna
from Bio import SeqIO

#calcula a porcentagem de bases em relação ao total
from Bio.SeqUtils import gc_fraction

import glob

output= open("gc_content.txt", "w")

for file in glob.glob("*.fna"):
	for seq_record in SeqIO.parse(file, "fasta"):
		gc = gc_fraction(seq_record.seq)

		escreva = file + "\t" + str(gc) + "\n"
		output.writelines(escreva)

output.close()