import qrcode

# data to encoding in QRCode
data = "https://nezirmahamat-ethicfashion-my-app-ismuri.streamlit.app/"


# QRCode object
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)


qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("fast_fashion.png")
