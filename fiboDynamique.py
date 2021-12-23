import timeit


print("Fibonacci sequence:")
start = timeit.default_timer()
for n in range( 30 , 50):
    start = timeit.default_timer()
    fibo_cache = {}
    def calcul_fibonacci(n):
       if n in fibo_cache:
          return fibo_cache[n]
       else:
          if n in {0 ,1}:
              if n == 0:
                  valeur = 0
              else:
                  valeur = 1
          else :
              valeur = calcul_fibonacci(n-2) + calcul_fibonacci(n-1)
              fibo_cache[n] = valeur
          return valeur

    print("Fib(", n,")=", calcul_fibonacci(n), end=' ')
    end = timeit.default_timer()
    print("Temps d'execution:",(end - start)*1000,  end='\n')