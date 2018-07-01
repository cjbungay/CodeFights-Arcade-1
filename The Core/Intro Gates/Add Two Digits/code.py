def addTwoDigits(n):
  sum1 = 0
  while n!=0:
    num = n%10
    sum1+=num
    n= n//10
  return sum1