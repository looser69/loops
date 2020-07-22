n = input('enter the position you want')
f = 0
s = 1
r = -1;
if n==1:
    r == f
if n==2:
    r == s
for i in range(3,n+1):
    r = s+f
    f = s
    s = r
print(r)
