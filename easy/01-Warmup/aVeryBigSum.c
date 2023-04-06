long aVeryBigSum(int ar_count, long* ar) {
    long sum = 0; // initialize the sum to 0
    for(int i = 0; i < ar_count; i++) {
        sum += ar[i]; // add each element of the array to the sum
    }
    return sum; // return the sum
}
