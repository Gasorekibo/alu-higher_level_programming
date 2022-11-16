#!/usr/bin/python3
# a class MyList that inherits from list
''' define a class MyList '''


class Mylist(list):
    '''defining the class that inherited from list '''

    def print_sorted(self):
    ''' function that print sorted list '''
    return(sorted(self))
