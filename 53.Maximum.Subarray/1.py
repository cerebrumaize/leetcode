#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''Solution function description'''
        if not nums:
            return 0
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            #think this as adding sum to cur num, thus once the sum < 0
            #there is no meaning in adding more number. just recount cur_sum
            cur_sum = max(num, num+cur_sum)
            max_sum = max(max_sum, cur_sum)
        return max_sum

def main():
    '''main function'''
    _solution = Solution()
    inp = []
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
