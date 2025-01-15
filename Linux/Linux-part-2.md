# Welcome to Linux Part II

In this section, we explore more advanced Linux functions and commands, focusing on the use of regular expressions (regex). This guide is designed with students in mind, offering practical examples for learning and mastering regex in Linux.

---

# Regular Expressions in Linux

## Overview
Regular expressions (regex) are powerful tools for matching patterns in text. They are widely used in Linux commands like `grep`, `sed`, and `awk` to search, filter, and manipulate text. Regex provides precise control to find, replace, and analyze strings in files.

---

## Preparing a Test File
Before using regex, let's create a sample file to test our commands. Open a terminal and create a file named `file.txt`:

```bash
echo -e "Hello World\nLinux is amazing\nHat\nHit\nHot\nGoodbye world" > file.txt
```

This file will contain the following text:

```
Hello World
Linux is amazing
Hat
Hit
Hot
Goodbye world
```

We'll use this file for all the examples below.

---

## Key Regex Syntax and Examples

| Symbol   | Meaning                                | Example         | Matches                                   |
| -------- | -------------------------------------- | --------------- | ----------------------------------------- |
| `^`      | Start of line                          | `^Hello`        | Lines starting with "Hello"             |
| `$`      | End of line                            | `world$`        | Lines ending with "world"               |
| `.`      | Any single character                   | `h.t`           | `Hat`, `Hit`, `Hot`                      |
| `[abc]`  | Any character in brackets              | `[abc]`         | Lines containing `a`, `b`, or `c`        |
| `[^abc]` | Any character not in brackets          | `[^abc]`        | Lines without `a`, `b`, or `c`           |
| `*`      | Zero or more of the previous character | `go*`           | Matches `g`, `go`, `goo`                 |
| `+`      | One or more of the previous character  | `go+`           | Matches `go`, `goo`                      |
| `?`      | Zero or one of the previous character  | `colou?r`       | Matches `color`, `colour`                |
| `{n}`    | Exactly `n` occurrences                | `a{3}`          | Matches `aaa`                            |
| `{n,}`   | `n` or more occurrences                | `a{2,}`         | Matches `aa`, `aaa`, etc.                |
| `{n,m}`  | Between `n` and `m` occurrences        | `a{2,4}`        | Matches `aa`, `aaa`, `aaaa`              |

---

## Using `grep` with Regex

`grep` is a Linux command for searching text using patterns, including regex. Below are practical examples using `file.txt`.

### Examples

1. **Search for lines starting with a word**:
   ```bash
   grep "^Hello" file.txt
   ```
   **Output**:
   ```
   Hello World
   ```

2. **Search for lines ending with a word**:
   ```bash
   grep "world$" file.txt
   ```
   **Output**:
   ```
   Hello World
   Goodbye world
   ```

3. **Match any three-character word starting with `h` and ending with `t`**:
   ```bash
   grep "h.t" file.txt
   ```
   **Output**:
   ```
   Hat
   Hit
   Hot
   ```

4. **Exclude lines containing specific characters**:
   ```bash
   grep -v "Hot" file.txt
   ```
   **Output**:
   ```
   Hello World
   Linux is amazing
   Hat
   Hit
   Goodbye world
   ```

5. **Count matching lines**:
   ```bash
   grep -c "world" file.txt
   ```
   **Output**:
   ```
   2
   ```

6. **Show line numbers with matches**:
   ```bash
   grep -n "Hello" file.txt
   ```
   **Output**:
   ```
   1:Hello World
   ```

7. **Search for patterns with specific ranges**:
   ```bash
   grep "[a-z]ing" file.txt
   ```
   **Output**:
   ```
   Linux is amazing
   ```

8. **Search for words with repeated characters**:
   ```bash
   grep "o*" file.txt
   ```
   **Output**:
   ```
   Hello World
   Linux is amazing
   Goodbye world
   ```

9. **Match words with escape characters**:
   ```bash
   grep "\." file.txt
   ```
   **Explanation**: This matches any line containing a literal `.` character.

---

## Additional Tips

- Use `grep -i` for case-insensitive matching (e.g., `grep -i "hello" file.txt`).
- Use `grep -A n` to show `n` lines after a match and `-B n` to show `n` lines before a match (e.g., `grep -A 1 "Hello" file.txt`).
- Combine multiple patterns using `grep -E` or `grep "pattern1\|pattern2"`.

---

This updated guide provides a structured and detailed approach to learning regex with clear examples tailored for students. Let me know if further refinements are needed!

