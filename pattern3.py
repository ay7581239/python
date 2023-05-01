n=int(input("Enter the no.:"))
for i in range(n):
    print(' '*(n-i),end=" ")
    print('*'*(2*i-1))
for i in range(n):
    print(' '*(i),end=" ")
    print('*'*(2*n-2*i-1))  