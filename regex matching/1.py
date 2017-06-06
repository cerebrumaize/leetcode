
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, s, p):
        '''
        Solution function description
        '''
        if len(s) <= 1 and len(p) <= 1:
            if len(s) == 0 and len(p) == 0:
                return True
            elif len(s) == len(p) == 1:
                if s[0] == p[0] or s[0] == '.' or p[0] == '.':
                    return True
            else:
                return False
        i = j = 1
        while i < len(p):
            if i == '.':
                self.isMatch(s[i+1:], p[j+1:])
            elif i == '*':
                while j < len(s):



def main():
    '''main function'''
    _solution = Solution()
    a = "aa"
    b = "a*"
    res = _solution.isMatch(a, b)
    print res

if __name__ == "__main__":
    main()
