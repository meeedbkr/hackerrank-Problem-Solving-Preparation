class Result {

    /*
     * Complete the 'diagonalDifference' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY arr as parameter.
     */

    public static int diagonalDifference(List<List<Integer>> arr) {
        // Initialize variables to store diagonal sums and difference
        int d1 = 0, d2 = 0, diff = 0;

        // Loop through each element in the 2D array
        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < arr.get(i).size(); j++) {
                // If element is on diagonal from top-left to bottom-right
                if (i == j) {
                    d1 += arr.get(i).get(j);
                }
                // If element is on diagonal from top-right to bottom-left
                if (arr.size() - i - 1 == j) {
                    d2 += arr.get(i).get(j);
                }
            }
        }

        // Calculate absolute difference between diagonal sums
        diff = Math.abs(d1 - d2);
        return diff;
    }

}
