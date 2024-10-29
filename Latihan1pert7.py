from random import random

# Memaskkan jumlah angka yang mau dihasilkan
n = int(input("Masukkan nilai n: "))

# Menampilkan n bilangan acak yang lebih besar dari 0.5
print("Bilangan acak lebih besar dari 0.5:")
count = 1
while count <= n:
    number = random()
    if number > 0.5:
        print(f"Data ke-{count} => {number}")
        count += 1

print("Selesai")
