x,y,z=list(map(int, input().split()))
if x+y<=z:
    print("2")
elif x>z:
    print("0")
else:
    print("1")
