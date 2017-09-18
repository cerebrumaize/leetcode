#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums1, nums2, k):
        '''Solution function description'''
        from heapq import heappop, heappush
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(queue, [nums1[i]+nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heappop(queue)
            print('pop ', queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j+1)
            print('push ', queue)
            if j == 0:
                push(i+1, 0)
                print('push ', queue)
        return pairs

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,2,3], [1,2,2], 8)]
    for i in inp:
        print(_solution.func(i[0], i[1], i[2]))

if __name__ == "__main__":
    main()
