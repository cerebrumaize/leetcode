
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0111

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if (l1.val == 0) & (l1.next == None):
            return l2
        if (l2.val == 0) & (l2.next == None):
            return l1
        res, carry, mod = ListNode(0), 0, 0
        cur = res
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, mod = divmod(v1 + v2 + carry, 10)
            res.next = ListNode(mod)
            res = res.next
        #this is a clever way, use a 0 node as the start, and only return the tailing
        return cur.next 