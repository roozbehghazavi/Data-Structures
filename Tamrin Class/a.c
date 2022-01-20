#include <stdio.h>

int main()
{
	 int x , n;
	int xn=1 , f=1 , i = 2;
    
    double answer=1;

    printf("enter the two integers");

    scanf("%d %d",&n,&x);
	

      for(i=2 ; i<=n ; i+=2)
      {

        xn*=x*x;
        f*= (i-1) * i;
        if (i % 4 ==0)
        {
           answer += (double)xn / f ;/* code */
        }
        else
        {
           answer -= (double)xn / f ;
        }

      }

      printf("cos(%d) = %.2f", x , answer);
      

        return 0;
}