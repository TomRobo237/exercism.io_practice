from string import ascii_uppercase
from string import digits
from random import choice
from random import seed
from datetime import datetime

def rand_pre():
    return( choice( ascii_uppercase ) + choice( ascii_uppercase ) )
def rand_num():
    return( choice( digits ) + choice( digits ) + choice( digits ) )

names = []

class Robot(object):
    def __init__( self ):
        seed( datetime.now() )
        self.name = rand_pre() + rand_num()
        if self.name not in names:
            names.append( self.name )
        else:
            self.__init__()
    def reset(self):
        oldname = self.name # Saving oldname for when we remove it later
        self.__init__()     # This gives us a new name
        names.remove( oldname ) # Now we've tested for the old name in the init we can remove the oldname
