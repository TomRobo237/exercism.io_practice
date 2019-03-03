def is_pangram(sentence):
    # Creating a set of all lowercase, using ord a - z for readability
    # Need that + 1 b/c range will be one short
    alphabet = set(map(chr, range(ord('a'), ord('z') + 1)))
    # If the lowercase string is a superset of alphabet, return true
    # This accounts for other characters such as whitespace  
    if set(sentence.lower()) >= alphabet:
        return(True)
    else:
        return(False) 
