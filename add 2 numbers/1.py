class Solution(object):
    def ListNode_list(self, l):
        res = []
        while(l != None):
            res.append(l.val)
            l = l.next
        return res
        
    def addTwoNumbers(self, l1, l2):
        list1, list2 = self.ListNode_list(l1), self.ListNode_list(l2)
        if list1[-1] == 0:
            return l2
        if list2[-1] == 0:
            return l1
        #print list1, list2
        slist, llist = [], []
        if len(list1) > len(list2):
            llist = list1
            slist = list2
        else:
            llist = list2
            slist = list1

        carry, mod = 0, 0
        res = []
        for i in xrange(0, len(slist), 1):
            #print llist[i], slist[i]
            carry, mod = divmod(carry + llist[i] + slist[i], 10)
            res.append(mod)
        for i in xrange(len(slist), len(llist), 1):
            carry, mod = divmod(carry + llist[i], 10)
            res.append(mod)
        if carry > 0:
            res.append(carry)

        l3 = ListNode(res[0])
        cur = l3
        if len(res) == 1:
            return l3
        for i in xrange(1, len(res)):
            cur.next = ListNode(res[i])
            cur = cur.next
        return l3