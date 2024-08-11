import qrcode

def caesar_cipher(text, shift):
    encrypted_text = ""
    
    # Loop through each character in the text
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # Add any non-alphabetical characters as they are
        else:
            encrypted_text += char

    return encrypted_text

def generate_qr_code(data, filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10, 
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image to a file
    img.save(filename)

# User input for message and shift
message = input("Enter the message to encrypt: ")
shift = int(input("Enter the shift value (1-25): "))

# Encrypt the message using Caesar Cipher
encrypted_message = caesar_cipher(message, shift)
print("Encrypted Message:", encrypted_message)

# Generate QR code for the encrypted message
generate_qr_code(encrypted_message, "encrypted_message_qrcode.png")

print("QR code saved as 'encrypted_message_qrcode.png'")
