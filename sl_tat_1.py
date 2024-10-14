def getPentaNum(n):
    return (n * (3 * n - 1)) // 2

def pentaNumRange(n1, n2):
    penta_numbers = [getPentaNum(n) for n in range(n1, n2)]
    return penta_numbers

def sumDigit(num):
    return sum(int(digit) for digit in str(num))

gematria = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5,
    'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
    'כ': 20, 'ך':20, 'ל': 30, 'מ': 40,'ם': 40,'נ': 50, 'ן': 50, 'ס': 60,
    'ע': 70, 'פ': 80,'ף': 80, 'צ': 90,'ץ': 90, 'ק': 100, 'ר': 200,
    'ש': 300, 'ת': 400
}

def gematria_value(word):
    return sum(gematria[letter] for letter in word if letter in gematria)



import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def prime_twin(n):
    if is_prime(n):
        if is_prime(n + 2):
            return n + 2
        elif is_prime(n - 2):
            return n - 2
    return None


def prime_twins_dict(n):
    primes_twins = {}
    for i in range(2, n + 1):
        if is_prime(i):
            twin = prime_twin(i)

            primes_twins[i] = twin
    return primes_twins


def mult_2(x):
    return x * 2

def square(x):
    return x ** 2

def inverse(x):
    if x != 0:
        return 1 / x
    return "undefined"



def functions_dict(numbers, functions):
    result = {}
    for func in functions:
         result[func.__name__] = [func(num) for num in numbers]
    return result


