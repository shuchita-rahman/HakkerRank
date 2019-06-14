#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char *s;
    int stringSize, frequcey[10]= {0};

    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    stringSize = strlen(s);
    s = realloc(s, stringSize + 1);

    for(int i = 0; i < stringSize; i++)
    {
        int index = s[i] - '0';
        if(index >= 0 || index <= 9)
        {
              frequcey[index]++;
        }
    }
    for(int i = 0; i <= 9; i++)
    {
        printf("%d ", frequcey[i]);
    }
    return 0;
}
