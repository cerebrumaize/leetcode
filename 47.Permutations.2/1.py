#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def permuteUnique(self, nums):
        '''Solution function description'''
        if not nums: return []
        if len(nums) == 1: return [nums]
        nums.sort()
        res = []
        self.helper(res, [], nums)
        return res
    def helper(self, total_res, part_res, options):
        '''solution helper func'''
        if not options:
            total_res.append(part_res)
            return
        saved_e = options[0] - 1
        for i, e in enumerate(options):
            if saved_e == e: continue
            saved_e = e
            self.helper(total_res, part_res+[e], options[:i]+options[i+1:])

def main():
    '''main function'''
    _solution = Solution()
    inp = [[1,1,2,3], [1,3], [1, 4, 1]]
    for i in inp:
        print(_solution.permuteUnique(i))

if __name__ == "__main__":
    main()
