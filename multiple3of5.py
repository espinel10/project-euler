N=1000
acum=0

for i in range(0,N):
  if i%5==0 or i%3==0:
    acum=acum+i
  
print(acum)
