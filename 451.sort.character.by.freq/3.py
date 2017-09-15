#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, s):
        '''Solution function description'''
        res=sorted([[s.count(word), word] for word in set(s)], reverse=True)
        return ''.join([x[0]*x[1] for x in res])

def main():
    '''main function'''
    _solution = Solution()
    inp = ['tree', 'energetic']
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
