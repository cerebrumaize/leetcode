
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401

class Solution(object):
    '''Solution description'''
    def func(self, l1, l2):
        '''
        Solution function description
        '''
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10

        return dummy.next

def main():
    '''main function'''
    _solution = Solution()
    res = _solution.func(a, b)
    print res

if __name__ == "__main__":
    main()
