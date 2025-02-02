import qrcode

image = qrcode.make('https://www.youtube.com/watch?v=EHi0RDZ31VA&t=4458s')
image.save('qr.png', 'PNG')