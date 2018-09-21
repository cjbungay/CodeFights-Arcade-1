function adjacentElementsProduct(inputArray) {
    let result = -Infinity;
    let len = inputArray.length - 1;
    for (i = 0; i< len; i++) {
        if ((inputArray[i] * inputArray[i+1]) > result) {
            result = inputArray[i] * inputArray[i+1];
        }
    }
    return result;
}