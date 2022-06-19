import qrcode

url = ''

img = qrcode.make(url)

img.save(url)