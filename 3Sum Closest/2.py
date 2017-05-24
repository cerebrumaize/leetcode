
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums, target):
        '''
        Solution function description
        '''
        if nums is None or len(nums) < 3:
            return 0
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        n = len(nums)
        res = nums[0]+nums[1]+nums[2]
        if res >= target:
            return res

        diff = res - target
        for i in xrange(n-2):
            if nums[i] == nums[i-1] and i > 0:
                continue
            l, r = i+1, n-1
            while l < r:
                print i, l, r, diff
                diff = nums[i]+nums[l]+nums[r]-target
                if abs(res-target) >= abs(diff):
                    print 1
                    res = nums[i]+nums[l]+nums[r]
                if diff < 0:
                    print 2
                    l += 1
                if diff > 0:
                    print 4
                    r -= 1
                if diff == 0:
                    return res

        return res



def main():
    '''main function'''
    _solution = Solution()
    a = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]
    b = 0
    '''
    [1,2,4,8,16,32,64,128]
    82
    [0,2,1,-3]
    1
    [1,1,1,90, 0]
    100
    [0,1,2]
    0
    [0,0,0]
    1
    '''
    res = _solution.func(a, b)
    print res

if __name__ == "__main__":
    main()
