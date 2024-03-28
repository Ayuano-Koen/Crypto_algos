
#  Rivest, Shamir, Adleman(RSA) Algorithm
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

def generate_prime(intial_range,final_range):
    prime = random.randint(intial_range,final_range)
    while not is_prime(prime):
        prime = random.randint(intial_range,final_range)
    return prime


def mod_inverse(e,phi):
    for d in range(3,phi):
        if(d*e)%phi==1:
            return d
        
        
# now taking two random large prime numbers

x,y = generate_prime(1000,5000),generate_prime(1000,5000)

# here in case we get two similar prime for that we checking here
while x==y:
    y = generate_prime(1000,5000)   

n = x*y
# euler totient function
phi_n = (x-1)*(y-1)

# to find the co-prime
e = random.randint(3,phi_n-1)

while math.gcd(e,phi_n)!=1:
    e = random.randint(3,phi_n-1)
 
d= mod_inverse(e,phi_n)

print()
print(" two prime numbers  x,y respectively are : ",x,y)   
print()
print("n = x*y :",n)
print()
print("Phi of n",phi_n)
print()
print("public key",e)
print()
print("private key",d)
print()
message = input("Enter the message :")
print()
message_encode = []  

for ch in message:
    message_encode.append(ord(ch))
    
ciphertext = []
for ch in message_encode:
    ciphertext.append(pow(ch, e, n))
print("Cypher-Text :",ciphertext)
print()
decrypted_message = []
for ch in ciphertext:
   decrypted_message.append(pow(ch, d, n)) 

print("decrypted_message :",decrypted_message)
print()
decrypted_string = ""
for ch in decrypted_message:
    decrypted_string += chr(ch)

print("Decrypted message : ",decrypted_string)
print()