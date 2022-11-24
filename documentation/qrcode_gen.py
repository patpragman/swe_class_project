import qrcode
img = qrcode.make('https://github.com/patpragman/swe_class_project/blob/master/.github/workflows/push_to_dev.yml')
img.save("yaml_link.png")