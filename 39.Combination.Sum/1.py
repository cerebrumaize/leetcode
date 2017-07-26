#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def helper(self, total_res, part_res, options, t):
        '''solution helper'''
        if sum(part_res) > t: return
        elif sum(part_res) < t:
            for i, e in list(enumerate(options)):
                self.helper(total_res, part_res+[e], options[i:], t)
        else: total_res.append(part_res)

    def func(self, candidates, target):
        '''Solution function description'''
        res = []
        self.helper(res, [], candidates, target)
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [([2,3,6,7], 7)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
