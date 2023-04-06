#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// Function to add two integers
int solveMeFirst(int a, int b) {
    return a+b;
}

// Main function
int main() {
    // Read two integers from standard input
    int num1, num2;
    scanf("%d %d", &num1, &num2);
    
    // Compute the sum of the two numbers using the solveMeFirst function
    int sum = solveMeFirst(num1, num2);
    
    // Print the sum to standard output
    printf("%d", sum);
    
    // Return 0 to indicate successful completion of program
    return 0;
}
