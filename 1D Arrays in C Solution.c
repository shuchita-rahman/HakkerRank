#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
  
  int n, a[1005], sum = 0;
  
  scanf("%d", &n);

  for(int i = 0; i < n; i++)
  {
      scanf("%d", &a[i]);
      sum = sum + a[i];
  }
  printf("%d\n", sum);
    return 0;
}

