print("=== PROGRAM BELAJAR MENABUNG ===")


target = int(input("Masukkan target tabungan: "))


tabung_per_hari = int(input("Masukkan jumlah uang yang ditabung per hari: "))


hari = 0
saldo = 0

while saldo < target:
    saldo += tabung_per_hari
    hari += 1


print("\n=== HASIL ===")
print("Target tabungan :", target)
print("Menabung per hari:", tabung_per_hari)
print("Waktu yang dibutuhkan :", hari, "hari")
print("Total saldo terkumpul :", saldo)
