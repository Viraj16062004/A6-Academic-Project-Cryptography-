import string import collections
from itertools import permutations

# Helper function to clean text def clean_text(text):
return ''.join(filter(str.isalpha, text.upper()))

# Frequency analysis function def frequency_analysis(text):
text = clean_text(text)
freq = collections.Counter(text) total_chars = sum(freq.values())
return {char: round((count / total_chars) * 100, 2) for char, count in freq.items()}

# Brute-force attack for Caesar Cipher def caesar_brute_force(ciphertext):
for shift in range(26):
decrypted = ''.join(
chr(((ord(char) - 65 - shift) % 26) + 65) if char.isalpha() else char for char in ciphertext.upper()
)
print(f'Shift {shift}: {decrypted}')
# Dictionary attack for Caesar Cipher
def caesar_dictionary_attack(ciphertext, wordlist):
for shift in range(26):
decrypted = ''.join(
chr(((ord(char) - 65 - shift) % 26) + 65) if char.isalpha() else char for char in ciphertext.upper()
)
if any(word in decrypted for word in wordlist): print(f'Possible match with shift {shift}: {decrypted}')
# Vigenere Cipher encryption
 
def vigenere_encrypt(plaintext, key):
key = key.upper() encrypted = '' key_index = 0
for char in plaintext.upper():
if char.isalpha():
shift = ord(key[key_index]) - 65
encrypted += chr(((ord(char) - 65 + shift) % 26) + 65) key_index = (key_index + 1) % len(key)
else:
encrypted += char return encrypted

# Vigenere Cipher decryption
def vigenere_decrypt(ciphertext, key):
key = key.upper() decrypted = '' key_index = 0
for char in ciphertext.upper():
if char.isalpha():
shift = ord(key[key_index]) - 65
decrypted += chr(((ord(char) - 65 - shift) % 26) + 65) key_index = (key_index + 1) % len(key)
else:
decrypted += char return decrypted

# Simple substitution cipher decryption using frequency analysis def substitution_decrypt(ciphertext, mapping):
return ''.join(mapping.get(char, char) for char in ciphertext.upper())
# Detect the cipher type based on character distribution def detect_cipher(ciphertext):
char_set = set(ciphertext)
if all(char in string.ascii_uppercase for char in char_set): print("Likely a monoalphabetic substitution cipher")
elif any(char.isdigit() for char in char_set):
print("Might be a transposition cipher") else:
print("Unknown cipher type")

# Example usage
if   name  == "  main  ":
sample_text = "Wklv lv d whvw phvvdjh" # Encrypted with Caesar Cipher shift 3 print("Frequency Analysis:", frequency_analysis(sample_text))
print("\nBrute Forcing Caesar Cipher:") caesar_brute_force(sample_text)

print("\nVigenere Cipher Encryption:")
encrypted_text = vigenere_encrypt("HELLOWORLD", "KEY") print(f'Encrypted: {encrypted_text}')

print("\nVigenere Cipher Decryption:")
print(f'Decrypted: {vigenere_decrypt(encrypted_text, "KEY")}')

print("\nCipher Type Detection:") detect_cipher(sample_text)
