#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, nums1, nums2, k):
        '''Solution function description'''
        streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
        #map returns an iterator instead of a list, this is the key to why this passed lc
        #for x in streams: print('en? ', [i for i in x])
        from heapq import merge
        stream = merge(*streams)
        from itertools import islice
        #print('stream ', list(stream))
        #print('slice ', list(islice(stream, k)))
        return [sumuv[1:] for sumuv in islice(stream, k)]

def main():
    '''main function'''
    _solution = Solution()
    inp = [([1,1,2], [1,2,3], 2)]
    for i in inp:
        print(_solution.func(i[0], i[1], i[2]))

if __name__ == "__main__":
    main()

'''
input = [([1,1,2], [1,2,3], 2)]
output
streams  [[2, 1, 1], [3, 1, 2], [4, 1, 3]]
         [[2, 1, 1], [3, 1, 2], [4, 1, 3]]
         [[3, 2, 1], [4, 2, 2], [5, 2, 3]]

stream  [[2, 1, 1], [2, 1, 1], [3, 1, 2], [3, 1, 2], [3, 2, 1], [4, 1, 3], [4, 1, 3], [4, 2, 2], [5, 2, 3]]

slice  [[2, 1, 1], [2, 1, 1]]
'''