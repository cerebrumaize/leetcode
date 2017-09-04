#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, num, target):
        '''Solution function description'''
        def dfs(start, length, remain, cur, result):
            if (remain == 0
                and ((length == 4 and cur < 12)
                or (length == 6 and cur < 60))):
                result.append(cur)
                return
            for i in range(start, length):
                dfs(i + 1, length, remain - 1, cur + 2 ** (length - i - 1), result)
        ret = []
        for top in range(0, num + 1):
            bottom = num - top
            # calculate possible top results
            top_results = []
            dfs(0, 4, top, 0, top_results)
            # calculate possible bottom results
            bottom_results = []
            dfs(0, 6, bottom, 0, bottom_results)
            for top_r in top_results:
                for bottom_r in bottom_results:
                    ret.append(str(top_r) + ':' + (str(bottom_r) if bottom_r >= 10 else ('0' + str(bottom_r))))
        return list(set(ret))

def main():
    '''main function'''
    _solution = Solution()
    inp = []
    for i in inp:
        print(_solution.func(i[0], i[1]))

if __name__ == "__main__":
    main()
