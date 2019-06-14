#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

//Complete the following function.

int marks_summation(int* marks, int number_of_students, char gender) {
    
    int sum = 0, j;
    if(gender == 'b')
    {     
        j = 0;
    }
    else if(gender == 'g')
    {
        j = 1;
    }

    for(int i = j; i < number_of_students; i = i + 2)
    {
        sum = sum + marks[i];
    }
    return sum;
}


int main() {
