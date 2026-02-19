# Issues Found in CipherForge Course Materials

> Document created as part of systematic testing and review of the CipherForge project instructions.
> Created: 19 February 2026

---

## Summary

After following the CipherForge course instructions as a student would, the following issues were identified. Issues are categorised by severity.

---

## Critical Issues

### C1: CP-instructions.md Describes Wrong Project

**Location:** `course/CP-instructions.md`

**Issue:** The Copilot instructions file describes a completely different project (ChatterBot AI chatbot) instead of CipherForge encryption. This would cause AI assistants to provide irrelevant guidance.

**Impact:** High - Students using GitHub Copilot or similar AI tools would receive guidance for the wrong project.

**Recommendation:** Replace CP-instructions.md with CipherForge-specific instructions (see new `.github/copilot-instructions.md` created as part of this review).

---

### C2: No Copilot Instructions for CipherForge

**Location:** Missing `.github/copilot-instructions.md`

**Issue:** There is no copilot-instructions.md file specific to the CipherForge project in the expected location.

**Impact:** High - AI coding assistants have no project context.

**Recommendation:** Create `.github/copilot-instructions.md` with CipherForge-specific guidance.

---

## Major Issues

### M1: Duplicate Key in devcontainer.json

**Location:** `.devcontainer/devcontainer.json`

**Issue:** The JSON file contains duplicate `hostRequirements` key entries, making it invalid JSON in strict parsers.

**Impact:** Medium - May cause issues with some JSON parsers or IDEs.

**Recommendation:** Remove the duplicate key, keeping only one `hostRequirements` section.

---

### M2: Copilot Disabled in VS Code Settings

**Location:** `.vscode/settings.json`

**Issue:** GitHub Copilot is explicitly disabled for Python, HTML, and CSS files:
```json
"github.copilot.enable": {
    "python": false,
    "html": false,
    "css": false
}
```

**Impact:** Medium - Contradicts using AI assistance as part of the learning activity.

**Recommendation:** Either enable Copilot for these languages or document why it's intentionally disabled.

---

### M3: Lesson JSON Files Lack Section Titles

**Location:** All lesson JSON files in `course/`

**Issue:** Markdown sections don't have descriptive titles in the JSON structure—titles are only embedded within the markdown content.

**Impact:** Low-Medium - Makes it harder to programmatically navigate or display lesson content.

**Recommendation:** Add `title` fields to markdown sections or document that titles should be extracted from the markdown heading.

---

## Minor Issues

### m1: README is Generic Template

**Location:** `README.md` (template repository version)

**Issue:** The initial README.md is a generic template that doesn't provide project-specific setup instructions.

**Impact:** Low - Students update this in Lesson 1, but initial clone is confusing.

**Recommendation:** Provide more specific placeholder content or instructions.

---

### m2: requirements.txt Contains Unexplained Packages

**Location:** `requirements.txt`

**Issue:** Contains `bcrypt` and `flask_wtf` packages that aren't used in the main lessons (only in optional extensions). No explanation provided.

**Impact:** Low - May confuse students about what packages they actually need.

**Recommendation:** Add comments explaining which packages are for core functionality vs extensions, or split into `requirements.txt` and `requirements-extensions.txt`.

---

### m3: Card Text Not Visible in Web Interface

**Location:** `templates/base.html` and `templates/index.html`

**Issue:** The Bootstrap cards use dark backgrounds but the card title and text classes don't have explicit white text colour set. This results in dark/invisible text on dark cards.

**Impact:** Medium - The homepage cards showing the 5 phases are unreadable.

**Recommendation:** Add explicit `color: #fff` or use Bootstrap's `text-light` classes for card content, or add CSS rules for `.card-title` and `.card-text` to ensure white text.

---

## Issues Encountered During Implementation

### I1: Empty String Edge Case in Phase 5

**Location:** `engine.py` - Phase 5 pair swap

**Issue:** The pair swap algorithm needed special handling for empty strings and single character strings.

**Resolution:** Added length check before processing.

---

### I2: Code Block Formatting in Lesson JSON

**Location:** Multiple lesson JSON files

**Issue:** Some code blocks in the JSON files have escaped newlines (`\n`) making them harder to read directly.

**Resolution:** This is expected JSON formatting—use a JSON viewer or parser to read properly.

---

## Recommendations for Course Improvement

1. **Replace CP-instructions.md** with CipherForge-specific content
2. **Create .github/copilot-instructions.md** for proper AI assistant context
3. **Fix duplicate JSON keys** in devcontainer.json
4. **Review Copilot settings** in .vscode/settings.json
5. **Add inline comments** to requirements.txt explaining each package
6. **Consider adding a "Common Issues" section** to each lesson for known stumbling blocks

---

## Testing Methodology

This review was conducted by:
1. Reading all lesson JSON files
2. Following instructions step-by-step as a student would
3. Implementing all required code
4. Running tests to verify functionality
5. Documenting issues as encountered

All 8 main lessons were completed successfully with the issues noted above.
