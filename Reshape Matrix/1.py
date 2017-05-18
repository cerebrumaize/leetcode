
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums, r, c):
        '''
        Solution function description
        '''
        if (len(nums)*len(nums[0]) != r*c) | ((len(nums)*len(nums[0]) == r*c)&(len(nums[0]) == c)):
            return nums
        temp = []
        for row in nums:
            temp += row
        print 'debug temp: ', temp
        if r == 1:
            return [temp]

        res = []
        for i in xrange(r):
            res.append(temp[i*c+0:i*c+c])
        return res

def main():
    '''main function'''
    _solution = Solution()
    l = [[1], [2], [3], [4]]
    res = _solution.func(l, 1, 4)
    print res

if __name__ == "__main__":
    main()
