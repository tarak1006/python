n=50000
a=range(3,n,2)
l=len(a)
for i in range(0,l):
    if a[i]!=0:
        for j in range(i + 1, l):
            if a[j] % a[i ] == 0:
                a[j] = 0
b=[]
for i in range(len(a)):
    if a[i]!=0:
        b.append(a[i])
print(b)
c=range(50001,100000)
l1=len(c)
for i in range(0,len(b)):
    if b[i]!=0:
        for j in range(0,:


nn