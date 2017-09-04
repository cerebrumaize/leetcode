#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103, C0321

class Solution(object):
    '''Solution description'''
    def readBinaryWatch(self, num):
        '''Solution function description'''
        if num==0:return ["0:00"]
        total = []
        rev = False
        if num > 5:
            rev = True
            part = ['1']*10
            num = 10-num
        else: part = ['0']*10
        def recur(total, part, num, rev):
            if num == 0:
                h = int(''.join(part[0:4]), base=2)
                m = int(''.join(part[4:10]), base=2)
                if h < 12 and m < 60:
                    if m<10: total.append(str(h)+':0'+str(m))
                    else: total.append(str(h)+':'+str(m))
                return
            for i in range(10):
                tmp = part[:]
                if not rev:
                    if tmp[i] == '1': continue
                    else: tmp[i] = '1'
                    if int(''.join(tmp[0:4]), base=2) > 11: continue
                    if int(''.join(tmp[4:10]), base=2) > 59: continue
                else:
                    if tmp[i] == '0': continue
                    else: tmp[i] = '0'
                recur(total, tmp, num-1, rev)

        recur(total, part, num, rev)
        return list(set(total))

def main():
    '''main function'''
    _solution = Solution()
    inp = [1,2,6]
    for i in inp:
        print(_solution.readBinaryWatch(i))

if __name__ == "__main__":
    main()
