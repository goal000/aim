def dls(vis,a,src,n,count,dl):
    if(count<dl):
        for i in range(0,n):
            if(a[src][i]==1 and vis[i]==0):
                print(i,end=" ")
                vis[i]=1
                dls(vis,a,i,n,count+1,dl)
print("Enter no of vertices : ")
n=int(input())
a=a=[[0 for i in range(n)] for j in range(n)]
print("Enter no of edgs : ")
edgs=int(input())
vis=[0]*n
print("Enter edges (src to dst) : ")
for i in range(0,edgs):
    l1,l2=[int(x) for x in input().split()]
    a[l1][l2]=1
print("enter depth limit : ")
dlimit=int(input())
print(0,end=" ")
dls(vis,a,0,n,0,dlimit)