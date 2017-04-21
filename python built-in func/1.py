
#!/usr/bin/env python
'''code description'''
import ast
# pylint: disable = I0011, E0401
def cube(side):
    return side ** 3


def main():
    '''main function. try
    built-in func https://docs.python.org/2/library/functions.html#built-in-functions
    and bitwise operation on https://wiki.python.org/moin/BitwiseOperators
    '''
    months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', \
              'September', 'October', 'November', 'December']
    a_d = dict([(0, 'as'), (2, 'dj'), (88, 'so')])
    int_l = [1, 22, 89, 84.89, 234]
    an_iter = (m for m in months)
    hamlet_f = open('./python built-in func/hamlet_act3_scene4.txt')

    print abs(-7), all([1 == 1, 2 == 2, 3 == 4]), any([1 == 1, 2 == 2, 3 == 4])
    print isinstance(u"unicode", basestring), isinstance("unicode", basestring),\
          isinstance(1, basestring)
    print bin(7) #0bxxx, 0b for labeling binary
    print bool(1 == 2), bytearray([97, 123, 59]), callable(basestring)
    print chr(99), classmethod(int) #dont know the usage, what is a func decorator
    print False is None, cmp(1, 3), '\t', cmp('abc', 'abcd'), '\t', cmp(True, False)
    #pinrt compile
    print complex(2, 1)**2, a_d, a_d.get(1, 'N/A'), dir(int_l), divmod(10.3, 2)
    print list(enumerate(months, start=1))
    print isinstance(hamlet_f, file)
    print [x[1] for x in enumerate(months) if x[0] > 6]#better than filter+lambda
    print "{:9.3f}".format(1.11), globals(), hash(a_d.get(0))
    print float.hex(5.484651), id(a_d), int('11', 8)
    print type(an_iter), locals(), max(int_l), map(cube, [1, 2, 3, 4])
    print map(oct, int_l[0:3]), ord('1'), pow(2, 3, 4)

if __name__ == "__main__":
    main()
