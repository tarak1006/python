import collections
a = [1,1,1,1,2,2,2,2,3,3,4,5,5]
counter=collections.Counter(a)
print(counter)
# Counter({1: 4, 2: 4, 3: 2, 5: 2, 4: 1})
n=counter.values()
# [4, 4, 2, 1, 2]
print(counter.keys())
# [1, 2, 3, 4, 5]
print(counter.most_common(4))
# [(1, 4), (2, 4), (3, 2)]
l= dict(counter)
for i,j in l:
    if i==max(n):
        print i,j
