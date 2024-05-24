import qrcode
import os
import re

# Takes user input
url = input("Enter url here: ")

def make_qr_code():
    # Makes the qr code and stores it into a variable
    img = qrcode.make(url)

    # Saves the image with name of the url
    img.save('./qr_codes/{}.png'.format(url))

    # Saves the url's qr code in a database
    with open('database.txt', 'a') as file:
        file.write(url + '\n')

# Opens the database.txt to check if the entered url already has a qr code to make script more efficient
with open('database.txt', 'r') as file:
    content = file.read()

if re.search(r'\b{}\b'.format(url), content):
    print(f"The QR code for '{url}' already exist.")
else:
    make_qr_code()