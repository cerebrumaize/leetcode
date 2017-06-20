
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def __init__(self, nums):
        """type nums: List[int]"""
        self.l = nums

    def sumRange(self, i, j):
        """type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.l[i:j+1])

def main():
    '''main function'''
    _solution = Solution([-2, 0, 3, -5, 2, -1])
    a, b = 2, 4
    res = _solution.sumRange(a, b)
    print(res)

if __name__ == "__main__":
    main()
