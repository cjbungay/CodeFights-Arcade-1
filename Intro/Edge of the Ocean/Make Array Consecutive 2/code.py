def makeArrayConsecutive2(statues):
    stat = sorted(statues)
    length = len(statues)
    required_statues=0
    for i in range(length-1):
        required_statues+=stat[i+1]-stat[i]-1
    return required_statues
    