 #recursion
#1.1 - regular recursion
def create_tuple(n):
    if n == 1:
        return (1,)
    else:
        return (n,) + create_tuple(n - 1)

#1.2 - tail recursion
def create_tuple_tail(n):
    def helper(n, acc):
        if n == 0:
            return acc
        else:
            return helper(n - 1, (n,) + acc)

    return helper(n, ())


#result_regular_rec = create_tuple(1000)
#result_tail_rec = create_tuple_tail(1000)
#print(result_regular_rec)
#print(result_tail_rec)

#2.1 - regular recursion
def sum_elements(n):
    if len(n) == 0:
        return 0
    else:
        return n[0] + sum_elements(n[1:])

#print(sum_elements(create_tuple(10)))

#2.2 - tail recursion

def sum_elements_tail(n):
    def helper(n, acc):
        if len(n) == 0:
            return acc
        else:
            return helper(n[1:], acc + n[0])

    return helper(n, 0)

#print(sum_elements_tail(create_tuple_tail(10)))

#3.1 - regular recursion

def gcd(a, b):
     if b == 0:
        return a
     return gcd(b, a % b)

def lcm(a, b):
     return abs(a * b) // gcd(a, b)


#3.2 - tail recursion
def lcm_tail(a, b):
    def helper(multiple, a, b):
        if multiple % a == 0 and multiple % b == 0:
            return multiple
        else:
            return helper(multiple + 1, a, b)

    return helper(max(a,b), a, b)

#print(lcm_tail(9,3))


#4.1
def isPalindrome(num):
    # Convert the number to a string
    s = str(num)

    def checkPalindrome(s, left, right):
         if left >= right:
            return True
         if s[left] != s[right]:
            return False
         return checkPalindrome(s, left + 1, right - 1)

    return checkPalindrome(s, 0, len(s) - 1)

#4.2
def is_palindrome_tail(n):
     def helper(n, reversed_n, original):
         if n == 0:
             return reversed_n == original
         return helper(n // 10, reversed_n * 10 + n % 10, original)

     return helper(n, 0, n)


#5.1
def sortedzip(lists):
    # Sort each sublist using sorted
    sorted_lists = [sorted(lst) for lst in lists]

    # Recursive function to zip the sorted lists
    def zip_recursive(lists, index=0):
        if index >= len(sorted_lists[0]):
            return []  # Return an empty list when reaching the end
        # Create a tuple of the current elements from each list
        current_zip = tuple(lst[index] for lst in sorted_lists)
        # Combine current tuple with the result of the recursive call
        return [current_zip] + zip_recursive(lists, index + 1)

    return zip_recursive(sorted_lists)


# Example usage
result = sortedzip([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])
print(result)  # [(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]

#5.2
def tail_sortedzip(l):
    def helper(l):
        return [] if not l else [sorted(l[0])] + helper(l[1:])
    return zip(*helper(l))

print(list(tail_sortedzip([[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']])))


#Lazy Evaluation, Generators
#1.1
import time
import sys


def create_array():
    start_time = time.time()
    arr = list(range(10001))  # not lazy
    end_time = time.time()

    print(f"Execution time (eager): {end_time - start_time:.10f} seconds")
    print(f"Memory size: {sys.getsizeof(arr)} bytes")
    print(f"Type of array: {type(arr)}")

    return arr


not_lazy_array = create_array()


def create_lazy_array():
    start_time = time.time()
    arr = (x for x in range(10001))  #lazy - with generator
    end_time = time.time()

    print(f"Execution time (lazy): {end_time - start_time:.10f} seconds")
    print(f"Memory size: {sys.getsizeof(arr)} bytes")
    print(f"Type of array: {type(arr)}")

    return arr

lazy_array = create_lazy_array()

#1.2
def create_first_5000(full_array):
    start_time = time.time()  # התחלת מדידת זמן
    first_5000 = full_array[:5000]  # חיתוך המערך
    end_time = time.time()  # סיום מדידת זמן

    print(f"Execution time for first 5000 (eager): {end_time - start_time:.10f} seconds")
    print(f"Memory size: {sys.getsizeof(first_5000)} bytes")
    print(f"Type of new array: {type(first_5000)}")

    return first_5000

first_5000_array = create_first_5000(not_lazy_array)

def create_lazy_first_5000(lazy_array):
    start_time = time.time()  # התחלת מדידת זמן
    first_5000 = (x for i, x in enumerate(lazy_array) if i < 5000)  # גנרטור עם חיתוך
    end_time = time.time()  # סיום מדידת זמן

    print(f"Execution time for first 5000 (lazy): {end_time - start_time:.10f} seconds")
    print(f"Memory size: {sys.getsizeof(first_5000)} bytes")
    print(f"Type of new array: {type(first_5000)}")

    return first_5000

lazy_first_5000_array = create_lazy_first_5000(lazy_array)


#2

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
    num = 2  # Start from the first prime number
    while True:
        if is_prime(num):
            yield num  # Return the current prime number
        num += 1  # Move to the next number

# Example usage
prime_gen = prime_generator()
for k in range(10):  # Print the first 10 prime numbers
    print(next(prime_gen))


#3

import math

def power_function(exponent):
    return lambda base: base ** exponent

def power_map(n):
    return map(lambda exponent: power_function(exponent), range(n))

def taylor_generator(x):
    """Generator for Taylor series terms for e^x."""
    n = 0
    current_term = 1.0  # The first term (x^0 / 0!) is 1
    while True:
        yield current_term
        n += 1
        current_term *= x / n  # Update the term for x^n / n!

# Example usage
x=3
taylor_gen = taylor_generator(x)

# Print the first few terms of the Taylor series
for _ in range(8):
    print(next(taylor_gen))
