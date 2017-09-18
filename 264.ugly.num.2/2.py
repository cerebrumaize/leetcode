#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321, C0326

NUMS = [1]

i2,i3,i5=0,0,0
while len(NUMS)<1700:
    UMIN = min(2*NUMS[i2],3*NUMS[i3],5*NUMS[i5])
    NUMS.append(UMIN)
    if UMIN == 2*NUMS[i2]: i2+=1
    if UMIN == 3*NUMS[i3]: i3+=1
    if UMIN == 5*NUMS[i5]: i5+=1

class Solution(object):
    '''Solution description'''
    def func(self, n):
        '''Solution function description'''
        return NUMS[n-1]

def main():
    '''main function'''
    _solution = Solution()
    inp = [1600, 1601, 1602, 1609]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
