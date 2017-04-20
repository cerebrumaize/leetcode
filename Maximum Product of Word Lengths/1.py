
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def get_number(self, s):
        l = []
        for c in xrange(26):
            l.append("0")
        for c in s:
            if l[122-ord(c)] != '1':
                l[122-ord(c)] = "1"
        print "".join(c for c in l), len("".join(c for c in l))
        return int("".join(c for c in l), 2)
    def func(self, words):
        '''
        Solution function description
        '''
        d = {}
        for w in words:
            d[self.get_number(w)] = max(len(w), d.get(self.get_number(w), 0))
        return max([d[x]*d[y] for x in d for y in d if not x&y] or [0])

def main():
    '''main function'''
    _solution = Solution()
    a = ["abc", 'skspodfk']
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
