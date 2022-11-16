#!/usr/bin/python3
# only sub class will return True
# otherwise return True
''' we are not allowed to import any module
    and we are going to use isinstance '''



def inherits_from(obj, a_class):
    ''' determine if obj is subclass of a_class '''
    if issubclass(type(obj), a_class)) and type(obj) != a_class:
        return True
    else:
        return False
