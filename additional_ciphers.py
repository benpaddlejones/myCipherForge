"""Additional encryption techniques for CipherForge.

This module provides alternative encryption methods that can be used
as Phase 5 replacements or for experimentation.

Includes:
- XOR Encryption
- Vigenère Cipher
- Rail Fence Cipher
"""


def xor_encrypt(text, key):
    """XOR each character with a key value (printable-safe version).
    
    This version uses modular arithmetic to keep results in the
    printable ASCII range while maintaining reversibility.
    
    Args:
        text: The text to encrypt
        key: Dictionary containing "xor_value" (default: 42)
    
    Returns:
        Encrypted text in printable ASCII range
    """
    xor_key = key.get("xor_value", 42) % 95  # Keep within printable range
    result = []
    for char in text:
        if 32 <= ord(char) <= 126:
            # Map to 0-94 range, add key (mod 95), map back to 32-126
            pos = ord(char) - 32
            new_pos = (pos + xor_key) % 95  # Use addition instead of XOR for reversibility
            result.append(chr(new_pos + 32))
        else:
            result.append(char)
    return ''.join(result)


def xor_decrypt(text, key):
    """Reverse XOR encryption.
    
    Uses subtraction to reverse the addition-based cipher.
    """
    xor_key = key.get("xor_value", 42) % 95
    result = []
    for char in text:
        if 32 <= ord(char) <= 126:
            pos = ord(char) - 32
            new_pos = (pos - xor_key) % 95  # Subtract to reverse
            result.append(chr(new_pos + 32))
        else:
            result.append(char)
    return ''.join(result)


def vigenere_encrypt(text, key):
    """Vigenère cipher with repeating keyword (letters only).
    
    The Vigenère cipher was called "le chiffre indéchiffrable" 
    (the unbreakable cipher) for 300 years!
    
    Instead of shifting every letter by the same amount (like Caesar),
    Vigenère uses a keyword where each letter determines a different
    shift amount.
    
    Note: This classic Vigenère only encrypts letters (A-Z, a-z).
    Numbers, spaces, and symbols pass through unchanged.
    
    Args:
        text: The text to encrypt
        key: Dictionary containing "vigenere_key" (default: "KEY")
    
    Returns:
        Encrypted text with letters shifted
    """
    keyword = key.get("vigenere_key", "KEY")
    result = []
    key_index = 0  # Track position in keyword separately
    for char in text:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)].upper()) - ord('A')
            code = ord(char)
            if char.isupper():
                new_char = chr((code - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((code - ord('a') + shift) % 26 + ord('a'))
            result.append(new_char)
            key_index += 1  # Only advance key for letters
        else:
            result.append(char)
    return ''.join(result)


def vigenere_decrypt(text, key):
    """Reverse Vigenère cipher.
    
    Uses subtraction instead of addition for the shift.
    """
    keyword = key.get("vigenere_key", "KEY")
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(keyword[key_index % len(keyword)].upper()) - ord('A')
            code = ord(char)
            if char.isupper():
                new_char = chr((code - ord('A') - shift) % 26 + ord('A'))
            else:
                new_char = chr((code - ord('a') - shift) % 26 + ord('a'))
            result.append(new_char)
            key_index += 1
        else:
            result.append(char)
    return ''.join(result)


def rail_fence_encrypt(text, key):
    """Rail fence transposition cipher.
    
    The Rail Fence cipher writes the message in a zigzag pattern
    across multiple "rails" (rows), then reads each rail left-to-right.
    
    Example with 3 rails and "HELLO WORLD":
    Rail 1: H . . . O . . . R . .
    Rail 2: . E . L . . W . . L .
    Rail 3: . . L . . . . O . . D
    
    Result: HOR + ELWL + LOD = "HORELWLLOD"
    
    Args:
        text: The text to encrypt
        key: Dictionary containing "rails" (default: 3)
    
    Returns:
        Text with characters rearranged in rail fence pattern
    """
    rails = key.get("rails", 3)
    if rails < 2 or len(text) == 0:
        return text
    
    fence = [[] for _ in range(rails)]
    
    rail = 0
    direction = 1
    
    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    
    return ''.join([''.join(row) for row in fence])


def rail_fence_decrypt(text, key):
    """Reverse rail fence cipher.
    
    To decrypt, we first calculate how many characters go on each rail,
    split the ciphertext into those segments, then read in zigzag order.
    """
    rails = key.get("rails", 3)
    if rails < 2 or len(text) == 0:
        return text
    
    # First, calculate how many chars go on each rail
    rail_lengths = [0] * rails
    rail = 0
    direction = 1
    for _ in text:
        rail_lengths[rail] += 1
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    
    # Split ciphertext into rail segments
    fence = []
    pos = 0
    for length in rail_lengths:
        fence.append(list(text[pos:pos + length]))
        pos += length
    
    # Read off in zigzag order
    result = []
    rail = 0
    direction = 1
    for _ in text:
        result.append(fence[rail].pop(0))
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    
    return ''.join(result)


# Quick test function
if __name__ == "__main__":
    print("Testing additional ciphers...")
    
    # Test XOR
    key = {"xor_value": 42}
    original = "Hello World!"
    encrypted = xor_encrypt(original, key)
    decrypted = xor_decrypt(encrypted, key)
    print(f"XOR: {original} -> {encrypted} -> {decrypted}")
    assert decrypted == original, "XOR failed!"
    
    # Test Vigenère
    key = {"vigenere_key": "KEY"}
    original = "Hello World"
    encrypted = vigenere_encrypt(original, key)
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Vigenère: {original} -> {encrypted} -> {decrypted}")
    assert decrypted == original, "Vigenère failed!"
    
    # Test Rail Fence
    key = {"rails": 3}
    original = "Hello World!"
    encrypted = rail_fence_encrypt(original, key)
    decrypted = rail_fence_decrypt(encrypted, key)
    print(f"Rail Fence: {original} -> {encrypted} -> {decrypted}")
    assert decrypted == original, "Rail Fence failed!"
    
    print("\nAll additional ciphers working correctly!")
