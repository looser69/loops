import sys

n = int(input('enter upto which you want to see finbonacci series: '))
if n<1:
    print('please enter a valid number')
    sys.exit(-1)
print(0)
if n==1:
    sys.exit(0)
print(1)
if n<=2:
    sys.exit(0)
f = 0
s = 1
for i in range(3 , n+1):
    t = s + f
    print(t)
    f = s
    s = t
