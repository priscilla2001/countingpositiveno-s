a=[]
for i in range(0,5,1):
    print("enter a[%d]"%i)
    new=int(input())
    a.append(new)
print(a)
print("The number of positive values")
for list in a:
  if list>=1:
    print(list)
