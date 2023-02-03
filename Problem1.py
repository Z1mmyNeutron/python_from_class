# Final Exam Problem 1
def aux(n):
  return int((((1 + 5**0.5) / 2)**n - ((1 - 5**0.5) / 2)**n) / 5**0.5)

def mystery(n):
  return map(aux, range(n))