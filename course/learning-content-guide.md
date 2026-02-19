# Learning Content Guide

> Complete documentation for creating and managing learning content in the HSC Software Engineering platform.
> **Last Updated**: February 2026

---

## Table of Contents

1. [Overview](#overview)
2. [Directory Structure](#directory-structure)
3. [Folder Naming Convention](#folder-naming-convention)
4. [Module Types](#module-types)
5. [Creating a Standard Module](#creating-a-standard-module)
6. [Creating an External Course](#creating-an-external-course)
7. [Lesson Page Structure](#lesson-page-structure)
8. [Section Types Reference](#section-types-reference)
9. [JSON Schema Reference](#json-schema-reference)
10. [Progress Tracking](#progress-tracking)
11. [Testing Content](#testing-content)

---

## Overview

The learning feature provides structured educational content organized into modules (courses) and pages (lessons). Content is defined in JSON files within the `app/content/learning/` directory.

### Key Concepts

| Concept             | Description                                                       |
| ------------------- | ----------------------------------------------------------------- |
| **Module**          | A course/topic (e.g., "Number Systems") containing multiple pages |
| **Page**            | A lesson within a module containing sections                      |
| **Section**         | A content block (markdown, code activity, MCQ, etc.)              |
| **External Course** | A module linking to content hosted elsewhere (e.g., GitHub)       |
| **Submodule**       | A topic within an external course that students can mark complete |

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Learning Dashboard                      │
│  ┌─────────────────────┐    ┌─────────────────────────────┐ │
│  │     Year 11         │    │        Year 12 HSC          │ │
│  │  (Preliminary)      │    │      (HSC Course)           │ │
│  └─────────────────────┘    └─────────────────────────────┘ │
├─────────────────────────────────────────────────────────────┤
│  Module Cards: [Title] [Progress Badge] [External Badge]    │
└─────────────────────────────────────────────────────────────┘
         │                              │
         ▼                              ▼
┌─────────────────┐          ┌────────────────────────┐
│ Standard Module │          │   External Course      │
│  - Pages list   │          │  - Submodule checklist │
│  - Progress %   │          │  - External links      │
└─────────────────┘          └────────────────────────┘
```

---

## Directory Structure

```
app/content/learning/
├── _page_schema.json         # JSON schema for lesson pages
├── _module_schema.json       # JSON schema for module.json files
├── 11.1.number-systems/      # Year 11, Order 1: Number Systems
│   ├── module.json           # Module metadata
│   ├── 1.number-systems.json # Lesson 1
│   ├── 2.twos-complement.json
│   └── 3.standard-data-types.json
├── 11.2.intro-to-algorithms/
│   ├── module.json
│   ├── 1.what-is-an-algorithm.json
│   └── ...
├── 12.1.advanced-algorithms/  # Year 12 module
│   └── module.json
└── 12.3.learn-sql-basics/     # External course
    └── module.json            # Contains submodules array
```

---

## Folder Naming Convention

Module folders follow the pattern: `{YEAR}.{ORDER}.{SLUG}`

| Component | Description                                  | Example          |
| --------- | -------------------------------------------- | ---------------- |
| `YEAR`    | 11 (Preliminary) or 12 (HSC)                 | `11`, `12`       |
| `ORDER`   | Display order within the year (1-99)         | `1`, `2`, `10`   |
| `SLUG`    | URL-friendly identifier (lowercase, hyphens) | `number-systems` |

### Examples

```
11.1.number-systems        → Year 11, 1st module
11.2.intro-to-algorithms   → Year 11, 2nd module
12.1.advanced-algorithms   → Year 12, 1st module
12.3.learn-sql-basics      → Year 12, 3rd module (external)
```

### Parsing Logic

The system extracts:

- **Year**: First number (11 or 12)
- **Order**: Second number (course_order)
- **Module ID**: The slug portion after the second dot

---

## Module Types

### Standard Module (Local Content)

A module with lesson pages stored in JSON files.

**Required files:**

- `module.json` - Module metadata
- `*.json` lesson files (at least one)

**Example: `11.1.number-systems/module.json`**

```json
{
  "id": "number-systems",
  "title": "Number Systems & Data Representation",
  "description": "Understand how computers represent data at the binary level.",
  "order": 1,
  "prerequisites": [],
  "learning_outcomes": [
    "Convert between binary, decimal, and hexadecimal",
    "Understand two's complement representation",
    "Apply appropriate data types in programs"
  ]
}
```

### External Course (Linked Content)

A module that links to content hosted elsewhere (GitHub, external LMS, etc.).

**Required files:**

- `module.json` only (no lesson files)

**Required fields:**

- `is_external: true`
- `external_url` - Base URL for the course
- `submodules` - Array of topics students can mark complete

**Example: `12.3.learn-sql-basics/module.json`**

```json
{
  "id": "learn-sql-basics",
  "title": "Learn SQL Basics",
  "description": "A hands-on SQL course using a Star Wars-themed database!",
  "order": 3,
  "is_external": true,
  "external_url": "https://github.com/TempeHS/Learn_SQL_Basics/tree/main",
  "learning_outcomes": [
    "Write SELECT queries with WHERE filters",
    "Perform table joins to combine data"
  ],
  "submodules": [
    {
      "id": "intro-databases-sqlite",
      "title": "Introduction to Databases & SQLite Setup",
      "description": "Learn what databases are and set up SQLite",
      "url": "https://github.com/TempeHS/Learn_SQL_Basics/tree/main/1.Intro_to_Databases"
    },
    {
      "id": "select-where",
      "title": "Selecting and Filtering Data",
      "description": "Write your first SQL queries",
      "url": "https://github.com/TempeHS/Learn_SQL_Basics/tree/main/2.Selecting_Filtering_Data"
    }
  ]
}
```

---

## Creating a Standard Module

### Step 1: Create the Module Directory

```bash
mkdir learning/11.5.my-new-module
```

### Step 2: Create `module.json`

```json
{
  "id": "my-new-module",
  "title": "My New Module",
  "description": "A brief description of what students will learn.",
  "order": 5,
  "prerequisites": ["number-systems"],
  "learning_outcomes": ["First learning outcome", "Second learning outcome"]
}
```

### Step 3: Create Lesson Files

Lesson files follow the pattern: `{ORDER}.{SLUG}.json`

**Example: `1.introduction.json`**

```json
{
  "id": "introduction",
  "title": "Introduction to the Topic",
  "description": "Overview of what we'll cover.",
  "order": 1,
  "estimated_duration": "20-30 minutes",
  "learning_outcomes": ["Understand the basics", "Identify key concepts"],
  "sections": [
    {
      "type": "markdown",
      "title": "Welcome",
      "content": {
        "text": "## Welcome to This Module\n\nIn this lesson, you will learn..."
      }
    },
    {
      "type": "mcq",
      "title": "Check Your Understanding",
      "content": {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
        "correct_index": 2,
        "explanation": "Canberra is the capital of Australia."
      }
    }
  ]
}
```

---

## Creating an External Course

### Step 1: Create the Module Directory

```bash
mkdir learning/12.4.external-course-name
```

### Step 2: Create `module.json` with External Fields

```json
{
  "id": "external-course-name",
  "title": "External Course Title",
  "description": "Description of the external course.",
  "order": 4,
  "is_external": true,
  "external_url": "https://github.com/org/repo",
  "learning_outcomes": ["What students will learn"],
  "submodules": [
    {
      "id": "topic-1",
      "title": "First Topic",
      "description": "What this topic covers",
      "url": "https://github.com/org/repo/tree/main/Topic1"
    },
    {
      "id": "topic-2",
      "title": "Second Topic",
      "description": "What this topic covers"
    }
  ]
}
```

**Note:** If a submodule doesn't have a `url`, students will be directed to the module's `external_url`.

---

## Lesson Page Structure

Each lesson page contains an array of **sections** displayed in order.

```json
{
  "id": "lesson-id",
  "title": "Lesson Title",
  "description": "Brief description",
  "order": 1,
  "estimated_duration": "30-45 minutes",
  "learning_outcomes": ["Outcome 1", "Outcome 2"],
  "sections": [
    { "type": "markdown", "content": { "text": "..." } },
    { "type": "python", "content": { "description": "...", "starter_code": "..." } },
    { "type": "mcq", "content": { "question": "...", "options": [...], "correct_index": 0 } }
  ]
}
```

---

## Section Types Reference

### 1. Markdown Section

For explanatory content with rich formatting.

```json
{
  "type": "markdown",
  "title": "Optional Title",
  "content": {
    "text": "## Heading\n\nParagraph with **bold** and *italic* text.\n\n| Column 1 | Column 2 |\n|----------|----------|\n| Value A  | Value B  |"
  }
}
```

**Supports:** Headings, tables, code blocks, lists, blockquotes, links, images.

---

### 2. Python Code Activity

Interactive Python coding exercise with test cases.

```json
{
  "type": "python",
  "title": "Activity: Calculate Average",
  "content": {
    "description": "Write a function that calculates the average of a list of numbers.",
    "starter_code": "def calculate_average(numbers):\n    # Your code here\n    pass\n\n# Test\nprint(calculate_average([1, 2, 3, 4, 5]))",
    "example_answer": "def calculate_average(numbers):\n    return sum(numbers) / len(numbers)",
    "test_cases": [
      {
        "input": "calculate_average([1, 2, 3, 4, 5])",
        "expected": "3.0"
      },
      {
        "input": "calculate_average([10, 20])",
        "expected": "15.0",
        "hidden": true
      }
    ],
    "hints": [
      "Use the sum() function to add all numbers",
      "Divide by len() to get the average"
    ]
  }
}
```

---

### 3. Pseudocode Activity

Practice writing HSC-standard pseudocode.

```json
{
  "type": "pseudocode",
  "title": "Write Pseudocode: Find Maximum",
  "content": {
    "description": "Write pseudocode to find the maximum value in a list.",
    "starter_code": "BEGIN\n    # Your pseudocode here\nEND",
    "example_answer": "BEGIN\n    max = list[0]\n    FOR EACH item IN list\n        IF item > max THEN\n            max = item\n        ENDIF\n    ENDFOR\n    RETURN max\nEND",
    "hints": ["Start by assuming the first item is the maximum"],
    "validation_rules": {
      "must_contain": ["BEGIN", "END", "IF", "THEN"],
      "min_lines": 5
    }
  }
}
```

---

### 4. Flowchart Activity

Create flowcharts using the Draw.io editor.

```json
{
  "type": "flowchart",
  "title": "Design a Flowchart",
  "content": {
    "description": "Create a flowchart for a login process.",
    "starter_xml": "<mxGraphModel>...</mxGraphModel>",
    "example_answer_xml": "<mxGraphModel>...</mxGraphModel>",
    "hints": [
      "Start with a terminal symbol",
      "Use decision diamonds for yes/no questions"
    ]
  }
}
```

---

### 5. Multiple Choice Question (MCQ)

Quick comprehension checks.

```json
{
  "type": "mcq",
  "title": "Check Your Understanding",
  "content": {
    "question": "Which data type would you use to store a person's age?",
    "options": ["String", "Integer", "Float", "Boolean"],
    "correct_index": 1,
    "explanation": "Age is a whole number, so Integer is the most appropriate type."
  }
}
```

---

### 6. Written Response

Open-ended text questions.

```json
{
  "type": "written_response",
  "title": "Explain in Your Own Words",
  "content": {
    "description": "Explain why binary is used in computers instead of decimal.",
    "example_answer": "Binary is used because computer circuits use transistors that have two states: on (1) and off (0). This makes binary a natural fit for electronic hardware.",
    "min_words": 50,
    "max_words": 200
  }
}
```

---

### 7. Draw.io Static Diagram

Display a pre-made diagram (not editable).

```json
{
  "type": "drawio",
  "title": "System Architecture",
  "content": {
    "xml": "<mxGraphModel>...</mxGraphModel>",
    "caption": "Figure 1: High-level system architecture"
  }
}
```

---

### 8. Structure Chart Activity

```json
{
  "type": "structure_chart",
  "title": "Design a Structure Chart",
  "content": {
    "description": "Create a structure chart for a calculator program.",
    "hints": ["Break the problem into main functions"]
  }
}
```

---

### 9. Data Flow Diagram (DFD) Activity

```json
{
  "type": "dfd",
  "title": "Create a DFD",
  "content": {
    "description": "Design a context diagram for an online shopping system.",
    "hints": ["Identify external entities first"]
  }
}
```

---

### 10. Video Section

Embed YouTube videos with optional description.

```json
{
  "type": "video",
  "title": "Watch: Introduction to Algorithms",
  "content": {
    "youtube_id": "xPvuJB33Fco",
    "description": "Watch this video introduction before continuing with the lesson."
  }
}
```

**Fields:**
| Field | Required | Description |
|-------|----------|-------------|
| `youtube_id` | Yes | YouTube video ID (the part after `v=` in the URL) |
| `description` | No | Text displayed below the video |

---

### 11. Data Dictionary Activity

Interactive data dictionary builder for defining data elements.

```json
{
  "id": "product-data-dictionary",
  "type": "data_dictionary",
  "title": "Product Data Dictionary",
  "description": "Create a complete data dictionary for an online store product.",
  "content": {
    "instructions": "Build a data dictionary for product records.",
    "required_fields": 5,
    "min_fields": 2,
    "hints": [
      "Product IDs are typically integers that auto-increment",
      "Prices need decimal places — use Real/Float"
    ],
    "starter_data": [
      {
        "name": "productID",
        "type": "Integer",
        "size": "8 digits",
        "description": "",
        "constraints": "",
        "source": ""
      }
    ]
  }
}
```

**Fields:**
| Field | Required | Description |
|-------|----------|-------------|
| `instructions` | No | Instructions for the activity |
| `required_fields` | No | Number of fields students must complete |
| `min_fields` | No | Minimum fields for validation (default: 2) |
| `hints` | No | Progressive hints array |
| `starter_data` | No | Pre-populated field entries |

---

## JSON Schema Reference

### Module Schema (`_module_schema.json`)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "LearningModule",
  "type": "object",
  "required": ["id", "title"],
  "properties": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9-]+$",
      "description": "Unique identifier (lowercase, hyphens allowed)"
    },
    "title": { "type": "string" },
    "description": { "type": "string" },
    "order": { "type": "integer", "minimum": 1 },
    "prerequisites": {
      "type": "array",
      "items": { "type": "string" }
    },
    "learning_outcomes": {
      "type": "array",
      "items": { "type": "string" }
    },
    "is_external": { "type": "boolean", "default": false },
    "external_url": { "type": "string", "format": "uri" },
    "submodules": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "title"],
        "properties": {
          "id": { "type": "string", "pattern": "^[a-z0-9-]+$" },
          "title": { "type": "string" },
          "description": { "type": "string" },
          "url": { "type": "string", "format": "uri" }
        }
      }
    }
  }
}
```

### Lesson Page Schema (`_page_schema.json`)

The full schema is available in `app/content/learning/_page_schema.json`. Key definitions:

| Definition                  | Purpose                                  |
| --------------------------- | ---------------------------------------- |
| `markdownContent`           | Text content for markdown sections       |
| `codeActivityContent`       | Python activities with test cases        |
| `pseudocodeActivityContent` | Pseudocode activities with validation    |
| `diagramActivityContent`    | Flowchart/DFD/Structure chart activities |
| `mcqContent`                | Multiple choice questions                |
| `writtenContent`            | Open-ended response questions            |
| `drawioContent`             | Static Draw.io diagrams                  |
| `videoContent`              | YouTube embedded videos                  |

---

## Section Minimum Requirements

Sections must meet minimum content requirements before they can be marked complete. This ensures students engage meaningfully with the content.

### Default Requirements by Section Type

| Section Type       | Requirement              | Default Value                    |
| ------------------ | ------------------------ | -------------------------------- |
| `written_response` | Minimum words            | 20 words                         |
| `python`           | Minimum lines            | 3 lines (non-comment, non-empty) |
| `python`           | Must differ from starter | Yes                              |
| `pseudocode`       | Minimum lines            | 3 lines                          |
| `pseudocode`       | Must differ from starter | Yes                              |
| `flowchart`        | Minimum shapes           | 3 shapes                         |
| `flowchart`        | Minimum connectors       | 1 connector                      |
| `dfd`              | Minimum shapes           | 3 shapes                         |
| `dfd`              | Minimum connectors       | 1 connector                      |
| `structure_chart`  | Minimum shapes           | 2 shapes                         |
| `structure_chart`  | Minimum connectors       | 1 connector                      |
| `data_dictionary`  | Minimum fields           | 2 fields                         |
| `mcq`              | Answer selected          | Yes                              |

### AI Feedback Requirement

Some sections require students to request AI feedback before completion:

- `pseudocode`
- `flowchart`
- `dfd`
- `structure_chart`

This encourages students to validate their work before moving on.

### Validation Messages

When requirements are not met, students see specific feedback:

- "Please write at least 20 words"
- "Please write at least 3 lines of code"
- "Your code must differ from the starter code"
- "Please add at least 3 shapes to your diagram"
- "Please request AI feedback before marking complete"

---

## Progress Tracking

### Standard Modules

Progress is tracked per-page:

- **Page visit**: Recorded when user views a page
- **Page complete**: All activities on the page submitted
- **Module complete**: All pages completed

### External Courses

Progress is tracked per-submodule:

- Students manually check off completed topics
- Progress stored as: `{module_id}/{submodule_id}`
- Module complete when all submodules checked

### Database Storage

Progress is stored in the `learning_progress` table:

| Column         | Type     | Description                  |
| -------------- | -------- | ---------------------------- |
| `user_id`      | String   | GitHub user ID               |
| `page_id`      | String   | Page or submodule identifier |
| `is_complete`  | Boolean  | Whether marked complete      |
| `visited_at`   | DateTime | First visit timestamp        |
| `completed_at` | DateTime | Completion timestamp         |

---

## Testing Content

### Validate JSON Syntax

```bash
# Check all learning content
python -m pytest tests/test_learning_json_content.py -v
```

### Test Module Loading

```bash
python -c "
from app.services.learning_service import get_learning_service
service = get_learning_service()
for m in service.get_all_modules():
    print(f'{m.year}.{m.course_order} - {m.title}')
    print(f'  Pages: {len(m.pages)}, External: {m.is_external}')
"
```

### Common Validation Errors

| Error                       | Cause                                 | Fix                        |
| --------------------------- | ------------------------------------- | -------------------------- |
| Missing required field      | JSON missing `id`, `title`, etc.      | Add the required field     |
| Invalid ID format           | IDs with uppercase or spaces          | Use lowercase with hyphens |
| MCQ missing options         | `correct_index` but no `options`      | Add options array          |
| External without submodules | `is_external: true` but no submodules | Add submodules array       |

---

## Best Practices

### Content Guidelines

1. **Keep lessons focused** - Each page should cover one concept
2. **Interleave activities** - Don't put all activities at the end
3. **Progressive hints** - Order hints from general to specific
4. **Test your test cases** - Ensure expected outputs are correct
5. **Use markdown tables** - Great for comparisons and reference

### Naming Conventions

- **Module IDs**: `topic-name` (e.g., `number-systems`)
- **Lesson IDs**: `topic-subtopic` (e.g., `twos-complement`)
- **Submodule IDs**: `topic-name` (e.g., `intro-databases-sqlite`)

### External Courses

1. **Verify URLs** - Ensure all external links are accessible
2. **Match submodules to content** - Each submodule should map to a distinct topic
3. **Provide descriptions** - Help students understand what each topic covers
4. **Update when source changes** - Keep submodules in sync with external content

---

## Quick Reference

### Create Standard Module Checklist

- [ ] Create folder: `{YEAR}.{ORDER}.{SLUG}/`
- [ ] Create `module.json` with id, title, description
- [ ] Add learning_outcomes array
- [ ] Create at least one lesson file: `{ORDER}.{SLUG}.json`
- [ ] Add sections array to each lesson
- [ ] Run tests: `pytest tests/test_learning_json_content.py`

### Create External Course Checklist

- [ ] Create folder: `{YEAR}.{ORDER}.{SLUG}/`
- [ ] Create `module.json` with `is_external: true`
- [ ] Add `external_url` pointing to course root
- [ ] Add `submodules` array with id, title for each topic
- [ ] Optionally add `url` overrides for specific submodules
- [ ] Run tests to validate

---

## Related Documentation

- [AI Feedback Guide](ai-feedback-guide.md) - How AI feedback works
- [Challenges Content Guide](challenges-content-guide.md) - Challenge JSON format
- [High-Level Design](high-level-design.md) - System architecture
