__author__ = 'yongkang'

from collections import Counter

some_list1 = [1,2,3,4]
another_list1 = [x+1 for x in some_list1]
print(another_list1)


some_list2 = [1,2,3,4,5,6,7,8,9,10]
another_list2 = [x for x in some_list2 if x%2 == 0]
print(another_list2)

some_list3 = {x:x%2 == 0 for x in range(1,11)}
print(some_list3)

c = Counter('hello world!')
print(c)
