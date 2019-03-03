# sum is a function, using mysum instead for variable.
def square_of_sum(count):
    mysum=0
    for i in range( 1 , count + 1 ):
        mysum=mysum + i
    return mysum ** 2

def sum_of_squares(count):
    mysum=0
    for i in range( 1 , count + 1 ):
        mysum=mysum + i ** 2
    return mysum

def difference(count):
    return square_of_sum( count ) - sum_of_squares( count )
