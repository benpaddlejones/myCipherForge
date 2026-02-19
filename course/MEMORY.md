# Memory Document: CipherForge Project Testing & Review

> This document guides the systematic testing and review of the CipherForge project instructions.
> Created: 19 February 2026
> Last Updated: 19 February 2026

---

## 1. Project Understanding

### What This Project Actually Is
- **CipherForge**: A 5-phase encryption algorithm project for secondary students
- Students build a complete encryption system from scratch
- Culminates in a Flask web interface to showcase their work
- **9 lessons** delivered via JSON files in `course/` folder

### Learning Outcomes
1. Set up Git repository with proper licensing and documentation
2. Understand ASCII encoding with `ord()` and `chr()`
3. Design Phase 1: Substitution cipher
4. Design Phase 2: Transposition (scrambling positions)
5. Design Phase 3: Password-based encryption with variable shifts
6. Design Phase 4: Noise injection to defeat frequency analysis
7. Design Phase 5: Wild card (student's own invention)
8. Build Flask web application
9. Write test suites and documentation

### Critical Problem Discovered
**CP-instructions.md describes a COMPLETELY DIFFERENT PROJECT** (ChatterBot chatbot) - NOT this CipherForge encryption project. This is a major issue.

---

## 2. Current Repository State (After Fork)

### Files Present
| File | Status | Notes |
|------|--------|-------|
| `requirements.txt` | ⚠️ WRONG | Has Flask/bcrypt/flask_wtf - sufficient for final project but unclear |
| `README.md` | ⚠️ TEMPLATE | Generic template only |
| `LICENSE` | ✅ OK | MIT License present |
| `.gitignore` | ✅ OK | Standard Python gitignore |
| `.devcontainer/` | ✅ OK | Python 3.11 Codespace config |
| `.vscode/` | ✅ OK | VS Code settings |
| `course/` | ✅ OK | 9 JSON lesson files + module.json |
| `course/CP-instructions.md` | ❌ WRONG PROJECT | Describes ChatterBot, not CipherForge |

### Files Students Must Create
| File | Created In | Purpose |
|------|------------|---------|
| `engine.py` | Lesson 2 | Core encryption/decryption functions |
| `app.py` | Lesson 7 | Flask web application |
| `templates/base.html` | Lesson 7 | HTML base template |
| `templates/index.html` | Lesson 7 | Main page |
| `templates/workshop.html` | Lesson 7 | Encryption workshop page |
| `test_engine.py` | Lesson 8 | Pytest test suite |

---

## 3. Required Commits (From Instructions)

| Lesson | Commit Message | Description |
|--------|----------------|-------------|
| 1 | `docs: set up initial README for CipherForge` | Initial README update |
| 2 | `feature: add simple_shift and simple_unshift functions` | First cipher functions |
| 3 | `feature: implement Phase 1 substitution cipher with master functions` | Phase 1 complete |
| 4 | `feature: implement Phase 2 transposition with block reversal` | Phase 2 complete |
| 5 | `feature: implement Phase 3 password-based encryption` | Phase 3 complete |
| 6 | `feat: Complete 5-phase encryption algorithm` | Phases 4 & 5 complete |
| 7 | `feat: Add Flask web interface for CipherForge` | Web interface done |
| 8 | `feat: Add test suite and complete documentation` | Testing & docs done |
| 9 | `feat: Add extensions (auth, pytest, etc.)` | Extensions (optional) |

---

## 4. Tasks To Complete

### Phase 1: Document All Issues ⏳ IN PROGRESS
- [x] Read all lesson JSON files
- [x] Identify what files need to be created
- [x] Extract all required commit messages
- [ ] Follow instructions step-by-step as a student would
- [ ] Document every issue encountered

### Phase 2: Execute Instructions as Student
- [ ] Lesson 1: Set up repository (README update)
- [ ] Lesson 2: Create engine.py with simple_shift/simple_unshift
- [ ] Lesson 3: Implement Phase 1 functions
- [ ] Lesson 4: Implement Phase 2 functions
- [ ] Lesson 5: Implement Phase 3 functions
- [ ] Lesson 6: Implement Phases 4 & 5
- [ ] Lesson 7: Create Flask app and templates
- [ ] Lesson 8: Create test suite

### Phase 3: Create Deliverables
- [ ] Create `course/ISSUES_FOUND.md` with all problems found
- [ ] Create `.github/copilot-instructions.md` for this specific project

---

## 5. Issues Found So Far

### CRITICAL ISSUES

| # | Issue | Impact | Location |
|---|-------|--------|----------|
| C1 | CP-instructions.md is for WRONG PROJECT (ChatterBot not CipherForge) | Complete confusion | `course/CP-instructions.md` |
| C2 | No copilot-instructions.md exists for CipherForge | AI assistant has wrong context | Missing file |

### MAJOR ISSUES

| # | Issue | Impact | Location |
|---|-------|--------|----------|
| M1 | devcontainer.json has duplicate `hostRequirements` key | Invalid JSON | `.devcontainer/devcontainer.json` |
| M2 | Copilot disabled for Python/HTML/CSS in settings | Contradicts using AI assistant | `.vscode/settings.json` |
| M3 | Lessons have no titles on markdown sections | Poor accessibility | All lesson JSON files |

### MINOR ISSUES

| # | Issue | Impact | Location |
|---|-------|--------|----------|
| m1 | README is generic template | Not project-specific | `README.md` |
| m2 | requirements.txt has bcrypt/flask_wtf but no explanation | May confuse students | `requirements.txt` |

### POTENTIAL STUDENT PROBLEMS (To Verify)

| # | Potential Issue | Test Required |
|---|-----------------|---------------|
| P1 | Instructions may not match current Codespaces UI | Follow UI steps |
| P2 | Code blocks may have errors | Run all code samples |
| P3 | Missing instructions for file creation in some lessons | Follow step-by-step |
| P4 | Lesson JSON content may reference things not explained | Read full context |

---

## 6. Execution Plan

### Step 1: Follow Lesson 1 Instructions
- Update README as instructed
- Make commit with exact message: `docs: set up initial README for CipherForge`
- Push to GitHub

### Step 2: Follow Lesson 2 Instructions
- Create `engine.py`
- Add `simple_shift` and `simple_unshift` functions
- Test in Python REPL
- Make commit: `feature: add simple_shift and simple_unshift functions`
- Push

### Step 3-6: Follow Phases 1-5
- Continue implementing each phase
- Make commits as specified
- Document any issues

### Step 7: Follow Lesson 7 (Flask)
- Create `app.py` and templates
- Test web interface
- Make commit

### Step 8: Follow Lesson 8 (Testing)
- Create test suite
- Make commit

### Final: Create Deliverables
- Document all issues found in `course/ISSUES_FOUND.md`
- Create proper `copilot-instructions.md` for CipherForge

---

## 7. Progress Log

| Timestamp | Action | Result |
|-----------|--------|--------|
| 09:20 | Initial exploration | Found CP-instructions.md is WRONG PROJECT |
| 09:25 | Read all lesson JSONs | Mapped structure and commits |
| 09:30 | Created MEMORY.md | This document |
| NEXT | Begin Lesson 1 execution | ... |

---

## 8. Reference: Lesson Structure

### Lesson 1: Setting Up Your CipherForge Repository (26 sections)
- Fork template, rename repository
- Update README
- Understand MIT License
- Commit messages style guide

### Lesson 2: Codespaces, ASCII, and Your First Cipher (28 sections)
- Open Codespace
- Learn ASCII with ord()/chr()
- Create engine.py
- Write simple_shift and simple_unshift

### Lesson 3: Phase 1: Building Your Substitution Layer (20 sections)
- Design phase1_encrypt/phase1_decrypt
- Create master encrypt/decrypt functions

### Lesson 4: Phase 2: Transposition (22 sections)
- Block reversal technique
- phase2_encrypt/phase2_decrypt

### Lesson 5: Phase 3: Password-Based Encryption (22 sections)
- Variable shifts based on password
- phase3_encrypt/phase3_decrypt

### Lesson 6: Phases 4 & 5 (17 sections)
- Noise injection (Phase 4)
- Wild card - student's invention (Phase 5)

### Lesson 7: Building the Flask Web Interface (13 sections)
- Create app.py with routes
- Create HTML templates
- Form handling

### Lesson 8: Testing and Documentation (11 sections)
- Create test_engine.py with pytest
- Complete README documentation

### Lesson 9: Extensions and Challenges (19 sections)
- Optional: user authentication, database, advanced tests

---

**NEXT ACTION**: Begin following instructions as a student, starting with Lesson 1.
