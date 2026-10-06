# Simple black and white QR code generator
import qrcode as qr

img = qr.make("https://www.example.com")
img.save("qr_basic.png")