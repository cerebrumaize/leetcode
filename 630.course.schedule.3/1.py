#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, courses):
        '''Solution function description'''
        from heapq import heappush as hpush
        from heapq import heappop as hpop
        duration, hq = 0, []
        if not courses: return 0
        for c in sorted(courses, key=lambda c: c[1]):
            duration += c[0]
            hpush(hq, -c[0])
            print('prev ', hq)
            if duration > c[1]:
                duration += hpop(hq)
            print('post ', hq)
        return len(hq)

def main():
    '''main function'''
    _solution = Solution()
    inp = [[[100,200],[200,1300],[1000,1250],[2000,3200]], [[5,5],[4,6],[2,6]], \
           [[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]]]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
