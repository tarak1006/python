
a=[2,11,16,12,36,60,71,17,29,144,288,129,432,993]

n =len(a)

def Best(i):
    if i==0:
        return 1
    else:
        m=1
        for j in range(i):
            if a[i]%a[j]==0:
                m=max(m,Best(j)+1)
    return m
res=[]
for j in range(n):
    res.append(Best(j))
print max(res)
