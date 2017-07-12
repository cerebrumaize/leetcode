#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, tasks, n):
        '''Solution function description'''
        if not tasks: return 0
        d = {}
        for c in tasks: d[c] = d[c]+1 if c in d else 1
        l = sorted(d, key=lambda x: d[x], reverse=True)
        tmp = 0
        for i in l:
            if d[i] == d[l[0]]: tmp += 1
            else: break
        return max(len(tasks), (1+n)*(d[l[0]]-1)+tmp)

def main():
    '''main function'''
    _solution = Solution()
    inp = [(['A','A','A','B','B','B'], 2), (['A','A','A','B','B','B', 'C'], 2)]
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
