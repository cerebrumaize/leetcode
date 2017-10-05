#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, n, primes):
        '''Solution function description'''
        from heapq import heappush, heappop
        tmp = [1]+primes[:]
        while n:
            res = heappop(tmp)
            for p in primes:
                if p*res not in tmp: heappush(tmp, p*res)
            n -= 1
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [(1,[2,3,5])]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
