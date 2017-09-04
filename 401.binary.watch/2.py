
#!/usr/bin/env python
'''code description'''
# pylint: disable = I0011, E0401, C0103
import copy

def perm(data, pos, res):
    if pos == len(data)-1:
        res.append(''.join( str(di) for di in data ))
    else:
        for j in xrange(pos, len(data)):
            data[pos], data[j] = data[j], data[pos]
            perm(data, pos+1, res)
            data[pos], data[j] = data[j], data[pos]
    return list(set(res))

def get_list(count, t):
    res = [0]*t
    for i in xrange(count):
        res[i]=1
    return perm(res, 0, [])

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        times=[]
        hour_ceiling = 4 if 4 <= num else num
        for hour_count in xrange(hour_ceiling + 1):
            list_hour = get_list( hour_count, 4)
            if num - hour_count > 6:
                continue
            list_min = get_list( num - hour_count, 6)
            for hour in list_hour:
                for min in list_min:
                    if ( int(hour, 2) >= 12 ) | ( int(min, 2) >= 60 ) :
                        continue
                    times.append("{0}:{1:02d}".format(int(hour, 2), int(min, 2)))

        return times
        
def main():
    '''main function'''
    sol = Solution()
    a = random.random(0, 10)
    res = sol.readBinaryWatch(a)
    print res

if __name__ == "__main__":
    main()
