# import qrcode
# from PIL import Image
# qr=qrcode.QRcode(
#     version=1,
#     error_correction=qrcode.ERROR_CORRECT_H,
#     box_size=10,
#     border=4,
#                  )
# qr.add_data("https://www.tiktok.com/@essa.khan636")
# qr.make (fit=True)
# img=qr.make_image(fill_color="red",back_color="blue")
# img.save("essakhan_tiktok.png")


import qrcode

# # Create instance of QRCode
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )

# # Add data to the QR code
# qr.add_data('Your data here')
# qr.make(fit=True)

# # Create an image object from the QRCode instance
# img = qr.make_image(fill='black', back_color='white')

# # Save the image to a file
# img.save('your_qrcode.png')


import qrcode
from PIL import Image

# Create an instance of QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

# Add data to the QR code
qr.add_data("https://www.tiktok.com/@essa.khan636")
qr.make(fit=True)

# Create an image object from the QRCode instance
img = qr.make_image(fill_color="red", back_color="white")

# Save the image to a file
img.save("essakhan_tiktok.png")
