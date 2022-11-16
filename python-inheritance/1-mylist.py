#!usr/bin/python3
# a class MyList that inherits from list
''' printing a scorted list '''


class Mylist(list):
    ''' defining Mylist class inherted from list '''
    def print_sorted(self):
        ''' return the sorted list '''
        return(sorted(self))
