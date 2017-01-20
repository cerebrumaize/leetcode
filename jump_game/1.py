
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401

class Solution(object):
    '''Solution description'''
    def canJump(self, nums):
        '''
        Solution function description
        '''
        nums_l = len(nums)
        if nums_l == 1:
            return True
        elif nums_l == 2:
            if nums[0] >= 1:
                return True
            else:
                return False
        else:
            del nums[-1]
            canJump(nums)

def main():
    '''main function'''
    _solution = Solution()
    nums = [0, 2, 3]
    res = _solution.canJump(nums)
    print res

if __name__ == "__main__":
    main()
