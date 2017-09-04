#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, A, B):
        '''Solution function description'''
        if len(A) <= 1: return A
        if A[-1] == -1: return []
        if len(A) <= B: return [A[0], A[-1]]
        def helper(total, path, coins, pos, A, B):
            if len(A) - pos <= B:
                total.append((coins+A[-1], path+[len(A)-1]))
                return
            for i in range(pos, pos+B):
                if A[i] == -1: continue
                helper(total, path+[i], coins+A[i], i+1, A, B)
        res = []
        path = []
        helper(res, path, 0, 0, A, B)
        return min(res)[1]

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,2,4, -1, 2], 2)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
