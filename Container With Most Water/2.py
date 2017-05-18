
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def func(self, height):
        '''
        Solution function description
        '''
        l, r, max_area = 0, len(height)-1, 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

def main():
    '''main function'''
    _solution = Solution()
    a = [1, 3, 2, 9]
    res = _solution.func(a)
    print res

if __name__ == "__main__":
    main()
