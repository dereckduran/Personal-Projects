import segno as sg
filename  = input("Enter the name of the file you want to create:")
url = input("Enter the URL for the ColorStack PUPR site: ")
qrcode = sg.make(url)
qrcode.save(f'{filename}.png', scale = 10, light = '#104c9b')

