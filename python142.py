#Python function to display all the Armstrong number from 1 to n.

def armstrong_num(num):
  for n in range(1,num):
    sum = 0
    temp = n
    while temp > 0:
      digit = temp % 10
      sum += digit ** 3
      temp //= 10
    if n == sum:
      print(n)

armstrong_num(1000)

