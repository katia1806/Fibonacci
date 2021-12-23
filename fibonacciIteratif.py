import timeit


print("Fibonacci sequence:")

for n in range( 30 , 50):
    start = timeit.default_timer()
    def calcul_fibonacci( n ):

       if n in {0,1}:
           if n==0:
               return 0
           else:
               return 1
       else :
           return calcul_fibonacci(n-2) + calcul_fibonacci(n-1)


    print("Fib(", n,")=", calcul_fibonacci( n ) , end=' ')
    end = timeit.default_timer()
    print("Temps d'execution:",(end - start),  end='\n')
