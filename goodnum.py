n1=int(input("enter a number:"))
n2=int(input("enter a number:"))

t = input()
while t:
    inpt = raw_input()
    data = inpt.split()
    ma = []
    for i in range(n1, n2 + 1, 1):
        ma.append(i)
    p = []
    for i in range(2, n2):
        c = 0
        for j in range(1, i + 1):
            if i % j == 0:
                c += 1
        else:
            if c == 2:
                p.append(i)
    s = []
    i = 2
    while i * i < n2:
        s.append(i * i)
        i += 1
    for j in s:
        c = []
        for i in ma:
            if i % j != 0:
                c.append(i)
        ma = c
    s = []
    for i in ma:
        q = 0
        for j in range(1, i + 1, 1):
            if i % j == 0:
                q += j
        s.append(q)
    d = []
    for i in s:
        k = 0
        for j in p:
            if i % j == 0:
                k += 1
        d.append(k)
    e = []
    for i in range(d.__len__()):
        if d[i] in p:
            e.append(i)

    l = int(data[0])
    r = int(data[1])
    x = 0
    for i in e:
        x += s[i]
    t -=1


def matmult(m1, m2):
    v = []
    for i in range(len(m1)):
        b=[]
        for j in range(len(m2[0])):
            p=0
            for t in range(len(m2)):
                 p=p + m1[i][t]*m2[t][j]
            b.append(p)
        v.append(b)
    return v

