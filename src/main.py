def add(a,b,c=0):
  if type(a) != str or type(b) != str or type(c) != str:
    if 0 <= a <= 10 and 0 <= b <= 10 and 0 <= c <= 10 
      return int(a+b) + int(c)
    else:
      return -1
  else:
    return -1
