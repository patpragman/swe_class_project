import qrcode

url = "https://hackaday.com/2019/03/05/good-code-documents-itself-and-other-hilarious-jokes-you-shouldnt-tell-yourself/"
img = qrcode.make(url)
img.save("self_documenting_link.png")