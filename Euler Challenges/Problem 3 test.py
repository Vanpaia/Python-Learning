"""

Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

number = int(raw_input("Number you want the largest prime factor of: "))

prime_factors = []
answer = []

for i in range(2, number):
	prime = True
	for n in range(2, i):
		if (i % n) == 0:
			prime = False
			break
	if prime:
		prime_factors.append(i)


for i in prime_factors:
	if number % i == 0:
		answer.append(i)

print max(answer)