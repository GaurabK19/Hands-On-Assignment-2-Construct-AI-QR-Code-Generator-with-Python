"""
qr_generator.py

Generates a QR code image from a user-provided URL.
The QR code is displayed using PIL (Pillow) and saved as a PNG file.

Assignment: Biox Systems - QR Code Generator
            University of the Cumberlands
Author:     Gaurab

Dependencies:
    pip install qrcode[pil]
"""

import qrcode
from PIL import Image


def get_url_from_user():
    """Prompt the user for a URL and return it after basic validation."""
    url = input("Enter the URL to encode as a QR code: ").strip()
    if not url:
        raise ValueError("URL cannot be empty. Please provide a valid URL.")
    return url


def generate_qr_code(url):
    """Generate and return a QR code PIL Image for the given URL."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% error correction
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")


def save_qr_code(qr_image, filename="qr_code_output.png"):
    """Save the QR code image to a file."""
    qr_image.save(filename)
    print(f"QR code saved as '{filename}'.")


def display_qr_code(qr_image):
    """Display the QR code image using the default image viewer."""
    qr_image.show()
    print("QR code displayed. Close the image window to exit.")


def main():
    """Main entry point for the QR code generator application."""
    print("=" * 50)
    print("       Biox Systems - QR Code Generator")
    print("=" * 50)

    try:
        url = get_url_from_user()
        print(f"\nGenerating QR code for: {url}")
        qr_image = generate_qr_code(url)
        save_qr_code(qr_image)
        display_qr_code(qr_image)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")


if __name__ == "__main__":
    main()