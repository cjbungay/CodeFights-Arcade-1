def centuryFromYear(year):
   a=int((year)/100)+1 
   if year % 100 == 0: 
      return a-1
   else: 
      return a
      