class Demo: 
    
    def add(self, nbr= 0, nbr2= 0):
        if type(nbr) is int and type(nbr2) is int:   
            return nbr + nbr2
        else :
            raise(Exception("error"))
