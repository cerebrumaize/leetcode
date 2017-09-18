#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321, C0326

class Solution(object):
    '''Solution description'''
    def func(self, n):
        '''Solution function description'''
        from heapq import heappop, heappush
        pool = [2,3,5]
        def push(res):
            for i in pool:
                if res*i not in queue: heappush(queue, res*i)
        queue, res, cnt = [1], 1, 0
        while queue and cnt < n:
            res = heappop(queue)
            cnt += 1
            if cnt <= n: push(res)
        return res

def main():
    '''main function'''
    _solution = Solution()
    inp = [1600]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
