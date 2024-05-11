def euclidean_algorithm(a:int, b:int):
    """
    Compute the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Parameters:
    - a: An integer
    - b: Another integer

    Returns:
    - The greatest common divisor (GCD) of a and b
    """
    # Ensure that a is greater than or equal to b
    if a < b:
        a, b = b, a
    while b != 0:
        # Compute the remainder of a divided by b
        remainder = a % b
        # Set a to b and b to the remainder
        a, b = b, remainder

    # The GCD is the value of a
    return a

# Example usage:
a = 66528
b = 52920
gcd = euclidean_algorithm(a, b)
print("GCD of", a, "and", b, "is:", gcd)
