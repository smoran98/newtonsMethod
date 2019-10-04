def sqrt(x):
    # Init. guess
    z = 1.0
    # Keep getting better est. for sqrt of x til you're 2 decimals
    while abs(z*z - x) >= 0.01:
        z-= (z*z - x) / (2*z)

    return z

print(sqrt(8.0))

z = sqrt(8.0)
print(z)
print(z*z)