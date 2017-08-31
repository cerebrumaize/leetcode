#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums, k):
        '''Solution function description'''
        res = []
        if k%2 == 1:
            for i in range(0, len(nums)-k+1):
                t = sorted(nums[i: i+k])
                res.append(t[(k-1)//2])
        else:
            for i in range(0, len(nums)-k+1):
                t = sorted(nums[i: i+k])
                res.append((t[k//2]+t[(k-1)//2])/2)
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,4,2,3], 4), ([1,3,-1,-3,5,3,6,7],3)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
