
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, matrix):
        '''List[List[str]]
        Solution function description
        '''
        if not matrix: return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in xrange(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in xrange(n+1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i-1-stack[-1]
                    ans = max(ans, h*w)
                stack.append(i)
                print stack, ans
        return ans

def main():
    '''main function'''
    _solution = Solution()
    a = ["10100","10111","11111","10010"]
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
