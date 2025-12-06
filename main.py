# Generate QR using python

# importing library
import qrcode

url = input('Enter text or URL :').strip()

# file
file_path = 'qrcode.png'

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print('QR Code generated !'