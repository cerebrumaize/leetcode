#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums, k):
        '''Solution function description'''
        d = {}
        s = set(nums)
        for i in s:
            c = nums.count(i)
            if c not in d: d[c]=[]
            d[c].append(i)
        from heapq import heapify, heappop
        tmp = [(x,y)for x, y in d.items()]
        tmp = heapify(tmp)
        res = []
        while len(res) < k:
            res += tmp.heappop()
        return res[:k]

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,1,1,2,3,2], 3)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
