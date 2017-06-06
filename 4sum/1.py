
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums, target):
        '''
        Solution function description
        '''
        N = 4
        if len(nums) < N or N < 2:
            return
        nums.sort()
        resL = []
        self.findNSum(nums, target, N, [], resL)
        return resL

    def findNSum(self, nums, target, N, res, resL):
        if target < nums[0]*N or target > nums[-1]*N:
            return
        if N == 2:
            l, r = 0, len(nums)-1
            while l < r:
                if nums[l]+nums[r] == target:
                    resL.append(res+[nums[l]+nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif  nums[l]+nums[r] < target:
                    l += 1
                else: r -= 1
        else:
            for i in xrange(0, len(nums)-N+1):
                if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                    self.findNSum(nums[i+1:], target-nums[i], N-1, res+[nums[i]], resL)

def main():
    '''main function'''
    _solution = Solution()
    res = _solution.func(a, b)
    print res

if __name__ == "__main__":
    main()
