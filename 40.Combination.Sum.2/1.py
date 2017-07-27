#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, candidates, target):
        '''Solution function description'''
        res = []
        self.helper(res, [], sorted(candidates), target)
        return res

    def helper(self, total_res, part_res, candidates, target):
        '''Solution function description'''
        if target < 0: return
        if target == 0:
            if part_res in total_res: return
            total_res.append(part_res)
            return
        for i, e in enumerate(candidates):
            if e > target: return
            self.helper(total_res, part_res+[e], candidates[i+1:], target-e)

def main():
    '''main function'''
    _solution = Solution()
    inp = [([10,1,2,7,6,1,5], 8)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
