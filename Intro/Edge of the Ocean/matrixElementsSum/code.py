def matrixElementsSum(matrix):
    sumM = 0
    for i in range(0,len(matrix[0])):
      for j in range(0,len(matrix)):
        if matrix[j][i] == 0:
          break
        else:
          sumM+=matrix[j][i] 
    else:
      return sumM
