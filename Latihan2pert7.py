# Modal awal
modal = 100000000  # 100 juta
total_laba = 0

# Hitung laba bulanan
for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
        laba = 0
    elif bulan == 3 or bulan == 4:
        laba = modal * 0.01
    elif bulan == 5 or bulan == 6 or bulan == 7:
        laba = modal * 0.05
    elif bulan == 8:
        laba = modal * 0.02
    else:
        laba = 0
    
    print(f"Laba bulan ke-{bulan} sebesar: {laba}")
    total_laba += laba

print(f"Total laba adalah: {total_laba}")
