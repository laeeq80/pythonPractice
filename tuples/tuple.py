def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder  # Return as a tuple

result = divide(10, 3)

# Tuple unpacking to get quotient and remainder
quotient, remainder = result
print(f"Quotient: {quotient}, Remainder: {remainder}")
