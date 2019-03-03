def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError(f'Strands Must be of equal length. ( Given {strand_a} and {strand_b} )')
    return len([y for x, y in enumerate(strand_a) if strand_a[x] not in strand_b[x]])
