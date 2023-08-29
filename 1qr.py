import qrcode

# Function to generate a QR code
def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Example usage
data_to_encode = "https://viratkohli.com"  # Replace with your data
output_filename = "virat_qr_code.png"      # Replace with your desired output filename

generate_qr_code(data_to_encode, output_filename)
print(f"QR code generated and saved as {output_filename}")
