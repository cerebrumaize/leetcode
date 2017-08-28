#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, l):
        '''Solution function description'''
        res = []
        if len(l) <= 1: return ""
        for i in range(1, len(l)):
            tmp_len = len(min(l[i-1], l[i]))
            for j in range(tmp_len):
                if l[i-1][j] == l[i][j]: continue
                else:
                    res.append([l[i-1][j], l[i][j]])
                    break
        from functools import reduce
        s = list(set(list(reduce(lambda x, y: x+y, res))))
        graph = {}
        visited = {}
        for e in s:
            graph[e] = []
            visited[e] = 0
        for pair in res:
            graph[pair[0]].append(pair[1])
        def noCircle(v, ans):
            if visited[v] == -1: return False
            if visited[v] == 1: return True
            visited[v] = -1
            for u in graph[v]:
                if not noCircle(u, ans): return False
            visited[v] = 1
            ans.append(v)
            return True
        ans = []
        if all(noCircle(i, ans) for i in s): return ''.join(reversed(ans))
        else: return ''

def main():
    '''main function'''
    _solution = Solution()
    inp = [["wrt", 'wrf', 'er', 'ett', 'rftt']]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
