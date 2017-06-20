#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, s, wordDict):
        '''Solution function description'''
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1: i+1] and ((d[i-len(w)]) or i-len(w) == -1):
                    d[i] = True
                    continue
        return d[-1]
def main():
    '''main function'''
    _solution = Solution()
    res, inp = [], [('words', ['word', 'words', 'list'])]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
