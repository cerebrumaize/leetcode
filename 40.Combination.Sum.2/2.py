#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, candidates, target):
        '''Solution function description'''
        res = []
        candidates.sort()
        def helper(nums, path, target):
            '''Solution function description'''
            res = []
            if target == 0:
                res.append(path)
                return
            for i, num in enumerate(nums):
                if num > target: break
                if i > 0 and num == nums[i-1]: continue
                helper(nums[i+1:], path+[num], target-num)
        helper(candidates, [], target)
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [([10,1, 1, 1,2,7,6,1,5], 4)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
