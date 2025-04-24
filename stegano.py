from PIL import Image

img = Image.open("ctscan.png")
pixels = img.load()

pesan = "Test buat tugas ncc #EOF#"
bit_pesan = ''.join(format(ord(c), '08b') for c in pesan)

lebar, tinggi = img.size
bit_index = 0

for y in range(tinggi):
    for x in range(lebar):
        if bit_index >= len(bit_pesan):
            break
        
        pixel = list(pixels[x, y])
        bits = bit_pesan[bit_index:bit_index+3].ljust(3, '0')
        pixel[0] = (pixel[0] & 0b11111000) | int(bits, 2)
        pixels[x, y] = tuple(pixel)
        bit_index += 3

img.save("hasil_ctscan.png")
print("✅ Pesan berhasil disisipkan.")
