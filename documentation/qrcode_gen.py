import qrcode
img = qrcode.make('https://github.com/patpragman/swe_class_project/blob/master/documentation/systems.md')
type(img)  # qrcode.image.pil.PilImage
img.save("systems_qr_link.png")