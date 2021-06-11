#Code For Sum Of Subsets:
def SumOfSubsets(s,k,r):
    global y,m,x
    if (s+y[k]) == m:
        ans=[]
        x[k]=1
        for i in range(len(x)):
            if x[i] !=0:
                ans.append(y[i])
        print(ans)
    elif (s+y[k]+y[k+1] <= m ):
        x[k]=1
        SumOfSubsets(s+y[k],k+1,r-y[k])
    if ((s+r-y[k]>=m) and (s+y[k+1]<=m)):
        x[k] = 0
        SumOfSubsets(s,k+1,r-y[k])
    x[k] = 0
y = []
n=int(input("Enter length :"))
for i in range(0,n):
    y.append(int(input("Enter elements :")))
print("The list is :",y)
x = [0]*(len(y))
m = int(input("Enter the sum :"))
s,k = 0,0
if (s+y[k]+y[k+1] <= m and (s+sum(y)-y[k]>=m) and (s+y[k+1]<=m)):
    print("\n THE SUBSET IS FOUND")
    SumOfSubsets(s,k,sum(y))
else:
     print("NO SUBSET IS FOUND WITH THE GIVEN SUM")
