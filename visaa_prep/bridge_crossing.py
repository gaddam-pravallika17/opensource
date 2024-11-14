x,y,z=list(map(int,input().split()))
if y>z:
    mango=0
else:
    mango= (z-y)//x
print(mango)
