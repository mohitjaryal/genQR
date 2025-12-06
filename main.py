# Generate QR using python

import qrcode

# Take input
url = input('Enter text or URL: ').strip()

# Output file path
file_path = 'qrcode.png'

# Create QR code object
qr = qrcode.QRCode()

# Add data to QR code
qr.add_data(url)
qr.make(fit=True)

# Generate image
img = qr.make_image(fill_color="black", back_color="white")

# Save image
img.save(file_path)

print('✅ QR Code generated and saved as', file_path)
