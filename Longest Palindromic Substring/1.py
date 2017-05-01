
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, s):
        '''
        Solution function description
        '''
        most_left, max_len, s_len, pos, left, right = 0, 1, len(s), 0, 0, 0
        while pos < s_len and s_len-pos > max_len/2:
            left = right = pos
            while right < s_len-1 and s[right+1] == s[right]:
                right += 1

            pos = right + 1

            while right < s_len-1 and left > 0 and s[right+1] == s[left-1]:
                right += 1
                left -= 1

            if max_len < right-left+1:
                most_left = left
                max_len = right-left+1

        return s[most_left : most_left+max_len]

def main():
    '''main function'''
    _solution = Solution()
    a = "alsjfdoabbbafjdso"
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
