# PRODIGY_CS_01

## Description

This Python program implements the Caesar Cipher algorithm, a simple and classic encryption technique where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

The program allows the user to:

- Encrypt a text message using a chosen shift value.

- Decrypt a text message using the same shift value.

It supports both uppercase and lowercase letters, and leaves non-alphabetic characters unchanged.
---
## Features

- Encrypt any message using a custom shift value.

- Decrypt messages with the same shift value.

- Preserves spaces, numbers, and punctuation.
---

Simple and user-friendly CLI interface.

Project Structure 
### caesar_cipher.py # Main Python program
### README.md # Project documentation

## Requirements

> - Python 3.x No external libraries are required.
---

## Usage

- Clone or download this repository.

- Open a terminal in the project folder.

- Run the program:
```bash

python3 caesar_cipher.py
```

- Enter your message and shift value when prompted.
---

## Example

Do you want to encrypt(e) or decrypt(d)?

> - Encryption

- Enter your message: Hello World
- Enter the number of shift you want: 3
- Your message after encryption: Khoor Zruog

> - Decryption

- Enter your message: Khoor Zruog
- Enter the number of shift you want: 3 
- Your message after decryption: Hello World
---

## Algorithm Overview

The Caesar Cipher works by shifting each letter in the message by a fixed number of positions:

For encryption: (letter_position + shift) % 26

For decryption: (letter_position - shift) % 26
---

## Limitations

- Only works with letters from the English alphabet.

- Not secure for modern cryptographic purposes.
---

## Author

Developed by **DIAWARA Nana** as a simple Python cryptography project with prodigy infotech.
