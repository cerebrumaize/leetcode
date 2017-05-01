
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def get_mid(self, nums, pivot, pos):
        sl, ml, bl, p = [], [], [], nums[pos-1]
        print pos, nums
        for num in nums:
            if num < p:
                sl.append(num)
            elif num == p:
                ml.append(num)
            elif num > p:
                bl.append(num)
        print pos, sl, ml, bl
        if pos <= len(sl):
            return self.get_mid(sl, pos)
        elif pos <= len(sl) + len(ml):
            return p
        else:
            return self.get_mid(bl, pos-len(sl)-len(ml))

    def func(self, nums1, nums2):
        '''
        Solution function description
        '''
        length = len(nums1) + len(nums2)
        if length & 1 == 1:
            return self.get_mid(nums1+nums2, len(nums2), (length + 1) / 2)
        else:
            return (self.get_mid(nums1+nums2, len(nums2), length/2)+self.get_mid(nums1+nums2, len(nums2), 1+length/2))*0.5

def main():
    '''main function'''
    _solution = Solution()
    a = [1, 3]
    b = [2]
    res = _solution.func(a, b)
    print res

if __name__ == "__main__":
    main()
