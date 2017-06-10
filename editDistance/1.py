
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103

class Solution(object):
    '''Solution description'''
    def minDistance(self, word1, word2):
        '''
        Solution function description
        '''
        m, n = len(word1), len(word2)
        print word1, word2, m, n
        if m==0: return n
        if n==0: return m
        # think about it, the last character of each word, 
        # it stiil needs to ins/del/rep
        res = [[0]*(m+1) for i in xrange(n+1)]
        for i in xrange(n+1): res[i][0] = i
        for i in xrange(m+1): res[0][i] = i
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                if word1[j-1]==word2[i-1]:
                    res[i][j] = min(res[i-1][j]+1, res[i][j-1]+1, res[i-1][j-1])
                else:
                    res[i][j] = min(res[i-1][j]+1, res[i][j-1]+1, res[i-1][j-1]+1)
        print res
        return res[-1][-1]

def main():
    '''main function'''
    _solution = Solution()
    a, b='park', 'spake'
    res = _solution.minDistance(a, b)
    print res

if __name__ == "__main__":
    main()
