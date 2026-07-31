import random

# Convert text to binary
def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

# Calculate even parity bit
def parity(binary):
    return '0' if binary.count('1') % 2 == 0 else '1'

# Flip one random bit
def flip_bit(binary):
    index = random.randint(0, len(binary) - 1)
    flipped = '1' if binary[index] == '0' else '0'
    return binary[:index] + flipped + binary[index + 1:]

# Check parity
def check_parity(binary, parity_bit):
    return parity(binary) == parity_bit

# Checksum
def checksum(text):
    return sum(ord(c) for c in text)

# Corrupt one character
def corrupt_text(text):
    index = random.randint(0, len(text) - 1)
    new_char = chr(ord(text[index]) ^ 1)
    return text[:index] + new_char + text[index + 1:]

messages = ["Hello", "Network", "Python", "Packet", "CNLab"]

print("=== PARITY CHECK ===")
for msg in messages:
    binary = text_to_binary(msg)
    p = parity(binary)
    corrupted = flip_bit(binary)

    if check_parity(corrupted, p):
        print(f"{msg}: OK")
    else:
        print(f"{msg}: ERROR DETECTED")

print("\n=== CHECKSUM ===")
for msg in messages:
    original = checksum(msg)
    corrupted = corrupt_text(msg)
    new = checksum(corrupted)

    if original == new:
        print(f"{msg}: OK")
    else:
        print(f"{msg}: ERROR DETECTED")
