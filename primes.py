import time
largest_prime = 3

start_time = time.time()

def smallest_prime_divisor(num, largest_prime):
    """Find the smallest prime divisor of a number."""
    divchk = int(num ** 0.5) + 1
    for i in range(2, divchk + 1):
        if num % i == 0:
            return i
    return num  # return the number itself if no prime divisor is found
def next_iteration(index, number, largest_prime):
    """Get the next iteration of index, number, base, and increment."""
    
    base = (2 * index) - 1
    prime_divisor = smallest_prime_divisor(base, largest_prime)
    number = prime_divisor
    increment = (number - 1) // 2
    new_index = index + increment
    index = new_index
    
    return index, number, 

# Initial values
index = 3
number = 3

# Number of iterations
iterations = 500
print(f"Running {iterations} iterations...")
# Perform iterations
for _ in range(iterations + 1):
    print(f"Index: {index}, Number: {number}")
    print(f"iteration: {_}")
    if number > largest_prime:
        largest_prime = number
    index, number = next_iteration(index, number, largest_prime)
   

print(f"Largest prime calculated: {largest_prime}")
run_time = time.time() - start_time


if run_time > 1:
    print(f"--- {run_time} seconds ---")
else:
    print(f"--- {run_time * 1000} milliseconds ---")
