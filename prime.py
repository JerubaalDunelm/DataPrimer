# starting number
number = 2

# while loop looking for primes
while number<= 100:
    # figure out if the number is a prime
    # set as True, then disprove it
    is_prime = True
    trial = 2 # don't test for divisble by 1
    while trial < number:
        #test if divisible by any of the numbers below itself & above one
        if number % trial == 0:
            is_prime = False
        #increment trial
        trial += 1
    # if it's not prime, then next bit won't print
    if is_prime:
        print number
    #increment number
    number += 1
