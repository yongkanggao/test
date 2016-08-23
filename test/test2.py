__author__ = 'yongkang'
#coding=utf-8

'''输出树形结构'''

from collections import defaultdict
import json

def tree():
    return defaultdict(tree)

users = tree()
users['codingpy']['username'] = 'earlgrey'
users['python']['username'] = 'Guido van Rossum'
print(json.dumps(users,indent=1))