def fibonacci_dinamico(n,memo={}):
    if n==1:
        return memo[n]
    elif n==2:
        return memo[n]

    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n-1,memo) + fibonacci_dinamico(n-2,memo)
        memo[n]=resultado
        return resultado

def run(t1,t2,n):
    dic={}
    dic[1]=1
    dic[2]=2
    return fibonacci_dinamico(n,dic)


num=0
acum=0
i=1
while num<4000000:
    num=run(1,2,i)
    if num%2==0:
        acum=acum+num
    i=i+1


print("respuesta=",acum)
