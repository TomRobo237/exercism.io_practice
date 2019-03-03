def convert(nucleotide):
    if nucleotide == 'G':
        return('C')
    elif nucleotide == 'C':
        return('G')
    elif nucleotide == 'T':
        return('A')
    elif nucleotide == 'A':
        return('U')

def to_rna(dna_strand):
    output=''
    for i in list(dna_strand):
        output= output + convert(i)
    return(output)

