
#ElGamal Cryptosystem

import random
import math

def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(initial_range, final_range):
    prime = random.randint(initial_range, final_range)
    while not is_prime(prime):
        prime = random.randint(initial_range, final_range)
    return prime

def find_primitive_root(p):
    # Find a primitive root modulo p
    primitive_roots = []
    for i in range(2, p):
        if math.gcd(i, p) == 1:
            primitive_roots.append(i)
    return random.choice(primitive_roots)

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d

# Generating two random large prime numbers
p = generate_prime(1000, 5000)
g = find_primitive_root(p) #e1

# Alice's private key
a = random.randint(2, p - 1) #d

# Alice's public key
A = pow(g, a, p)

print()
print("Prime number (p):", p)
print()
print("Primitive root (g):", g)
print()
print("Alice's private key (a):", a)
print()
print("Alice's public key (A):", A) #e2
print()


def elgamal_encrypt(plaintext, p, g, A):
    # Bob chooses a random secret key
    k = random.randint(2, p - 2)
    # Shared secret
    s = pow(A, k, p)
    # Ciphertext pair (c1, c2)
    c1 = pow(g, k, p)
   
    c2 = []
    for ch in plaintext:
       c2.append( (s * ord(ch)) % p)
     
    return c1, c2

def elgamal_decrypt(c1, c2, p, a):
    # Shared secret
    s = pow(c1, a, p)
    # Plaintext
    plaintext = ''
    for ch in c2:
       plaintext += chr((ch * mod_inverse(s, p)) % p)

    return plaintext


message = input("Enter the message: ")
print()
c1, c2 = elgamal_encrypt(message, p, g, A)
print("Ciphertext (c1, c2):", c1, c2)
print()
decrypted_message = elgamal_decrypt(c1, c2, p, a)
print("Decrypted message:", decrypted_message)