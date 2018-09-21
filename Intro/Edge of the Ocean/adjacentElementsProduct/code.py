def adjacentElementsProduct(a):
  b=[]
  for i in range(len(a)-1):
    b.append(a[i]*a[i+1])
  return max(b)

def adjacentElementsProduct(inputArray):
  result = -float('inf')
  for i in range(len(inputArray) - 1):
      if inputArray[i] * inputArray[i+1] > result:
          result = inputArray[i] * inputArray[i+1]
  return result