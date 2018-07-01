def largestNumber(n):
  if n == 0:
    return 0
  largest_number = ''
  for i in range(n):
    largest_number += '9'
  return int(largest_number)