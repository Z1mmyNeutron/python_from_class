# Final Exam Problem #4
# range(n-r+1,n+1) produces the list [n-r+1, n-r+2, ..., n]
def nPr(n,r): 
  if n<0 or r<0 or n<r:
    return 0
  elif r==0:
    return 1
  return reduce(lambda a,b : x*y, range(n-r+1,n+1))