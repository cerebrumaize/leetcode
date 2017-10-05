#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321
from collections import abc
class Solution(object):
    '''Solution description'''
    def func(self, n, primes):
        '''Solution function description'''
        if n == 1: return 1
        inds = [0]*len(primes)
        nums = [1]
        while n > 1:
            min_num = min([nums[inds[i]]*primes[i] for i in range(len(inds))])
            for i in range(len(inds)):
                if min_num == nums[inds[i]]*primes[i]: inds[i]+=1
            nums.append(min_num)
            n -= 1
        return nums[-1]

def main():
    '''main function'''
    _solution = Solution()
    inp = [
           (1,[2,3,5]),
           (20,[2,3,5])
    ]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
