void staircase(int n) {
    // iterate through each row
    for(int i=1;i<=n;i++) {
        // print spaces before the hashtags
        for(int j=0;j<n-i;j++) {
            printf(" ");
        }
        // print hashtags
        for(int j=1;j<=i;j++) {
            printf("#");
        }
        // move to the next line
        printf("\n");
    }
}
