#include <stdio.h>
#include <math.h>

int isArmstrong(int number) {
    int originalNumber, remainder, n = 0, result = 0;
    
    originalNumber = number;

    // Count the number of digits in the number
    while (originalNumber != 0) {
        originalNumber /= 10;
        ++n;
    }

    originalNumber = number;

    // Calculate the Armstrong number
    while (originalNumber != 0) {
        remainder = originalNumber % 10;
        result += pow(remainder, n);
        originalNumber /= 10;
    }

    if (result == number) {
        return 1;  // It's an Armstrong number
    } else {
        return 0;  // It's not an Armstrong number
    }
}

int main() {
    int number;
    
    printf("Enter a number: ");
    scanf("%d", &number);
    
    if (isArmstrong(number)) {
        printf("%d is an Armstrong number.\n", number);
    } else {
        printf("%d is not an Armstrong number.\n", number);
    }

    return 0;
}
