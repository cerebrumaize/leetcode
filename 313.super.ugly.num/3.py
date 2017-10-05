#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, n, primes):
        '''Solution function description'''
        from heapq import heappush, heappop
        heap, uglies, idx, ugly_by_last_prime = [], [0]*n, [0]*len(primes), [0]*n
        uglies[0] = 1
        for k, p in enumerate(primes):
            heappush(heap, (p, k))
        for i in range(1, n):
            uglies[i], k = heappop(heap)
            ugly_by_last_prime[i] = k
            idx[k] += 1
            while ugly_by_last_prime[idx[k]] < k:
                idx[k] += 1
            heappush(heap, (primes[k]*uglies[idx[k]], k))
        return uglies[-1]

def main():
    '''main function'''
    _solution = Solution()
    inp = [(1,[2,3,5])]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
