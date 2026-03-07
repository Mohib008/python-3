# Working with Complex Numbers in Python 3

# 1. Creating Complex Numbers
# Python uses 'j' or 'J' for the imaginary unit (instead of 'i' commonly used in math)
z1 = 3 + 4j
print(f"Direct assignment: {z1}")  # Output: (3+4j)

# You can also use the complex(real, imag) constructor
z2 = complex(2, -5)
print(f"Using constructor: {z2}") # Output: (2-5j)

# 2. Accessing Parts
# Every complex object has .real and .imag attributes (floats)
print(f"Real part of z1: {z1.real}")
print(f"Imaginary part of z1: {z1.imag}")

# 3. Arithmetic Operations
# You can add, subtract, multiply, and divide complex numbers just like standard numbers
sum_z = z1 + z2
prod_z = z1 * z2

print(f"Addition ({z1} + {z2}): {sum_z}")
print(f"Multiplication ({z1} * {z2}): {prod_z}")

# 4. Conjugate
# The conjugate flips the sign of the imaginary part (a + bj becomes a - bj)
print(f"Conjugate of {z1}: {z1.conjugate()}")

# 5. Magnitude (Absolute Value)
# The abs() function returns the magnitude (distance from origin: sqrt(a^2 + b^2))
magnitude = abs(z1)  # sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5.0
print(f"Magnitude of {z1}: {magnitude}")
display = ((4 + 3j) * (2 - 5j)).conjugate() + abs(3 + 4j) - (1 + 2j).real;
#print(display);