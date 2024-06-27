def encrypt(shift, message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_message += chr((ord(char) - 97 + shift) % 26 + 97)
            elif char.isupper():
                encrypted_message += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(shift, message):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                decrypted_message += chr((ord(char) - 97 - shift) % 26 + 97)
            elif char.isupper():
                decrypted_message += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted_message += char
    return decrypted_message

def main():
    print("Welcome to the Caesar Cipher Program!")

    while True:
        choice = input("Do you want to encrypt (E) or decrypt (D) a message? (E/D): ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' or 'D'.")
            continue
        
        message = input("Enter your message: ")

        try:
            shift = int(input("Enter the shift value (1-25): "))
            if not 1 <= shift <= 25:
                raise ValueError("Shift value must be between 1 and 25.")
        except ValueError as ve:
            print(f"Error: {ve}")
            continue
        
        if choice == 'E':
            result_message = encrypt(shift, message)
            print(f"Encrypted message: {result_message}")
        elif choice == 'D':
            result_message = decrypt(shift, message)
            print(f"Decrypted message: {result_message}")
        
        repeat = input("Do you want to encrypt/decrypt another message? (yes/y or no/n): ").lower()
        if repeat not in ['yes', 'y']:
            break
    
    print("Thank you for using the Caesar Cipher Program!")

if __name__ == "__main__":
    main()
