#include <stdio.h>

void update(int *a,int *b) {
     
     int i = *a + *b;
     int j = *a - *b;
      
      if(j < 0)
            j = j * -1;
      *a = i;
      *b = j;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

