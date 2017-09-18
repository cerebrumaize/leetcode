#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums1, nums2, k):
        '''Solution function description'''
        from heapq import heappop, heappush
        heap = []
        if nums2:
            for i in range(min(k,len(nums1))):
                heappush(heap, (nums1[i] + nums2[0], i, 0))
        pairs = []
        while len(pairs) < k and heap:
            _,i,j = heappop(heap)
            pairs.append((nums1[i],nums2[j]))
            j += 1
            if j < len(nums2):
                heappush(heap, (nums1[i] + nums2[j], i, j))
        return pairs

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,1,2], [1,2,3], 2)]
    for i in inp:
        print(_solution.func(i[0], i[1], i[2]))

if __name__ == "__main__":
    main()
