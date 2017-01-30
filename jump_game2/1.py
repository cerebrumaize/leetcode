
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''
        Solution function description
        '''
        nums_len = len(nums)
        if nums_len == 1:
            return 0
        prev_farest, farest, steps = 0, nums[0], 1
        for ind in xrange(0, nums_len):
            if ind > prev_farest:
                steps += 1
                prev_farest = farest
            farest = max(farest, (nums[ind] + ind))
            if farest >= nums_len - 1:
                return steps


def main():
    '''main function'''
    _solution = Solution()
    nums = [1, 2, 3, 0, 0]
    res = _solution.func(nums)
    print res

if __name__ == "__main__":
    main()
