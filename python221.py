#Write a program that generates a set of prime numbers and another set of odd numbers. Demonstrate the result of union, intersection, difference and symmetric difference operations on these sets.



odd=set([x*2+1 for x in range (0,5)])
primes=set()
for i in range(2,10):
  j=2
  f=0
  while j<i/2:
      if i%j==0:
          f=1
      j+=1
  if f==0:    
    primes.add(i)
print("Odd:",odd)
print("Prime:",primes)
print("Union:",odd.union(primes))
print("Intersection:",odd.intersection(primes))
print("Difference:",odd.difference(primes))
print("Symmetric Difference:",odd.symmetric_difference(primes))