def circleOfNumbers(n, firstNumber):
   res = firstNumber+((n)//2)
   if res > n-1:
      return res-n
   else:
      return res
   
   