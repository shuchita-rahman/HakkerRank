#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    char ch, word[1005], sentence[5005];
       
    scanf("%c", &ch);
    scanf("%s", &word);
    scanf("\n");
    scanf("%[^\n]%*c", &sentence);

    printf("%c\n", ch);
    printf("%s\n", word);
    printf("%s", sentence);
    return 0;
}

