
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Interval(object):
    '''Interval description
    '''
    def __init__(self, s=0, e=0):
        '''Interval init description
        '''
        self.start = s
        self.end = e

class Solution(object):
    '''Solution description
    '''
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        for x in sorted(intervals, key=lambda x: x.start):
            if res and x.start <= res[-1].end:
                res[-1].end = max(res[-1].end, x.end)
            else:
                res.append(x)

def main():
    '''main function'''
    _solution = Solution()
    b = [0,1,2]
    res = _solution.merge(a, b)
    print res

if __name__ == "__main__":
    main()
