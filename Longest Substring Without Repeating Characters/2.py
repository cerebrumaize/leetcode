
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, maxLength = 0, 0
        usedChar = {}
        for i in xrange(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i
        return maxLength

def main():
    '''main function'''
    _solution = Solution()
    a = "bpfbhmipxf"
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
