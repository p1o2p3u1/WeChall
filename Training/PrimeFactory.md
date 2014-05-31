# Prime Factory

Your task is simple:  
Find the first two primes above 1 million, whose separate digit sums are also prime.
As example take 23, which is a prime whose digit sum, 5, is also prime.
The solution is the concatination of the two numbers,
Example: If the first number is 1,234,567
and the second is 8,765,432,
your solution is 12345678765432

## My Solution
```Python

def isPrime(n):
  for i in xrange(2,int(n ** .5) +1 ):
    if n % i == 0:
      return False
  return True
  
def sumDigit(n):
  sum = 0
  for i in str(n):
    sum += int(i)
  return sum
  
def getNextPrimeAfterN(n):
  n +=1
  while not isPrime(n):
    n+=1
  return n
  
def calc():
	n = 1000000
	prime = getNextPrimeAfterN(n)
	while not isPrime(sumDigit(prime)):
		prime = getNextPrimeAfterN(prime)
	prime1 = prime
	prime = getNextPrimeAfterN(prime)
	while not isPrime(sumDigit(prime)):
		prime = getNextPrimeAfterN(prime)
	prime2= prime
	print str(prime1) + str(prime2)

calc()

```

The answer is : 10000331000037

## Others Solution

```

```
