def slices(series, length):
    if not 0 < length <= len(series): # Testing if length is NOT inbetween 0 and length of series
        raise ValueError("Length of return set must be greater than 0 or less than length of series")
    return [series[x:x+length] for x in range(len(series) - length + 1)]
