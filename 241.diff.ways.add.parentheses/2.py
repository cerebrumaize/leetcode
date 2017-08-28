#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    def func(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        from re import split as resplit
        tokens = resplit('(\D)', input)
        nums = list(map(int, tokens[::2]))
        from operator import add, sub, mul
        ops = list(map({'+':add, '-':sub, '*':mul}.get, tokens[1::2]))
        #if not ops: return nums
        def helper(lo, hi):
            if lo == hi: return [nums[lo]]
            return [ops[i](a, b) for i in range(lo, hi) for a in helper(lo, i) for b in helper(i+1, hi)]
        return helper(0, len(ops))
        
def main():
    '''main function'''
    _solution = Solution()
    inp = ['11']
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
