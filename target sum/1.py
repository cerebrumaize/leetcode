#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''bad Solution, timeout'''
    def helper(self, l, cur_res, cnt, S):
        if not l: return
        if len(l) == 1:
            cnt[0] += int(cur_res+l[0] == S)
            cnt[0] += int(cur_res-l[0] == S)
        self.helper(l[:-1], cur_res+l[-1], cnt, S)
        self.helper(l[:-1], cur_res-l[-1], cnt, S)
    def func(self, nums, S):
        '''Solution function description'''
        cnt = [0]
        self.helper(nums, 0, cnt, S)
        return cnt[0]
def main():
    '''main function'''
    _solution = Solution()
    inp = [([1, 1, 1, 1, 1], 3)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
