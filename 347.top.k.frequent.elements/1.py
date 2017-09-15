#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums, k):
        '''Solution function description'''
        s = set(nums)
        d = {}
        for e in s:
            c = nums.count(e)
            if c not in d: d[c]=[]
            d[c].append(e)
        tmp = [(i, e)for i,e in d.items()]
        tmp.sort(key=lambda x: x[0], reverse=True)
        print(tmp)
        res = []
        for _, e in tmp:
            if len(res) >=k: break
            res += e
        return res[:k]

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,2,2,2,1,1,3],2)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
