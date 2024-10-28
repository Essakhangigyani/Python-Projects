import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
Data= 'Hi! \n MY NAME IS ESSA KHAN'
qr.add_data(Data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save ('qr-code.png')