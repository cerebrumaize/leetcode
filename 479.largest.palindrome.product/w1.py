def notPalindrome(x):
    s = str(x)
    l = len(s)
    #print(s[:l//2])
    #print(s[:l//2-1:-1])
    return s[:l//2]!=s[:l//2-1:-1]
def helper(n, k, part, total):
    if k==0:
        total.append(part)
        return
    for i in range(9, -1 if k<n else 0, -1):
        helper(n, k-1, part+str(i), total)

def largestPalindrome(n):
    if n==1: return 9
    if n==2: return 987
    res = []
    helper(n, n, '', res)
    lo, high=int('1'+'0'*(n-1)), int('9'*n)
    for i in res:
        t = int(i+i[::-1])
        for tmp_div in range(high, lo-1, -1):
            d, m = divmod(t, tmp_div)
            if len(str(d)) > len(str(tmp_div)): break
            if m == 0 and len(str(d)) == len(str(tmp_div)): return t%1337
print(largestPalindrome(6))