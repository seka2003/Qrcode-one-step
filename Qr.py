import pyqrcode

l=str(input('Enter link : '))
nim=str(input('Enter nameimage : '))

print(l)
print(nim)

image=pyqrcode.create(l)
image.svg(nim +'.svg', scale=8)





