def caesar_cipher(text, shift, encrypt=True):
    result = ""
    # Adjust the shift for decryption
    if not encrypt:
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                # Compute the new character for lowercase letters
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                # Compute the new character for uppercase letters
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            result += new_char
        else:
            # Non-alphabetic characters are added as is
            result += char
    return result

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (Enter 'Q' to quit): ").upper()
        if choice == 'Q':
            break
        if choice not in ['E', 'D']:
            print("Invalid choice. Please enter 'E' to encrypt, 'D' to decrypt, or 'Q' to quit.")
            continue

        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
        
        if choice == 'E':
            encrypted_message = caesar_cipher(message, shift, encrypt=True)
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message = caesar_cipher(message, shift, encrypt=False)
            print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
