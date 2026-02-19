# 🔐 CipherForge

**A custom 5-layer encryption algorithm** built as part of Year 9 Digital Technologies.

## About

This project implements a multi-layered encryption system that I designed from scratch. Each layer adds a different type of protection, similar to how real encryption algorithms like AES work.

## Algorithm Phases

| Phase | Name | Description | Status |
|-------|------|-------------|--------|
| 1 | Substitution | Shifts all characters by a fixed amount using ASCII values | ✅ Complete |
| 2 | Transposition | Reverses characters within blocks to scramble positions | ✅ Complete |
| 3 | Key-Dependent | Uses a password to create variable shifts per character | ✅ Complete |
| 4 | Noise Injection | Adds decoy characters to defeat frequency analysis | ✅ Complete |
| 5 | Wild Card | Swaps adjacent character pairs (pair swap) | ✅ Complete |

## How It Works

### Encryption
```
Plaintext → Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Ciphertext
```

### Decryption
```
Ciphertext → Phase 5 → Phase 4 → Phase 3 → Phase 2 → Phase 1 → Plaintext
```

Decryption MUST apply phases in **reverse order** to restore the original message.

## Usage

### Python API

```python
from engine import encrypt, decrypt

key = {
    "shift": 7,           # Phase 1: how much to shift
    "block_size": 4,      # Phase 2: block size for reversal
    "password": "SECRET", # Phase 3: encryption password
    "noise_interval": 3,  # Phase 4: insert noise every N chars
    "noise_char": "~"     # Phase 4: which character to use as noise
}

# Encrypt a message
ciphertext = encrypt("Hello World!", key)
print(ciphertext)  # Scrambled output

# Decrypt it back
plaintext = decrypt(ciphertext, key)
print(plaintext)   # "Hello World!"
```

### Web Interface

Run the Flask application:

```bash
python app.py
```

Then visit `http://localhost:5000` in your browser to use the workshop interface.

## Running Tests

```bash
python test_engine.py
```

## Files

| File | Purpose |
|------|---------|
| `engine.py` | Core encryption/decryption functions |
| `app.py` | Flask web application |
| `test_engine.py` | Test suite |
| `templates/` | HTML templates for web interface |

## Security Note

This is an educational project demonstrating encryption concepts. It is **NOT** suitable for protecting real sensitive data. Use established encryption libraries like `cryptography` for real applications.

## Author

**Test Student** — Year 9, 2026

## License

MIT License — see [LICENSE](LICENSE) for details.
