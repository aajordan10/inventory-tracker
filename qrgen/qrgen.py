import qrcode

def generate_qr_code():
    # Prompt user for data to encode
    data = input("Enter the data or URL to encode in the QR code: ")
    if not data.strip():
        print("Error: Data cannot be empty!")
        return

    # Prompt user for customization options
    print("\n--- QR Code Customization Options ---")
    error_levels = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H,
    }
    error_correction = input("Choose error correction level (L, M, Q, H; default is M): ").upper()
    error_correction = error_levels.get(error_correction, qrcode.constants.ERROR_CORRECT_M)

    try:
        box_size = int(input("Enter the box size (default is 10): ") or 10)
        border = int(input("Enter the border size (default is 4): ") or 4)
    except ValueError:
        print("Error: Box size and border must be integers!")
        return

    fill_color = input("Enter the fill color (default is black): ") or "black"
    back_color = input("Enter the background color (default is white): ") or "white"

    # Create a QR code object with the user's settings
    qr = qrcode.QRCode(version=1, error_correction=error_correction, box_size=box_size, border=border)
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Save the image
    filename = input("Enter the filename to save the QR code (default is 'qr_code.png'): ") or "qr_code.png"
    img.save(filename)
    print(f"QR code saved as {filename}!")

# Run the function
generate_qr_code()
