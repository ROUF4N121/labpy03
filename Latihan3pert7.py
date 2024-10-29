# Saldo awal
saldo = 1000000  # Rp 1.000.000

# Loop menu ATM
while True:
    print(f"\nSaldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == "1":
        jumlah = int(input("Masukkan jumlah penarikan: "))
        
        if jumlah > saldo:
            print("Saldo tidak mencukupi!")
        else:
            saldo -= jumlah
            print("Penarikan berhasil!")
            
    elif pilihan == "2":
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid, silakan pilih lagi.")
    