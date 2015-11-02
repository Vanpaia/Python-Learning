"""

Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

number = int(raw_input("Number you want the largest prime factor of: "))

i = 2
prime_factors = []
answer = []

while i < number:
	j = 2
	while j <= (i/j):
		if not (i%j):
			break
		j = j + 1
	if j > (i/j):
		prime_factors.append(i)
	i = i+1


for i in prime_factors:
	if number % i == 0:
		answer.append(i)

print answer[len(answer)-1]