def removeFirst(sequence, k):
    if 0 < k < len(sequence) - 1:
        if sequence[k-1] >= sequence[k+1]:
            return k-1
    for i in range(k+1, len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return i
    return -1

def almostIncreasingSequence(sequence):
    j = removeFirst(sequence, -1)
    if j == -1:
        return True  
    if removeFirst(sequence, j) == -1:
        return True 
    if removeFirst(sequence, j+1) == -1:
        return True 
    return False  