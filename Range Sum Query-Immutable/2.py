
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def __init__(self, nums):
        """type nums: List[int]"""
        count, self.dp = 0, [0]
        for i in nums:
            count += i
            self.dp.append(count)
    def sumRange(self, i, j):
        """type i: int
        :type j: int
        :rtype: int
        """
        n = len(self.dp)
        l = 0 if i < 0 else i
        r = n-1 if j > n-1 else j
        return self.dp[j+1]-self.dp[i]

def main():
    '''main function'''
    _solution = Solution([-2, 0, 3, -5, 2, -1])
    a, b = 2, 4
    res = _solution.sumRange(a, b)
    print(res)

if __name__ == "__main__":
    main()
