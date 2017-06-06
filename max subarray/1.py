
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''
        Solution function description
        '''
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
    a = [-2,1,-3,4,-1,2,1,-5,4]
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
