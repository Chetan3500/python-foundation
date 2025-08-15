# 📜 Python `re` Regex Cheatsheet

## 1️⃣ Matching Functions
| Function          | Description |
|-------------------|-------------|
| `re.match()`      | Match **only at start** of string |
| `re.search()`     | Match **first occurrence anywhere** |
| `re.findall()`    | Return all non-overlapping matches as a list |
| `re.finditer()`   | Return all matches as an iterator of `Match` objects |
| `re.fullmatch()`  | Match **entire** string |
| `re.sub()`        | Replace pattern |
| `re.split()`      | Split by pattern |

---

## 2️⃣ Special Characters
| Char | Meaning | Example |
|------|---------|---------|
| `.`  | Any char except `\n` (dotall mode changes this) | `a.b` → `"acb"` matches |
| `^`  | Start of string (or line in `MULTILINE`) | `^Hello` |
| `$`  | End of string (or line in `MULTILINE`) | `world$` |
| `\`  | Escape special char | `\.` matches `"."` |

---

## 3️⃣ Character Classes
| Pattern | Matches |
|---------|---------|
| `[abc]` | a, b, or c |
| `[^abc]` | NOT a, b, or c |
| `[a-z]` | Lowercase letters a–z |
| `[0-9]` | Digits 0–9 |
| `\d` | Digit (0–9) |
| `\D` | Non-digit |
| `\w` | Word char (letters, digits, `_`) |
| `\W` | Non-word char |
| `\s` | Whitespace (space, tab, newline) |
| `\S` | Non-whitespace |

---

## 4️⃣ Quantifiers
| Pattern | Meaning |
|---------|---------|
| `*`     | 0 or more |
| `+`     | 1 or more |
| `?`     | 0 or 1 |
| `{n}`   | Exactly n |
| `{n,}`  | At least n |
| `{,m}`  | Up to m |
| `{n,m}` | Between n and m |

**Greedy vs Lazy**:  
- `.*` → greedy (as much as possible)  
- `.*?` → lazy (as little as possible)  

---

## 5️⃣ Grouping & Capturing
| Syntax | Meaning |
|--------|---------|
| `(abc)` | Capturing group |
| `(?:abc)` | Non-capturing group |
| `(?P<name>abc)` | Named capturing group |
| `(?P=name)` | Backreference to named group |
| `\1`, `\2` | Backreference to group number |

---

## 6️⃣ Alternation
| Pattern | Meaning |
|---------|---------|
| `a|b`   | Matches a **or** b |

---

## 7️⃣ Lookarounds
| Pattern | Meaning |
|---------|---------|
| `(?=...)` | Positive lookahead |
| `(?!...)` | Negative lookahead |
| `(?<=...)` | Positive lookbehind |
| `(?<!...)` | Negative lookbehind |

---

## 8️⃣ Flags
| Flag | Inline | Meaning |
|------|--------|---------|
| `re.I` | `(?i)` | Ignore case |
| `re.M` | `(?m)` | Multiline (`^`/`$` match per line) |
| `re.S` | `(?s)` | Dot matches newline |
| `re.X` | `(?x)` | Verbose mode (ignore whitespace, allow comments) |
| `re.A` | `(?a)` | ASCII-only `\w`, `\d`, etc. |

---

## 9️⃣ Tips
- **Escape special chars** with `\` if you want them literal.  
- Use **non-capturing groups** when you don’t need the matched text saved.  
- Remember: **inside repeated capturing groups, only the last match is saved**.  
- For validation + extraction, consider `fullmatch()` to ensure whole-string matches.
