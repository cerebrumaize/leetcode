
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums1, nums2):
        '''
        Solution function description
        '''
        len1, len2, left1, right1, left2, right2 = len(nums1), len(nums2), [], [], [], []
        if len1 & 1 == 1:
            left1 = nums1[0:(len1-1)/2]
            right1 = [nums1[(len1-1)/2]] + nums1[1+(len1-1)/2: len1-1]
        else:
            left1 = nums1[0:-1+len1/2]
            right1 = nums1[len1/2: len1-1]

        if len2 & 1 == 1:
            left2 = nums2[0:(len2-1)/2]
            right2 = [nums2[(len2-1)/2]] + nums1[1+(len2-1)/2: len2-1]
        else:
            left2 = nums2[0:-1+len2/2]
            right2 = nums2[len2/2: len2-1]
        if left1[-1]

def main():
    '''main function'''
    _solution = Solution()
    a = [1, 3]
    b = [2]
    res = _solution.func(a, b)
    print res

if __name__ == "__main__":
    main()
