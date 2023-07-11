arr1=[]
out=0
for i in range(4):
    inp=int(input())
    arr1.append(inp)
arr=arr1[:3]
arr1.sort()
for i in range(len(arr)):
    if arr[i]==arr1[3]:
        out=arr1[i+1]
ind=arr1.index(out)
if(ind==0):
    print("L1")
elif(ind==1):
    print("L2")
else:
    print("L3")
    