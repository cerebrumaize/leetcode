
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, nums, target):
        '''
        Solution function description
        '''
        if nums is None or len(nums) < 3:
            return 0
        if len(nums) == 3:
            return sum(nums)
        sn = sorted(nums)
        dif = sn[0]+sn[1]+sn[len(sn)-1]-target
        res = sn[0]+sn[1]+sn[len(sn)-1]
        for i in xrange(len(sn)-2):
            if sn[i] == sn[i-1] and i > 0:
                continue
            l, r = i+1, len(sn)-1
            while l < r:
                print i, l, r, dif
                dif = sn[i]+sn[l]+sn[r]-target
                if abs(res-target) >= abs(dif):
                    print 1
                    res = sn[i]+sn[l]+sn[r]
                if dif < 0:
                    print 2
                    l += 1
                if dif > 0:
                    print 4
                    r -= 1
                if dif == 0:
                    return res

        return res



def main():
    '''main function'''
    _solution = Solution()
    a = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]
    b = 0
    '''
    [1,2,4,8,16,32,64,128]
    82
    [0,2,1,-3]
    1
    [1,1,1,90, 0]
    100
    [0,1,2]
    0
    [0,0,0]
    1
    '''
    res = _solution.func(a, b)
    print res

if __name__ == "__main__":
    main()
