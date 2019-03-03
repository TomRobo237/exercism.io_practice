CODONS = {'Methionine': ['AUG'],
            'Phenylalanine' : ['UUU', 'UUC'],
            'Leucine': ['UUA', 'UUG'],
            'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
            'Tyrosine': ['UAU', 'UAC'],
            'Cysteine':['UGU', 'UGC'],
            'Tryptophan': ['UGG'],
            'STOP': ['UAA', 'UAG', 'UGA']}

def proteins(strand):
    triplets = [ strand[i:i+3] for i in range(0, len(strand), 3)]
    my_proteins = []
    for x in triplets:
        for y in CODONS.keys():
            if x in CODONS[y]:
                if y == 'STOP':
                    return my_proteins
                my_proteins.append(y)
    return my_proteins

