// Problem 7: What is the 10001st prime number?
// Author: Subhadeep Pal Date: 10/10/2026

# include <stdio.h>
# include <stdbool.h>

bool isPrime(int num)
{
    bool flag = true;
    for (int i = 2; i < num; i++)
    {
        if (num % i == 0)
        {
            flag = false;
        }
    }
    return flag;
}

int main()
{
    int arr[12000];
    int index = 0;

    arr[index] = 2;
    index++;

    for(int i = 3; i < 1000000; i++)
    {
        if (isPrime(i))
        {
            arr[index] = i;
            index++;
            // printf("%d prime found: %d\n", index, i);
            if (index > 10001) { break; }
        }
    }

    printf("%d prime is: %d\n", 10000, arr[9999]);
    printf("%d prime is: %d\n", 10001, arr[10000]);
    printf("%d prime is: %d\n", 10002, arr[10001]);

    return 0;
}