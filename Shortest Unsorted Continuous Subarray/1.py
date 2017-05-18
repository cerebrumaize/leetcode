
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''
        Solution function description
        '''
        sorted_nums = sorted(nums)
        for left in xrange(len(nums)):
            if nums[left] != sorted_nums[left]:
                break
        for right in reversed(range(len(nums))):
            if nums[right] != sorted_nums[right]:
                break
        return 0 if right <= left else right - left + 1

def main():
    '''main function'''
    _solution = Solution()
    b = [1, 2, 5, 2, 51, 624, 56, 865]
    res = _solution.func(b)
    print res

if __name__ == "__main__":
    main()
