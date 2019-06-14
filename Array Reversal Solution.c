#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) {
        scanf("%d", arr + i);
    }

    for(int i = 0, j = num - 1; i < num / 2; i++, j--)
    {
        int a = *(arr + j);
        *(arr + j) = *(arr + i);
        *(arr + i) = a;
    }
    
    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}

