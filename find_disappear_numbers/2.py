
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401

class Solution(object):
    '''Solution description'''
    def find_disappeared_numbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        shorter but longer
        """
        for num in nums:
            nums[abs(num) - 1] = -1 * abs(nums[abs(num) - 1])

        res = []
        for i in xrange(0, len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res

def main():
    '''main function'''
    _solution = Solution()
    res = _solution.find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1])
    print res

if __name__ == "__main__":
    main()
