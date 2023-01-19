import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
error_correction= qrcode.constants.ERROR_CORRECT_H,
box_size=10,
border=10,)
qr.add_data("https://www.youtube.com/watch?v=LVx5m8HMOy4&list=PLgirwYDDPtS2f6nOY3jtenaLI3gUrvqoI")
qr.make(fit = True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("abdul_hamid_urdu_qr.png")