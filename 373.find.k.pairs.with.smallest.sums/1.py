#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums1, nums2, k):
        '''Solution function description'''
        d = {}
        for i in nums1:
            for j in nums2:
                if i+j not in d: d[i+j]=[[i,j]]
                else: d[i+j].append([i,j])
        res = []
        for k,v in sorted(d.items(), key=lambda x:x[0]):
            res += v
            if len(res) >= k: break
        return res[:k]

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,1,2], [1,2,3], 2)]
    for i in inp:
        print(_solution.func(i[0], i[1], i[2]))

if __name__ == "__main__":
    main()
