func largestNumber(n int) int {
	var result int = 1;
	for n > 0 {
	   result = result * 10;
	   n--;
	}
	return result - 1;
 }
 