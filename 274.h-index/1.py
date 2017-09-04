#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        citations = sorted(citations)
        i = len(citations)-1
        while (citations[i]>=len(citations)-i) and i>=0:
            i -= 1
        return len(citations)-i-1

def main():
    '''main function'''
    _solution = Solution()
    inp = [[3, 0, 6, 1, 5], [3, 0, 6, 1, 4, 5], [100]]
    for i in inp:
        print(_solution.hIndex(i))

if __name__ == "__main__":
    main()
