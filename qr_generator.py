"""
qr_code_generator.py

Description:
    Generates a QR code image from a user-provided URL address.
    The QR code is displayed using PIL (Pillow) and saved as a PNG file.

Assignment:
    Biox Systems - QR Code Generator
    University of the Cumberlands

Author:
    Gaurab

Dependencies:
    - qrcode (pip install qrcode[pil])
    - Pillow (installed automatically with qrcode[pil])

Usage:
    Run the script and enter a URL when prompted.
    The QR code will be displayed and saved to the current directory.
"""

import qrcode
from PIL import Image


def get_url_from_user():
    """
    Prompt the user to enter a URL and return the input after basic validation.

    Returns:
        str: The URL entered by the user.
    """
    url = input("Enter the URL to encode as a QR code: ").strip()

    # Basic check to ensure the user did not leave the input blank
    if not url:
        raise ValueError("URL cannot be empty. Please provide a valid URL.")

    return url


def generate_qr_code(url):
    """
    Generate a QR code image object from the given URL.

    Args:
        url (str): The URL to encode in the QR code.

    Returns:
        PIL.Image.Image: The generated QR code as a PIL Image object.
    """
    # Configure the QR code properties
    qr = qrcode.QRCode(
        version=1,                          # Controls the size of the QR Code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (30%)
        box_size=10,                        # Size of each box (pixel) in the QR code grid
        border=4,                           # Thickness of the border (in boxes)
    )

    # Add the URL data to the QR code
    qr.add_data(url)
    qr.make(fit=True)  # Automatically determine the best version for the data

    # Create the QR code image with black fill and white background
    qr_image = qr.make_image(fill_color="black", back_color="white")

    return qr_image


def save_qr_code(qr_image, filename="qr_code_output.png"):
    """
    Save the QR code image to a file.

    Args:
        qr_image (PIL.Image.Image): The QR code image to save.
        filename (str): The name of the output file. Defaults to 'qr_code_output.png'.
    """
    qr_image.save(filename)
    print(f"QR code saved as '{filename}'.")


def display_qr_code(qr_image):
    """
    Display the QR code image using the default image viewer.

    Args:
        qr_image (PIL.Image.Image): The QR code image to display.
    """
    qr_image.show()
    print("QR code displayed. Close the image window to exit.")


def main():
    """
    Main entry point for the QR code generator application.

    Steps:
        1. Prompt the user for a URL.
        2. Generate the QR code.
        3. Save it to a PNG file.
        4. Display it using the system image viewer.
    """
    print("=" * 50)
    print("       Biox Systems - QR Code Generator")
    print("=" * 50)

    try:
        # Step 1: Get the URL from the user
        url = get_url_from_user()

        # Step 2: Generate the QR code image
        print(f"\nGenerating QR code for: {url}")
        qr_image = generate_qr_code(url)

        # Step 3: Save the QR code to disk
        save_qr_code(qr_image)

        # Step 4: Display the QR code in the image viewer
        display_qr_code(qr_image)

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")


# Run the application only when executed directly (not when imported as a module)
if __name__ == "__main__":
    main()