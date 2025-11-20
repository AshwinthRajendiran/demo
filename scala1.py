  GNU nano 6.2                                                     studentData.sc
// 1. List of marks for five students
val marks = List(45, 88, 55, 92, 30)

// 2. Set of unique subjects
val subjects = Set("Math", "Physics", "Chemistry", "English", "History")

// 3. Map storing student names with their marks
val studentMarks = Map("Alice" -> 45, "Bob" -> 88, "Charlie" -> 55, "David" -> 92, "Eve" -> 30)

// Functional Programming Operations:

// Uses map to calculate the square of each mark
val squaredMarks = marks.map(m => m * m)

// Uses filter to find marks greater than 50
val highMarks = marks.filter(_ > 50)

// Uses foldLeft to find the sum of all marks
val totalSum = marks.foldLeft(0)(_ + _)

// Additional requirement: Print the highest and lowest mark
val highestMark = marks.max
val lowestMark = marks.min

// Output results
println(s"Original Marks: $marks")
println(s"Squared Marks: $squaredMarks")
println(s"Marks > 50: $highMarks")
println(s"Total Sum of Marks: $totalSum")
println(s"Unique Subjects: $subjects")
println(s"Student Marks Map: $studentMarks")
println(s"Highest Mark: $highestMark")
println(s"Lowest Mark: $lowestMark")