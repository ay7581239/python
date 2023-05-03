n=int(input("Enter the no.:"))
if(n%2==0):
    n=n+1
j=n//2+1
print('* '*j,end="")
k=n//2-1
print('  '*k,end="")
print('*')
for i in range(k):
    print('  '*(j-1),end="")
    print('*',end="")
    print('  '*k,end="")
    print(' *')
print('* '*j,end='')
print('* '*k,end="")
print('*')
for i in range(k):
    print('*',end='')
    print('  '*k,end="")
    print(' *')
print('*',end='')
print('  '*k,end="")
print(' *'*j,end="")