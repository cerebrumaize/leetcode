
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, s, words):
        '''
        Solution function description
        '''
        word_len = len(words[0])
        d = {}
        for ind in xrange(0, len(s)):
            print s[ind, ind + word_len]
            if s[ind, ind + word_len] in words:
                if s[ind, ind + word_len] in d:
                    d[s[ind, ind + word_len]].append(ind)
                else:
                    d[s[ind, ind + word_len]] = ind
        print d

def main():
    '''main function'''
    _solution = Solution()
    res = _solution.func(a, b)
    print res

if __name__ == "__main__":
    main()
