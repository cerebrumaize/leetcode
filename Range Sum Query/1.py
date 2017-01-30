
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.ls, self.li, self.lj = 0, 0, 0

    '''Solution description'''
    def func(self, nums, target):
        '''
        Solution function description
        '''
        res = 0
        if (self.li == self.lj == self.ls == 0) |\
           (i>self.lj) |\
           (j<self.li):
            for ind in xrange(i, j + 1):
                res += self.nums[ind]
                self.li=i
                self.lj=j
                self.ls=res
            return res
        elif (i<=self.li) & (j<=self.lj):
            for ind in xrange(i, self.li + 1):
                self.ls+=self.nums[ind]
            for ind in xrange(j, self.lj + 1):
                self.ls-=self.nums[ind]
        elif (i<=self.li) & (self.lj<j):
            for ind in xrange(i, self.li + 1):
                self.ls+=self.nums[ind]
            for ind in xrange(self.lj, j + 1):
                self.ls+=self.nums[ind]
        elif (self.li<i) & (j<=self.lj):
            for ind in xrange(self.li, i + 1):
                self.ls-=self.nums[ind]
            for ind in xrange(j, self.lj + 1):
                self.ls-=self.nums[ind]
        elif (self.li<i) & (self.lj<j):
            for ind in xrange(self.li, i + 1):
                self.ls-=self.nums[ind]
            for ind in xrange(self.lj, j + 1):
                self.ls+=self.nums[ind]

def main():
    '''main function'''
    _solution = Solution()
    res = _solution.func(a, b)
    print res

if __name__ == "__main__":
    main()
