def largest_product(series, size):
    if size < 0:
        raise ValueError( 'Error' )
    results = []
    for i in range( 0 , len( series ) + 1 ):
        total = 1
        this_group = list(series[ i : size + i ])
        if len( this_group ) < size:
            continue
        for j in this_group:
            total *= int( j )
        results.append( total )
    return max( results )
