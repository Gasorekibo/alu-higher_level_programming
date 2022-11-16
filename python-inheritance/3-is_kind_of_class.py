#!/usr/bin/python3
# Same class or inherit from
''' determining the instance of object '''


def is_kind_of_class(obj, a_class):
    ''' checking the condition '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
