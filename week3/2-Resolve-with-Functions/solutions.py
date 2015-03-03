#divisors problem
from divisors import divisors
n=int(input("Please insert a number to find it's divisors: "))
print("The divisors of n({}) are {}".format(n,divisors(n)))


#sum_divisors problem
from sum_divisors import sum_divisors
n=int(input("Please insert a number to sum it's devisors: "))
print("The sum of divisors of n({}) is {}".format(n,sum_divisors(n)))


#is_perfect problem
from is_perfect import is_perfect
n=int(input("Please insert a number to check is it perfect: "))
print(is_perfect(n))

#first_N_perfect problem
from first_n_perfect import first_n_perfect
n=int(input("Please insert the count of perfect numbers to display: "))
print(first_n_perfect(n))

#prime_digit problem 
from prime_digit import prime_digit
n=int(input("Please insert a number to be checked for prime digits: "))
print(prime_digit(n))

#twin_prime problem
from twin_prime import twinp
n=int(input("Insert a number to ckeck for twin primes: "))
twinp(n)
