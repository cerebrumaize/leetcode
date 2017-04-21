
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401


def main():
    '''main function. try
    built-in func https://docs.python.org/2/library/functions.html#built-in-functions
    and bitwise operation on https://wiki.python.org/moin/BitwiseOperators
    '''
    print abs(-7)
    print all([1 == 1, 2 == 2, 3 == 4])
    print any([1 == 1, 2 == 2, 3 == 4])
    print isinstance(u"unicode", basestring), isinstance("unicode", basestring),\
    isinstance(1, basestring)
    print bin(7) #0bxxx, 0b for labeling binary
    print bool(1 == 2)
    print bytearray([97, 123, 59])

if __name__ == "__main__":
    main()
