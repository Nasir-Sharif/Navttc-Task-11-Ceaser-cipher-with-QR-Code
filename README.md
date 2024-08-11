# Navttc-Task-11-Ceaser-cipher-with-QR-Code

# Caesar Cipher with QR Code Generator

## Description

This Python script encrypts a message using the Caesar Cipher technique and then generates a QR code for the encrypted message. The script allows the user to input a message and a shift value, encrypts the message, and saves the resulting QR code as an image file.

## Code

```python
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
```

## Steps

1. **Import Required Modules:**
   - Import the `qrcode` library for generating QR codes.

2. **Define the `caesar_cipher` Function:**
   - This function encrypts the given text using the Caesar Cipher technique based on the provided shift value.
   - It handles both uppercase and lowercase letters, leaving non-alphabetical characters unchanged.

3. **Define the `generate_qr_code` Function:**
   - This function generates a QR code for the provided data and saves it as an image file.

4. **Get User Input:**
   - Prompt the user to input the message they want to encrypt and the shift value (1-25) for the Caesar Cipher.

5. **Encrypt the Message:**
   - Use the `caesar_cipher` function to encrypt the user's message.

6. **Generate and Save the QR Code:**
   - Use the `generate_qr_code` function to create a QR code for the encrypted message and save it as `encrypted_message_qrcode.png`.

## How to Run

1. **Ensure Python and Required Libraries are Installed:**
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
   - Install the required `qrcode` library using the following command:
     ```bash
     pip install qrcode[pil]
     ```

2. **Save the Script:**
   - Save the provided Python code into a file named `11-Ceaser cipher with qrcode(Nasir Sharif).py`.

3. **Execute the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `11-Ceaser cipher with qrcode(Nasir Sharif).py` is saved.
   - Run the script using the following command:
     ```bash
     python 11-Ceaser cipher with qrcode(Nasir Sharif).py
     ```

4. **Enter Message and Shift Value:**
   - Input the message you want to encrypt and the shift value (1-25) when prompted.

5. **View Output:**
   - The script will display the encrypted message and save the corresponding QR code as `encrypted_message_qrcode.png`.

## Example

- If you enter the message `HelloWorld` and a shift value of `3`, the script will output the encrypted message `KhoorZruog` and generate a QR code that is saved as `encrypted_message_qrcode.png`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact Nasir Sharif at   nasirsharifqasoori786@gmail.com
