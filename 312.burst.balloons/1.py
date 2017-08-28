#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums):
        '''Solution function description'''
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return nums[0]*nums[1]+max(nums)
        if len(nums) == 3:
<<<<<<< HEAD
            return self.helper(nums)
        res = []
        self.mid(res, 0, nums)
        return max(res)
    def mid(self, total, res, l):
        if len(l) == 3:
            total.append(res+self.helper(l))
            return
        for i,e in enumerate(l):
            if i==0: self.mid(total, res+e*l[i+1], l[0:i]+l[i+1:])
            elif i==len(l)-1: self.mid(total, res+l[i-1]*e, l[0:i]+l[i+1:])
            else: self.mid(total, res+l[i-1]*e*l[i+1], l[0:i]+l[i+1:])
    def helper(self, l):
        return max([l[0]*l[1]*l[2]+l[0]*l[2]+max(l[0],l[2]), l[0]*l[1]+l[1]*l[2]+max(l)])
=======
            return nums[0]*nums[1]*nums[2]+nums[0]*nums[2]+max(nums)
        l = list(x for x, y in sorted(enumerate(nums), key=lambda x: x[1]))
        res = 0
        i = 0
        while i < (len(l) - 3):
            if l[i] == 0: res += nums[l[i]]*nums[l[i]+1]
            elif l[i] == len(nums)-1: res += nums[l[i]-1]*nums[l[i]]
            else: res += nums[l[i]-1]*nums[l[i]]*nums[l[i]+1]
            nums.remove(nums[l[i]])
            l=[l[j]-1 if l[j]>l[i] else l[j] for j in range(len(l))]
            i += 1
        return res+nums[0]*nums[1]*nums[2]+nums[0]*nums[2]+max(nums)
            
>>>>>>> bf94fa262899589c63dfbb68d51d864e13fd4f39

def main():
    '''main function'''
    _solution = Solution()
<<<<<<< HEAD
    inp = [[9, 76,64,21]]
=======
    inp = [[3,1,5,8]]
>>>>>>> bf94fa262899589c63dfbb68d51d864e13fd4f39
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
