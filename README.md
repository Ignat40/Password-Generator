# Password Generator
---
First I imported the `secrects` and `string` modules from the python library. 
```
import secrets,string
```
---

The `string` module contains functions that provide us with all the characters needed for a secure password!
* The `.ascii_letters` contains all the letters from the english alphabet both lower and uppercase
* The `.digits` is a string with all natural numbers and **0**
* The `.punctuation` function provides us with all the special characters that a strong password needs

Finally we have all the symbols we need. Let's combine them in one variable:
```
characters = letters + digits + punct
```
