import operator
a="ifvjin roeicdoi kjbnfrelmpbvmjer"
b=list(set(list(a)))
print(b)
count=[ a.count(i) for i in b]
print(count)
e=zip(b,count)
print(e)
e.sort(key=operator.itemgetter(1))
print(e)
#print(dict(e))