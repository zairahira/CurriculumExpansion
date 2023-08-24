import asyncio
import math 
import time

# Define an asynchronous function is_prime(num) that checks whether a given number is prime or not. The function follows the trial division algorithm.
async def is_prime(num):
    
    # Handle base cases: numbers less than or equal to 1 are not prime, and 2 or 3 are prime.
    if num <= 1:
        return False
    if num <= 3:
        return True
    
    # Check divisibility by 2 and 3 to rule out even and multiples of 3.
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    # Calculate the integer square root of num using math.isqrt() to determine the upper limit of divisors to check.

    sqrt_num = math.isqrt(num)  # Calculate the integer square root, rounded
    print("square root of {} is {}".format(num, sqrt_num))

    while i <= sqrt_num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        # Loop through potential divisors in increments of 6, as per the optimization of prime numbers being in the form 6k ± 1.

        i += 6

    return True


# Define an asynchronous function generate_primes(limit) that generates a specified number of prime numbers.
async def generate_primes(limit):
   
    # Initialize an empty list primes to store prime numbers.
    primes = []

    # Initialize num to 2, the first prime number.
    num = 2

    # Loop until the desired number of prime numbers (limit) is reached.
    while len(primes) < limit:
        
        # Call the is_prime function and await its result to check if num is prime.
        if await is_prime(num):
            
            # If prime, add num to the primes list.
            primes.append(num)

        # Increment num to check the next number.
        num += 1

    return primes


# Define the main() async function, which serves as the entry point for the asynchronous program.
async def main():
    
    # Set the desired number of prime numbers to generate (limit).
    limit = 1000  
    
    # Call the generate_primes function with the specified limit and await the result.
    primes = await generate_primes(limit)

    print(f"The first {limit} prime numbers are: {primes}")
    t1 = time.time()
    print("execution time for async: ", t1-t0)

if __name__ == "__main__":
    
    # Set up the asyncio event loop and execute the asynchronous tasks within the main() function.
    asyncio.run(main())
