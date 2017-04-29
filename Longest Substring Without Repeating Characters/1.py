
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def get_pos(self, s, c):
        for i in xrange(len(s)):
            if s[i] == c:
                return i
    def func(self, s):
        """
        :type s: str
        :rtype: int
        """
        buf_str, cur_str = [], []
        for i in xrange(len(s)):
            print len(cur_str)
            if (len(cur_str) == 0) or (s[i] not in cur_str):
                cur_str.append(s[i])
            elif s[i] in cur_str or i == len(cur_str) - 1:
                if len(cur_str) > len(buf_str):
                    buf_str = cur_str[:]
                repeat_pos = self.get_pos(cur_str, s[i])
                cur_str = cur_str[repeat_pos + 1: len(cur_str)] + [s[i]]
        if len(buf_str) < len(cur_str):
            buf_str = cur_str[:]
        print cur_str, buf_str
        return len(buf_str)

def main():
    '''main function'''
    _solution = Solution()
    a = "bpfbhmipxf"
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
