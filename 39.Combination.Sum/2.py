#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''
    @param candidates, a list of integers
    @param target, integer
    @return a list of lists of integers
    '''
    def func(self, candidates, target):
        '''solution func'''
        candidates.sort()
        res = []
        self.DFS(candidates, target, 0, res, [])
        return res

    def DFS(self, candidates, target, start, res, intermedia):
        '''solution dfs'''
        if target == 0:
            res.append(intermedia)
            return
        for i in range(start, len(candidates)):
            if target < candidates[i]:
                return
            self.DFS(candidates, target-candidates[i], i, res, intermedia+[candidates[i]])

def main():
    '''main function'''
    _solution = Solution()
    inp = [([8, 7, 4, 3], 7)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
