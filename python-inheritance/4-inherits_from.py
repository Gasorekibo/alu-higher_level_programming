#!/usr/bin/python3
# only subclass return True
# and False if it is not a subclass
''' we are going to us issubclass function '''



def inherits_from(obj, a_class):
    ''' determine if obj is subclass of a_class '''
    if issubclass(obj, a_class)):
        return True
    else:
        return False
