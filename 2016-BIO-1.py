# Promenade Fractions
from functools import lru_cache

def get_hcf(a, b):
    primes = [2]
    hcf = 1
    for prime in primes:
        if(a % prime == 0 and b % prime == 0):
            a /= prime
            b /= prime
            hcf *= prime

    for testing in range(3, max(a, b)+1, 2): # Every odd num up to and including

        is_prime = True
        for prime in primes:
            if(prime % testing == 0): # Divisible
                is_prime = False
                break
        if is_prime:
            primes.append(testing)
            current = testing

            while(a % current == 0 and b % current == 0):
                # Common factor
                hcf *= current
                a /= current
                b /= current
            while(a % current == 0):
                    a /= current
            while(b % current == 0):
                    b /= current

            if(a == 1 or b == 1):
                return hcf
    return hcf

@lru_cache(maxsize=None) # Save found fractions in dict
def simplify(frac:tuple):
    num = frac[0]
    denom = frac[1]
    # Get HCF and div both by it
    hcf = get_hcf(num, denom)
    return (num//hcf, denom//hcf)

    return (num, denom) # If both 1s, then will return as-is

def to_fraction(promenade):
    # Initial Values
    last_left_val = (1, 0)
    last_right_val = (0, 1)
    result = (1, 1)

    for choice in promenade:
        # Change value before L/R
        if(choice == "L"):
            # Left
            last_left_val = result
        else:
            # Right
            last_right_val = result
        result = (last_left_val[0] + last_right_val[0], last_left_val[1] + last_right_val[1])
        # Do not need to simplify - adding num&denom keeps CFs until end

    return simplify(result)

promenade = input()
print(to_fraction(promenade))

input()