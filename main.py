# Generate QR using python

import qrcode

# Take input
url = input('Enter text or URL: ').strip()

# Output file path
file_path = 'qrcode.png'

# Create QR code object
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code (1–40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # how much error correction
    box_size=10,  # size of each box
    border=4,  # width of border (minimum 4)
)

# Add data to QR code
qr.add_data(url)
qr.make(fit=True)

# Generate image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save(file_path)

print('✅ QR Code generated and saved as', file_path)
