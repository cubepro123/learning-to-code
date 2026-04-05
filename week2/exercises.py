"""
week2 — Exercises
Try solving each exercise on your own before looking at the solution.
"""

# Exercise 1: FizzBuzz
# Print numbers 1-50. For multiples of 3 print Fizz,
# for multiples of 5 print Buzz, for both print FizzBuzz.
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0: print("FizzBuzz")
        elif i % 3 == 0: print("Fizz")
        elif i % 5 == 0: print("Buzz")
        else: print(i)

# Exercise 2: Fibonacci sequence
def fibonacci(n):
    """Return first n Fibonacci numbers."""
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

# Exercise 3: Check palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# Run exercises
if __name__ == "__main__":
    print("=== FizzBuzz (1-20) ===")
    fizzbuzz(20)
    print("\n=== Fibonacci (10 terms) ===")
    print(fibonacci(10))
    print("\n=== Palindrome check ===")
    for word in ["racecar", "hello", "level", "python"]:
        print(f"  {word!r}: {is_palindrome(word)}")
