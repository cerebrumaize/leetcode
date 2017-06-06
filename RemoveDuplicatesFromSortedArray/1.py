
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''
        Solution function description
        '''
        if nums is None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        i, cur = 1, 0
        while i < len(nums):
            if nums[i] != nums[cur]:
                print cur, i
                nums[cur+1] = nums[i]
                cur += 1
            i += 1
            print nums
        return cur+1


def main():
    '''main function'''
    _solution = Solution()
    a = [2, 2, 3, 3, 455]
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
