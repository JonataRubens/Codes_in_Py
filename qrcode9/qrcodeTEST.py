import qrcode

img = qrcode.make('https://www.youtube.com/watch?v=YlVRSUhW1go')
img.save('testQRcode.png')