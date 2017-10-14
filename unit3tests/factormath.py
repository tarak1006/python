def factorize_number(n):
    r=[]
    i=2
    while n!=1:
        c=0
        while n%i==0 & n!=1:
            c=c+1
            n=n/i
        if c!=0:
            r.append((i,c))
        i=i+1
    return r

def get_hcf(i1,i2):
        r=[]
        for m,n in i1:
            for p,q in i2:
                if m==p:
                    if n>q:
                        r.append((m,q))
                    else:
                        r.append((m,n))
        return sorted(r)



def get_lcm(i1,i2):
    r=[]
    if i2 > i1:
        i1,i2 = i2,i1
    for m2,n2 in i1:
        for m1,n1 in i2:
            if m2==m1:
                if n1<n2:
                    r.append((m2,n2))
                else:
                    r.append((m2,n1))
    for m,n in i1:
        k=False
        for p,q in r:
            if m==p:
                k=True
        if not k:
            r.append((m,n))
    for m,n in i2:
        k=False
        for p,q in r:
            if m==p:
                k=True
        if not k:
             r.append((m,n))

    return sorted(r)


def multiply(i1,i2):
    r=[]
    if i2>i1:
        i1,i2=i2,i1
    for m,n in i1:
        for p,q in i2:
            if m==p:
                r.append((m,n+q))
    for m, n in i1:
        k = False
        for p, q in r:
            if m == p:
                k = True
        if not k:
            r.append((m, n))
    for m,n in i2:
        k=False
        for p,q in r:
            if m==p:
                k=True
        if not k:
            r.append((m,n))
    return sorted(r)


