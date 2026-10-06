// Problem 1: Multiples of 3 or 5
// Find the sum of all multiples of 3 or 5 below 1000
// Author: Subhadeep Date: 5/10/2026

# include <stdio.h>

int main()
{
    int sum;

    sum = 0;
    for(int i = 1; i < 1000; i++)
    {
        if(i % 3 == 0 || i % 5 == 0)
        {
            sum = sum + i;
        }
    }

    printf("Sum: %d \n", sum);
    return 0;
}
