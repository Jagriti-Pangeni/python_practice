# collection:- Counter,namedtuple,orderdict,defaltdict,deque
from collections import Counter
a="aaaaaaaaaabbbbbbccccccc"
my_counter=Counter(a)
# print(my_counter) 
# print(my_counter.items()) 
print(list(my_counter.elements())) 
# print(my_counter.keys()) 
# print(my_counter.pop('b')) 

