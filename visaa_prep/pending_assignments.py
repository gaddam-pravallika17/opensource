x,y,z=list(map(int, input().split()))
total_min = z*24*60
if x*y <= total_min:
    print("YES")
else:
    print("NO")
