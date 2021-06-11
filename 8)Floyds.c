#include<stdio.h>
int min(int,int);
void floyds(int p[10][10],int n) {
	int i,j,k;
	for (k=1;k<=n;k++)
	  for (i=1;i<=n;i++)
	   for (j=1;j<=n;j++)
	    if(i==j)
	     p[i][j]=0; 
		else
	     p[i][j]=min(p[i][j],p[i][k]+p[k][j]);
}
int min(int a,int b) {
	if(a<b)
	  return(a); 
	else
	  return(b);
}
int main() {
	int p[10][10],w,n,u,v,i,j;
	printf("\n Enter the number of vertices:");
	scanf("%d",&n);
	printf("enter adjacency matrix");
	for (i=1;i<=n;i++) {
		for (j=1;j<=n;j++)
		   scanf("%d",&p[i][j]);
	}
	printf("\n Matrix of input data:\n");
	for (i=1;i<=n;i++) {
		for (j=1;j<=n;j++)
		   printf("%d \t",p[i][j]);
		printf("\n");
	}
	floyds(p,n);
	printf("\n Transitive closure:\n");
	for (i=1;i<=n;i++) {
		for (j=1;j<=n;j++)
		   printf("%d \t",p[i][j]);
		printf("\n");
	}
	printf("\n The shortest paths are:\n");
	for (i=1;i<=n;i++)
	  for (j=1;j<=n;j++) {
		if(i!=j)
		    printf("\n <%d,%d>=%d",i,j,p[i][j]);
	}
}
