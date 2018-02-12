from Point import Points
q = Points(3,3)
mylist = []
mylist.append(q)
l = Points(4,5)

if(l not in mylist):
    print 'Not here'
else:
    print 'here'