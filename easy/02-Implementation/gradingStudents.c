// Define a function named "gradingStudents" that takes three arguments:
// grades_count (an integer indicating the number of elements in the "grades" array),
// grades (a pointer to an integer array containing the grades to be rounded), and
// result_count (a pointer to an integer that will be set to "grades_count").
int* gradingStudents(int grades_count, int* grades, int* result_count) {
    
    // Set "result_count" to the value of "grades_count".
    *result_count = grades_count; 
    
    // Loop through each element in the "grades" array.
    for(int i=0;i<grades_count;i++){
        
        // Check if the current grade is greater than or equal to 38.
        if(grades[i]>=38){
            
            // Divide the current grade by 5 and round down to the nearest integer.
            int n = (int) (grades[i]/5);
            
            // Multiply the rounded value by 5 to get the next multiple of 5.
            n = (n+1)*5;
            
            // If the difference between the rounded grade and the current grade is less than 3,
            // round the current grade up to the next multiple of 5.
            if(n - grades[i] < 3) grades[i]=n;
        }
    }
    
    // Return a pointer to the "grades" array.
    return grades;
}
