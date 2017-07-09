#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas or not cost or len(gas) != len(cost): return -1
        n = len(gas)
        tmp = [gas[i]-cost[i] for i in range(n)]
        #print(tmp)
        for i in range(n):
            if tmp[i] < 0: continue
            t = 0
            for j in range(i, n+i):
                t += tmp[j-n]
                if t < 0: break
            if t >= 0: return i
        return -1

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1, 2, 3], [1, 1, 4]), ([1, 2, 3], [1, 1, 5]), ([2, 3, 1], [1, 5, 1]), ([3, 1, 2], [4, 1, 1])]
    for i in inp:
        print(_solution.canCompleteCircuit(i[0], i[1]))

if __name__ == "__main__":
    main()
