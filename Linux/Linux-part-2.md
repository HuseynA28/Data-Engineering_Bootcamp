Wellcome to linux part to in this part we look at more advanced linux funtions and command 
## Regular Expressions in Linux

Regular expressions (regex) are powerful tools for matching patterns in text. They are commonly used in Linux commands like `grep`, `sed`, and `awk` to search, filter, and manipulate text.

---

## Key Regex Syntax and Examples

| Symbol  | Meaning                                  | Example            | Matches                       |
|---------|------------------------------------------|--------------------|-------------------------------|
| `^`     | Start of line                           | `^Hello`           | Lines starting with "Hello"  |
| `$`     | End of line                             | `world$`           | Lines ending with "world"    |
| `.`     | Any single character                    | `h.t`              | `hat`, `hit`, `hot`, etc.     |
| `[abc]` | Any character in brackets               | `[abc]`            | `a`, `b`, or `c`             |
| `[^abc]`| Any character not in brackets           | `[^abc]`           | Any except `a`, `b`, `c`     |
| `*`     | Zero or more of the previous character  | `go*`              | `g`, `go`, `goo`, etc.       |
| `+`     | One or more of the previous character   | `go+`              | `go`, `goo`, etc.            |
| `?`     | Zero or one of the previous character   | `colou?r`          | `color`, `colour`            |
| `{n}`   | Exactly `n` occurrences                | `a{3}`             | `aaa`                        |
| `{n,}`  | `n` or more occurrences                | `a{2,}`            | `aa`, `aaa`, etc.            |
| `{n,m}` | Between `n` and `m` occurrences        | `a{2,4}`           | `aa`, `aaa`, `aaaa`          |

---

## Using `grep` with Regex

`grep` is a Linux command for searching text using patterns, including regex.

### Examples

1. **Search for lines starting with a word**:
   ```bash
   grep "^Hello" file.txt
   ```
   Matches lines starting with "Hello".

2. **Search for lines ending with a word**:
   ```bash
   grep "world$" file.txt
   ```
   Matches lines ending with "world".

3. **Match any three-character word starting with `h` and ending with `t`**:
   ```bash
   grep "h.t" file.txt
   ```
   Matches `hat`, `hit`, `hot`, etc.

4. **Match lines containing a specific range of characters**:
   ```bash
   grep "[a-c]" file.txt
   ```
   Matches lines with `a`, `b`, or `c`.

5. **Exclude lines containing specific characters**:
   ```bash
   grep "[^abc]" file.txt
   ```
   Matches lines without `a`, `b`, or `c`.

6. **Match lines with repeated patterns**:
   ```bash
   grep "go*" file.txt
   ```
   Matches `g`, `go`, `goo`, etc.

---

## Quick Tips
- Use `grep -i` for case-insensitive matching.
- Add `-n` to display line numbers with matches.
- Combine `grep` with other commands using pipes for advanced workflows.

