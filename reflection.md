# Reflection Questions

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest fixes were stylistic — such as renaming functions to follow `snake_case`, adding docstrings, and breaking long lines. These required only simple edits and didn’t affect program behavior.  
The hardest issues were the mutable default argument (`logs=[]`) and global variable handling. They required understanding of Python’s function memory model and ensuring that behavior remained consistent after refactoring.

---

### 2. Did the static analysis tools report any false positives? If so, describe one example.

Yes. Pylint reported the use of a “global statement” (`W0603`) as a warning. In this small, single-file script, the global variable was intentional to persist inventory state. While it’s generally bad practice, it wasn’t an actual bug for this context, making it a mild false positive.

---

### 3. How would you integrate static analysis tools into your actual software development workflow?

I would integrate **Flake8**, **Bandit**, and **Pylint** into a **Continuous Integration (CI)** pipeline using GitHub Actions.  
This ensures every commit is automatically scanned for style, security, and quality issues.  
Locally, I’d run `flake8` and `pylint` before committing, and set up pre-commit hooks to block commits that fail analysis.

---

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

After applying fixes:
- The code became **cleaner and more readable** due to consistent naming and docstrings.  
- The removal of `eval()` improved **security**.  
- Specific exception handling made error behavior **more predictable**.  
- Encoding specification and input validation improved **robustness** for file I/O and user data.  

Overall, the code evolved from a quick script into a more maintainable, production-ready module.

---