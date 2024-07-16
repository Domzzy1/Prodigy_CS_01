Caesar Cipher Encryption and Decryption in Python

This repository contains a Python program that implements the Caesar Cipher algorithm for encrypting and decrypting text messages. The Caesar Cipher is a classical encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet.
Features:

    Encryption: Allows users to input a message and a shift value to encrypt the message using the Caesar Cipher.
    Decryption: Provides functionality to decrypt encrypted messages by reversing the encryption process with the same shift value.
    Interactive Interface: Utilizes an interactive command-line interface (CLI) where users can choose to encrypt or decrypt messages based on their preference.

How It Works:

    Encryption Process: Each letter in the message is shifted forward in the alphabet by the specified shift value. Non-alphabetic characters remain unchanged.
    Decryption Process: Reverses the encryption by shifting each letter backwards in the alphabet by the same shift value.

Usage:

    Clone the Repository:

    bash

    git clone https://github.com/your-username/your-repo.git
    cd your-repo

    Run the Program:
        Execute python caesar_cipher.py in your terminal.
        Follow the prompts to choose between encryption (E) or decryption (D), enter your message, and specify the shift value.

    Example:
        Encrypting "Hello World" with a shift value of 3 would result in "Khoor Zruog".
        Decrypting "Khoor Zruog" with a shift value of 3 would recover the original message "Hello World".

Contributing:

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue.
