"""
Example: Factorial of a Number
factorial of n (n!) = 1*2*3*4....n
The factorial of a negative number doesn't exist. And the factorial of 0 is 1.
"""

"""
#include <stdio.h>
int main()
{
    int n, i;
    unsigned long long factorial = 1;

    printf("Enter an integer: ");
    scanf("%d",&n);

    // show error if the user enters a negative integer
    if (n < 0)
        printf("Error! Factorial of a negative number doesn't exist.");

    else
    {
        for(i=1; i<=n; ++i)
        {
            factorial *= i;              // factorial = factorial*i;
        }
        printf("Factorial of %d = %llu", n, factorial);
    }

    return 0;
}
"""


"""
Suppose the user entered 6.

Initially, the multiplyNumbers() is called from the main() function with 6 passed as an argument.

Then, 5 is passed to the multiplyNumbers() function from the same function (recursive call). In each recursive call, the value of argument n is decreased by 1.

When the value of n is less than 1, there is no recursive call.

"""
