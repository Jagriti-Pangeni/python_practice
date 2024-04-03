# from itertools import product

# a=(1,2)
# b=(3,4)

# print(list(product(a,b)))

# from itertools import combinations

# a=[1,2,3]
# print(list(combinations(a,3)))   same for permutations

# from itertools import accumulate
# import operator

# a=[1,2,5,3,4]
# print(a)
# print(list(accumulate(a)))
# print(list(accumulate(a,operator.mul)))
# print(list(accumulate(a,func=max)))

# from itertools import groupby
# def smaller_than(x):
#     return x<4

# a=[1,2,5,9,6,4,8]
# group_obj=groupby(a,key=smaller_than)
# for key,value in group_obj:
#     print(key, list(value))


# a=[{'name':'Jagriti','age':20},{'name':'Ram','age':'21'},{'name':'Alex','age':'21'},{'name':'Pooja','age':'20'},{'name':'Sonika','age':'20'},{'name':'Arati','age':'20'}]

# group_obj=groupby(a, key=lambda x: x['age'])

# for key,value in group_obj:
#     print(key,list(value))

from itertools import count,repeat,cycle

a=[2,3,4,5,6]

# for i in repeat(2,5):
#     print(i)

# for i in count(10):
#     print(i)
#     if i>=15:
#         break