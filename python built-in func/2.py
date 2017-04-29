l = [4, 6, 5, 7]
def func1(l1, l2):
  '''
  l1 is the leading indices of l,
  l2 is the tailing indices of l
  '''
  print l1, l2
  if len(l2) == 0:
    return None
  for i in xrange(len(l2)):
    temp = l1[:]
    tmp = l2[:]
    if l[temp[-1]] < l[tmp[i]]:
      temp.append(tmp[i])
      res.append([l[x] for x in temp])
      tmp = tmp[i+1:len(tmp)]
      func1(temp, tmp)

res = [] 
for x in xrange(len(l)):
  print x
  func1( [x], range(0, x) + range((x + 1), len(l)) )
print res