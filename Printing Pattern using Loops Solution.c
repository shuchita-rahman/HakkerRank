#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{

    int n, numOfIteration, temp, flag1 = 0;

    scanf("%d", &n);
    numOfIteration = (2 * n) - 1;
    temp = n;

    for(int i = numOfIteration; i >= 1; i--)
    {
       int difference = n - temp, temp4 = temp;
       int temp1 = n, flag = 1, index = 1;

       for(int j = 1; j <= numOfIteration; j++)
       {
           if(i == 1 || i == numOfIteration || j == numOfIteration)
           {
                printf("%d ", n);
           }
           else if(difference > 0)
           {
              printf("%d ", temp1);
              temp1--;
              difference--;
              flag = 1;
           }
           else if(flag == 1 && index <= (2*temp)-1 )
           {
               printf("%d ", temp);
               index++;
           }
           else
           {
               temp4++;
               printf("%d ", temp4);

           }
       }
       printf("\n");
       if(temp ==1)
       {
           flag1 = 1;
       }
       if(flag1 == 0)
       {
           temp--;
       }
       else
       {
           temp++;
       }
    }

    return 0;
}

