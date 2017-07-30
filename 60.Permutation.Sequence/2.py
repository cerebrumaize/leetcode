#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

import math
class Solution(object):
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def func(self, n, k):
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation

def main():
    '''main function'''
    _solution = Solution()
    inp = [(3, 4)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()