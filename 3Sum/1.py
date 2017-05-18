
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''
        Solution function description
        '''
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            print i, l, r
            while l < r:
                s = nums[l] + nums[i] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[l], nums[i], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while r > l and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

def main():
    '''main function'''
    _solution = Solution()
    a = [-1,0,1,2,-1,-4]
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
