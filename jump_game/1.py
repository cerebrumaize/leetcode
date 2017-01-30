
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103
class Solution(object):
    '''Solution description'''
    def canJump(self, nums):
        '''Solution func description'''
        max_step = 0
        for ind in xrange(0, len(nums)):
            if ind > max_step:
                return False
            max_step = max(max_step, nums[ind] + ind)

        return True

def main():
    '''main function'''
    _solution = Solution()
    nums = [7, 2, 3]
    res = _solution.canJump(nums)
    print res

if __name__ == "__main__":
    main()
