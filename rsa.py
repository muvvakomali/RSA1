from sympy import mod_inverse

# Helper function to compute gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# RSA Key Generation
def generate_keys(p, q):
    if p == q:
        raise ValueError("p and q must be distinct prime numbers.")
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Choose e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = 3
    while e < phi_n and gcd(e, phi_n) != 1:
        e += 2
    
    # Compute private key d
    d = mod_inverse(e, phi_n)
    
    return (e, n), (d, n)

# Encrypt a text message
def encrypt_text(message, public_key):
    e, n = public_key
    encrypted_numbers = [pow(ord(char), e, n) for char in message]  # Convert char to ASCII and encrypt
    return encrypted_numbers

# Decrypt an encrypted message
def decrypt_text(ciphertext, private_key):
    d, n = private_key
    decrypted_chars = [chr(pow(num, d, n)) for num in ciphertext]  # Decrypt and convert back to text
    return ''.join(decrypted_chars)

# User input for prime numbers
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

# Generate RSA keys
public_key, private_key = generate_keys(p, q)

# User input for message
message = input("Enter a message (text): ")

# Encrypt and decrypt
ciphertext = encrypt_text(message, public_key)
decrypted_message = decrypt_text(ciphertext, private_key)

# Output results
print(f"\nPrime p: {p}")
print(f"Prime q: {q}")
print(f"Public Key (e, n): {public_key}")
print(f"Private Key d: {private_key[0]}")
print(f"Original Message: {message}")
print(f"Ciphertext (Encrypted ASCII Values): {ciphertext}")
print(f"Decrypted Message: {decrypted_message}")



