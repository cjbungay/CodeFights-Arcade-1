def lateRide(n):
    num = 0
    hours,minutes = int(n/60), n%60
    while hours>0:
      num += hours%10
      hours = int(hours/10)
    while minutes>0:
      num += minutes%10
      minutes = int(minutes/10)
    return num