#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        import heapq
        '''Solution function description'''
        if len(nums) < 3: return False
        runs = {}
        for v in nums:
            if v-1 not in runs:
                if v not in runs:
                    runs[v] = [1]
                else:
                    heapq.heappush(runs[v], 1)
            else:
                length = heapq.heappop(runs[v-1])+1
                if len(runs[v-1]) == 0: del runs[v-1]
                if v not in runs:
                    runs[v] = []
                heapq.heappush(runs[v], length)
        for v, hp in runs.items():
            if len(hp) > 0 and min(hp) < 3:
                return False
        return True

def main():
    '''main function'''
    _solution = Solution()
    inp = [[1,2,3,3,4,4,5,5], [1,2,3,3,4,5], [1,2,3,4,4,5]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
