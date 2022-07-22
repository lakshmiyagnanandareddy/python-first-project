import collections
"collections : Counter, namedtuple, OrderedDict, defaultdict, deque"
alphabet = "aaaaabbbssbcbcc"
print(collections.Counter(alphabet))
print(collections.Counter(alphabet).values())
print(list(collections.Counter(alphabet).elements()))
print(collections.Counter(alphabet).most_common(1)) # it will gives the most common element in the string with values.
print(collections.Counter(alphabet).most_common(1)[0][0])   # it will gives the most common element in the string.
"""
namedtuple - it helps you for assigning the values. 
"""
a = collections.namedtuple("point", "x,y")
pt = a(1, 3)
print(pt)
print(pt.x, pt.y)
"""
OrderedDic 
"""
dicctionary = {}
dicctionary['a'] = 4
dicctionary['c'] = 39
dicctionary['d'] = 30
dicctionary['b'] = 1

print(dicctionary)
"""
defaultdict - we can write as the default value, int, float,etc..
"""
d = collections.defaultdict(int)
d["a"]= 3
d["b"] = 6
print(d["n"])
"""
deque- append, rotate, pop, remove. etc..
"""