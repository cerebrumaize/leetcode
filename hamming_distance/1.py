
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401

class Solution(object):
    '''Solution description'''
    def hamming_distance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        i = x ^ y
        return len(('{0:b}').format(i).replace('0', ''))

def main():
    '''main function'''
    _solution = Solution()
    res = _solution.hamming_distance(1, 2)
    print res

if __name__ == "__main__":
    main()
