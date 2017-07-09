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
        if not gas or not cost or len(gas) != len(cost) or sum(gas) < sum(cost): return -1
        n = len(gas)
        min_sum, min_ind, total = 0, 0, 0
        for i in range(n):
            total += (gas[i] - cost[i])
            if total < min_sum:
                min_sum = total
                min_ind = i + 1
        return -1 if total < 0 else min_ind

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1, 2, 3], [1, 1, 4]), ([1, 2, 3], [1, 1, 5]), ([2, 3, 1], [1, 5, 1]), ([3, 1, 2], [4, 1, 1])]
    for i in inp:
        print(_solution.canCompleteCircuit(i[0], i[1]))

if __name__ == "__main__":
    main()
