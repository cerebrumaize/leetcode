
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401

class Solution(object):
    '''Solution description'''
    def func(self, upper):
        '''
        Solution function description
        '''
        res = []
        temp = ''
        for i in xrange(1, upper + 1):
            if (i % 5 == 0) & (i % 3 == 0):
                temp = 'FizzBuzz'
            elif i % 5 == 0:
                temp = 'Buzz'
            elif i % 3 == 0:
                temp = 'Fizz'
            else:
                temp = str(i)
            res.append(temp)

        return res


def main():
    '''main function'''
    _solution = Solution()
    res = _solution.func(167348964)

if __name__ == "__main__":
    main()
