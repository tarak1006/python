import operator as op
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer =  reduce(op.mul,xrange(n,n-r,-1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

res=0
N,k=map(int,raw_input().split())
for i in xrange(0,k+1,2):
    res= res +ncr(N,i)
    res = res % 1000000007

print(res)