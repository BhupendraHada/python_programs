"""
Example: Check Prime and Armstrong Number
"""

# A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.
# For example: 153 is an Armstrong number since 153 = 1*1*1 + 5*5*5 + 3*3*3.

num = int(input("Enter a number: "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

"""
#include <stdio.h>
#include <math.h>

int checkPrimeNumber(int n);
int checkArmstrongNumber(int n);

int main()
{
    int n, flag;

    printf("Enter a positive integer: ");
    scanf("%d", &n);

    // Check prime number
    flag = checkPrimeNumber(n);
    if (flag == 1)
        printf("%d is a prime number.\n", n);
    else
        printf("%d is not a prime number.\n", n);

    // Check Armstrong number
    flag = checkArmstrongNumber(n);
    if (flag == 1)
        printf("%d is an Armstrong number.", n);
    else
        printf("%d is not an Armstrong number.",n);
    return 0;
}

int checkPrimeNumber(int n)
{
    int i, flag = 1;

    for(i=2; i<=n/2; ++i)
    {

    // condition for non-prime number
        if(n%i == 0)
        {
            flag = 0;
            break;
        }
    }
    return flag;
}

int checkArmstrongNumber(int number)
{
    int originalNumber, remainder, result = 0, n = 3, flag;

    originalNumber = number;

    while (originalNumber != 0)
    {
        originalNumber /= 10;
        ++n;
    }

    originalNumber = number;

    while (originalNumber != 0)
    {
        remainder = originalNumber%10;
        // result += pow(remainder, n);
        result += remainder*remainder*remainder;
        originalNumber /= 10;
    }

    // condition for Armstrong number
    if(result == number)
        flag = 1;
    else
        flag = 0;

    return flag;
}
"""
