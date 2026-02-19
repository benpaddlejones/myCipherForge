"""pytest-style tests for CipherForge.

Run with: pytest -v

This module contains comprehensive tests for all 5 encryption phases
using pytest fixtures and parametrized tests.
"""

import pytest
from engine import (
    phase1_encrypt, phase1_decrypt,
    phase2_encrypt, phase2_decrypt,
    phase3_encrypt, phase3_decrypt,
    phase4_encrypt, phase4_decrypt,
    phase5_encrypt, phase5_decrypt,
    encrypt, decrypt
)


class TestPhase1:
    """Tests for Phase 1: Caesar shift."""
    
    @pytest.fixture
    def key(self):
        """Standard key for Phase 1 tests."""
        return {"shift": 5}
    
    def test_encrypt_changes_text(self, key):
        """Encryption should modify the original text."""
        original = "Hello"
        encrypted = phase1_encrypt(original, key)
        assert encrypted != original
    
    def test_decrypt_reverses_encrypt(self, key):
        """Decryption should restore original text."""
        original = "Hello World"
        encrypted = phase1_encrypt(original, key)
        decrypted = phase1_decrypt(encrypted, key)
        assert decrypted == original
    
    @pytest.mark.parametrize("text", [
        "a",
        "AB",
        "Hello World!",
        "123 abc XYZ",
        "Special: @#$%^&*()"
    ])
    def test_various_inputs(self, key, text):
        """Test with various input strings."""
        encrypted = phase1_encrypt(text, key)
        decrypted = phase1_decrypt(encrypted, key)
        assert decrypted == text


class TestPhase2:
    """Tests for Phase 2: Block reversal transposition."""
    
    @pytest.fixture
    def key(self):
        """Standard key for Phase 2 tests."""
        return {"block_size": 4}
    
    def test_encrypt_rearranges_text(self, key):
        """Encryption should rearrange character positions."""
        original = "ABCDEFGH"
        encrypted = phase2_encrypt(original, key)
        # Block reversal with size 4: ABCD -> DCBA, EFGH -> HGFE
        assert encrypted == "DCBAHGFE"
    
    def test_decrypt_reverses_encrypt(self, key):
        """Decryption should restore original text."""
        original = "Hello World!"
        encrypted = phase2_encrypt(original, key)
        decrypted = phase2_decrypt(encrypted, key)
        assert decrypted == original
    
    def test_self_inverse(self, key):
        """Block reversal is its own inverse."""
        original = "ABCD"
        twice = phase2_encrypt(phase2_encrypt(original, key), key)
        assert twice == original


class TestPhase3:
    """Tests for Phase 3: Password-based variable shift."""
    
    @pytest.fixture
    def key(self):
        """Standard key for Phase 3 tests."""
        return {"password": "SECRET"}
    
    def test_password_creates_variation(self, key):
        """Different password positions should create different shifts."""
        original = "AAAA"
        encrypted = phase3_encrypt(original, key)
        # Each 'A' should be shifted differently based on password letter
        chars = list(encrypted)
        # At least some characters should differ (unless password happens to cycle perfectly)
        assert encrypted != original
    
    def test_decrypt_reverses_encrypt(self, key):
        """Decryption should restore original text."""
        original = "Testing password encryption"
        encrypted = phase3_encrypt(original, key)
        decrypted = phase3_decrypt(encrypted, key)
        assert decrypted == original


class TestPhase4:
    """Tests for Phase 4: Noise injection."""
    
    @pytest.fixture
    def key(self):
        """Standard key for Phase 4 tests."""
        return {"noise_interval": 3, "noise_char": "~"}
    
    def test_encrypt_adds_noise(self, key):
        """Encryption should add noise characters."""
        original = "Hello"
        encrypted = phase4_encrypt(original, key)
        assert len(encrypted) > len(original)
        assert "~" in encrypted
    
    def test_decrypt_removes_noise(self, key):
        """Decryption should remove noise characters."""
        original = "Hello World"
        encrypted = phase4_encrypt(original, key)
        decrypted = phase4_decrypt(encrypted, key)
        assert decrypted == original


class TestPhase5:
    """Tests for Phase 5: Pair swap (wild card)."""
    
    @pytest.fixture
    def key(self):
        """Standard key for Phase 5 tests."""
        return {}  # Phase 5 may not need a key parameter
    
    def test_encrypt_swaps_pairs(self, key):
        """Encryption should swap adjacent character pairs."""
        original = "ABCD"
        encrypted = phase5_encrypt(original, key)
        assert encrypted == "BADC"
    
    def test_decrypt_reverses_encrypt(self, key):
        """Decryption should restore original text."""
        original = "Hello World!"
        encrypted = phase5_encrypt(original, key)
        decrypted = phase5_decrypt(encrypted, key)
        assert decrypted == original


class TestFullEncryption:
    """Tests for the complete 5-phase encryption system."""
    
    @pytest.fixture
    def full_key(self):
        """Complete key with all phase parameters."""
        return {
            "shift": 5,
            "block_size": 4,
            "password": "SECRET",
            "noise_interval": 3,
            "noise_char": "~"
        }
    
    def test_full_roundtrip(self, full_key):
        """Full encryption/decryption should preserve message."""
        original = "The quick brown fox jumps over the lazy dog!"
        encrypted = encrypt(original, full_key)
        decrypted = decrypt(encrypted, full_key)
        assert decrypted == original
    
    def test_encryption_transforms_text(self, full_key):
        """Encrypted text should differ from original."""
        original = "Secret Message"
        encrypted = encrypt(original, full_key)
        assert encrypted != original
    
    @pytest.mark.parametrize("message", [
        "",
        "A",
        "AB",
        "Short",
        "A longer message with spaces and punctuation!",
        "Numbers: 12345",
        "Symbols: !@#$%^&*()",
    ])
    def test_various_messages(self, full_key, message):
        """Test full encryption with various message types."""
        encrypted = encrypt(message, full_key)
        decrypted = decrypt(encrypted, full_key)
        assert decrypted == message


if __name__ == "__main__":
    pytest.main(["-v", __file__])
