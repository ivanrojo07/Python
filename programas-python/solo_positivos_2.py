a = [1, 2, -1, -4, 5, -2] 

for i in range(0, len(a)):
  if a[i] < 0:
    del a[i]

print a
