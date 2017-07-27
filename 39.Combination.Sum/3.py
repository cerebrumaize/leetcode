#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, candidates, target):
        '''Solution function description'''
        res = []
        self.helper(res, [], candidates.sort(), target)
        return res

    def helper(self, total_res, part_res, options, t):
        '''solution helper'''
        if t < 0: return
        elif t > 0:
            for i, e in list(enumerate(options)):
                if t < e: return
                self.helper(total_res, part_res+[e], options[i:], t-e)
        else:
            total_res.append(part_res)
            return

def main():
    '''main function'''
    _solution = Solution()
    inp = [([2, 3, 6, 7], 7)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
