#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, m, n, k):
        '''Solution function description'''
        res = []
        self.helper(res, [], 0, 0, 0, 0, 0, 0, m, n, k)
        return res
    def helper(self, total, part, counter1, counter2, counter3, round, square, flower, m, n, k):
        if counter1 < 0 or counter2 < 0 or counter3 < 0: return
        if counter1 > m or counter2 > n or counter3 > k: return
        if round > m or square > n or flower > k: return
        if part and len(part) > (m + n + k) * 2: return
        if part and len(part) == (m + n + k) * 2 and counter1 == 0 and counter2 == 0 and counter3 == 0 and\
           round == m and square == n and flower == k:
            total.append(part)
            return
        self.helper(total, part+['('], counter1+1, counter2, counter3, round, square, flower, m, n, k)
        self.helper(total, part+[')'], counter1-1, counter2, counter3, round+1, square, flower, m, n, k)
        self.helper(total, part+['['], counter1, counter2+1, counter3, round, square, flower, m, n, k)
        self.helper(total, part+[']'], counter1, counter2-1, counter3, round, square+1, flower, m, n, k)
        self.helper(total, part+['{'], counter1, counter2, counter3+1, round, square, flower, m, n, k)
        self.helper(total, part+['}'], counter1, counter2, counter3-1, round, square, flower+1, m, n, k)

def main():
    '''main function'''
    _solution = Solution()
    inp = [(1, 1, 1)]
    for i in inp:
        for r in _solution.func(i[0], i[1], i[2]):
            print(r)

if __name__ == "__main__":
    main()
