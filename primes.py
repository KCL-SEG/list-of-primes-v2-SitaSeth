"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes<=0:
        raise ValueError("Please enter an integer greater than or equal to 1.")
    list = []
    x=2 
    while(len(list)<number_of_primes):
        if(isPrime(x)):
            list.append(x)
    
        x+=1   
    return list

def isPrime(n):
    factor_count=0;
    x=1; 
    while(x<=n):
        if(n%x==0):
            factor_count+=1 
        x+=1
    if(factor_count>2):
        return False
    return True
