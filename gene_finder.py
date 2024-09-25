from Bio import SeqIO

def readFASTA(file):
	record = list(SeqIO.parse(file,"fasta"))
	genome = ''
	for i in range(len(record)):
		genome+=record[i].seq
	N=len(genome)
	start_codon = "ATG"
	stop_codons = ["TAA","TAG","TGA"]
	amino_acids = []
	stop = False
	idx2 = 0

	while stop==False:
		for i in range(idx2,N):
			if i==(N-1):
				stop=True
				break
			if genome[i:i+3]==start_codon:
				idx1=i
				break
		for i in range(idx1,N,3):
			if (i+3)>(N-1):
				stop=True
				break
			if genome[i:i+3] in stop_codons:
				idx2=i
				amino_acids.append(genome[idx1:idx2+3])
				break
	return amino_acids
