from PIL import Image

img = Image.open("hasil_ctscan.png")
pixels = img.load()

width, height = img.size
bit_pesan = ""

for y in range(height):
    for x in range(width):
        pixel = list(pixels[x, y])
        titiknol = pixel[0]

        bits = format(titiknol, '08b')[-3:]
        bit_pesan += bits

pesan = ""
for i in range(0, len(bit_pesan), 8):
    byte = bit_pesan[i:i+8]
    if len(byte) < 8:
        break
    char = chr(int(byte, 2))
    pesan += char
    if "#EOF#" in pesan:
        break

pesan = pesan.replace("#EOF#", "")
print("Hidin mssg: ", pesan)
