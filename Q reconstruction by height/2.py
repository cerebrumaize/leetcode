#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def func(self, people):
        '''Solution function description'''
        people.sort(key=lambda x: (-x[0], x[1]))
        #print(people)
        res = []
        for x in people:
            res.insert(x[1], x)
            #print(res)

def main():
    '''main function'''
    _solution = Solution()
    inp = [[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]] ]
    for i in inp:
        print(_solution.func(i))

if __name__ == "__main__":
    main()
