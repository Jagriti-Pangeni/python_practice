# from collections import namedtuple

# point=namedtuple('point',"x,y,z")

# pt=point(1,3,5)
# print(pt)

from collections import deque

d=deque()
d.append(1)
d.append(9)
d.append(10)
d.append(34)

print(d)

d.pop()
print(d)

d.popleft()
print(d)


