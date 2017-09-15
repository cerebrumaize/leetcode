#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, s):
        '''Solution function description'''
        d={}
        for c in s:
            if c not in d: d[c]=1
            else: d[c]+=1
        res = list(d.items())
        res.sort(key=lambda x:x[1], reverse=True)
        return ''.join([k*v for k,v in res])

def main():
    '''main function'''
    _solution = Solution()
    inp = ['tree', 'energetic']
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
