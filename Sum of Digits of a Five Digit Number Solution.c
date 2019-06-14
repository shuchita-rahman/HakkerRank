#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n, sum = 0;
    scanf("%d", &n);
    
    for(int i = 1; i < 5; i++)
    {
         sum = sum + (n % 10);
         n = n /10;
    }
    sum = sum + n;
    printf("%d\n", sum);
    return 0;
}

