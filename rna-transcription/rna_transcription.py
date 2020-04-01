def to_rna(dna_strand):
    rna_strand = {'G': 'C','C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join(rna_strand[i] for i in dna_strand)
