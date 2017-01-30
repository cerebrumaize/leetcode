
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401

class Solution(object):
    '''Solution description'''
    def func(self, string):
        '''
        Solution function description
        '''
        res = []
        length = len(string)
        for i in range(0, length):
            res.append(string[length - 1 - i])
        return str(res)

def main():
    '''main function'''
    _solution = Solution()
    res = _solution.func('abcd')
    print res

if __name__ == "__main__":
    main()
