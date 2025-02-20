import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors

def generate_primes(end):
    return [num for num in range(2, end + 1) if is_prime(num)]

def main():
    print("Prime Number Analyzer")
    num = int(input("Enter a number: "))
    print(f"{num} is {'a prime' if is_prime(num) else 'not a prime'} number.")
    print(f"Prime factors: {prime_factors(num)}")
    end = int(input("Find primes up to: "))
    print(f"Prime numbers up to {end}: {generate_primes(end)}")

if __name__ == "__main__":
    main()
