def adjacentElementsProduct(a):
  b=[]
  for i in range(len(a)-1):
    b.append(a[i]*a[i+1])
  return max(b) 