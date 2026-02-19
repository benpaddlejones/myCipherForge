# Extension Issues Found

> Document created: 19 February 2026
> This document lists issues found when implementing the extensions from Lesson 9.

---

## Extension 1: Basic Authentication

### Issue E1.1: Decorator Order Not Clear
**Location:** Lesson 9, Extension 1, Step 3
**Severity:** Minor

The instruction says to add `@login_required` to the workshop route but doesn't clearly show where it should go relative to `@app.route`. The correct order is:

```python
@app.route("/workshop", methods=["GET", "POST"])
@login_required  # MUST be after @app.route
def workshop():
```

Students unfamiliar with decorator ordering may place it incorrectly.

---

## Extension 2: pytest

### Issue E2.1: Tests Folder Import Issues
**Location:** Lesson 9, Extension 2
**Severity:** Minor

The `conftest.py` setup works but relies on modifying `sys.path`. A cleaner approach would be to install the project as an editable package or use proper Python packaging.

---

## Extension 3: Additional Encryption Techniques

### Issue E3.1: XOR Cipher Code Is Broken
**Location:** Lesson 9, Extension 3, XOR Encryption section
**Severity:** **CRITICAL**

The XOR cipher code provided does NOT work correctly. The lesson code:

```python
pos = ord(char) - 32
xor_pos = pos ^ (xor_key % 95)
result.append(chr((xor_pos % 95) + 32))  # BUG HERE!
```

The `% 95` operation after XOR breaks the mathematical property that XOR is self-inverse. The code CANNOT correctly decrypt what it encrypts.

**Example of failure:**
- Original: "Hello World!" (72, 101, ...)
- Key: 42
- Position 72-32=40, XOR 40^42=2, (2%95)+32=34  ✓
- Position 101-32=69, XOR 69^42=111, (111%95)+32=48  ✗ (111 > 95 so mod changes value)

When decrypting, the same XOR operation doesn't reverse because the % operation lost information.

**Fix:** Either:
1. Limit xor_key to values that won't cause overflow (key < 32), OR
2. Use addition/subtraction instead of XOR (loses the "XOR is self-inverse" magic), OR  
3. Accept that output may contain non-printable characters (defeats the "printable-safe" claim)

The implementation I created uses addition/subtraction instead.

---

### Issue E3.2: Vigenère Example Mismatch
**Location:** Lesson 9, Extension 3, Vigenère Cipher section
**Severity:** Minor

The lesson's step-by-step example shows:
| Plaintext | H | E | L | L | O |
| Keyword   | K | E | Y | K | E |
| Result    | R | I | J | V | S |

But the actual output of the provided code for "HELLO WORLD" with keyword "KEY" would be "RIJVS UYVJN" (with the space and remaining letters). The example only shows 5 characters and doesn't demonstrate how the keyword cycles.

---

### Issue E3.3: Rail Fence Example Incorrect Character Count
**Location:** Lesson 9, Extension 3, Rail Fence section
**Severity:** Minor

The lesson shows:
> Result: HOR-EL WL-LOD → `"HORELWLLOD"`

But "HELLO WORLD" has 11 characters (including space), while "HORELWLLOD" has only 10. The space appears to be missing from the example output.

The actual output for "Hello World!" using the provided code is "Horel ol!lWd" (12 characters preserved).

---

## Extension 4: SQL Database

### Issue E4.1: JSON Truncation - Missing Code Steps
**Location:** Lesson 9, Extension 4
**Severity:** **MAJOR**

The lesson JSON for Extension 4 is truncated. The sections show:
- Step 1: Set Up the Database (complete)
- "Lines 128-129 omitted"
- "Lines 134-135 omitted"
- "Lines 140-141 omitted"

Students following along will not see:
- Step 2: Add user management functions (create_user, verify_user)
- Step 3: Update app.py to use the database instead of the USERS dictionary
- Step 4: Create registration form

This makes Extension 4 incomplete and impossible to follow without external research.

**Note:** This may be an LMS display issue rather than a source JSON issue.

---

### Issue E4.2: Incomplete Integration Instructions
**Location:** Lesson 9, Extension 4
**Severity:** Major

Even with the database.py module created, there are no clear instructions on how to:
1. Replace the simple USERS dictionary with database calls
2. Update the login route to use verify_user()
3. Add a registration route

Students would need to figure this out themselves.

---

## Summary

| Issue | Severity | Category |
|-------|----------|----------|
| E1.1 | Minor | Unclear instructions |
| E2.1 | Minor | Best practices |
| E3.1 | **Critical** | Broken code |
| E3.2 | Minor | Example mismatch |
| E3.3 | Minor | Example error |
| E4.1 | **Major** | Missing content |
| E4.2 | Major | Incomplete instructions |

**Critical issues requiring immediate fix:** E3.1 (XOR code doesn't work)
**Major issues:** E4.1, E4.2 (Extension 4 incomplete)
