#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, input):
        '''Solution function description'''
        from operator import add, mul, sub
        #tokens = re_split('(\D)', input)
        tokens = [c for c in input]
        nums = list(map(int, tokens[::2]))
        ops = list(map({'+':add, '-':sub, '*': mul}.get, tokens[1::2]))
        def build(lo, hi):
            if lo == hi:
                return [nums[lo]]
            return [ops[i](a, b) for i in range(lo, hi)
                                 for a in build(lo, i)
                                 for b in build(i+1, hi)]
        return build(0, len(nums)-1)

def main():
    '''main function'''
    _solution = Solution()
    inp = ['2*3+1-5']
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
