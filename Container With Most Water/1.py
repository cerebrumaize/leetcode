
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, height):
        '''
        Solution function description
        '''
        if len(height) == 2:
            return min(height)
        temp = sorted([(height[i], i) for i in xrange(len(height))], \
                      key=lambda p: p[0], reverse=True)
        res = []
        for i in xrange(1, len(height)):
            res.append(temp[i][0]*max(abs(temp[j][1]-temp[i][1]) for j in xrange(i)))
        return max(res)

def main():
    '''main function'''
    _solution = Solution()
    a = [1, 3, 2, 9]
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
