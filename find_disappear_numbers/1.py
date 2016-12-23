
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401

class Solution(object):
    '''Solution description'''
    def find_disappeared_numbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list1 = []
        for i in xrange(0, len(nums) + 1):
            list1.append(i)

        for i in xrange(0, len(nums)):
            list1[nums[i]] -= nums[i]

        res = []
        for rec in list1:
            if rec > 0:
                res.append(rec)

        return res

def main():
    '''main function'''
    _solution = Solution()
    res = _solution.find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1])
    print res

if __name__ == "__main__":
    main()
