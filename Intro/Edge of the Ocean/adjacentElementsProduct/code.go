func adjacentElementsProduct(inputArray []int) int {
    var l int = len(inputArray) - 1;
    var result int = -100000;
    for i:= 0; i < l ;i++ {
        if (inputArray[i] * inputArray[i+1]) > result {
            result = inputArray[i] * inputArray[i+1];
        }
    }
    return result;
}