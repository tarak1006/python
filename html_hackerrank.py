f1=open("html_comp.txt",'r')
s=f1.readlines();
s.sort()
f2=open("html_comp_op.txt",'w')
#for i in range(len(s)):
   # f2.write(s[i])
#print(s)
for i in range(len(s)):
    print(i)
for i in range(len(s)):
    print(s[i])
#print(len(s))
print(s)

