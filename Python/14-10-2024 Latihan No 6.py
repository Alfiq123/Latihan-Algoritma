# Harga suatu barang jika diketahui TOTAL BAYAR & BANYAK BARANG-nya.

# Input
banyak_barang = int(input("Masukkan banyak barang: "))
total_bayar = int(input("Masukkan total bayar: Rp. "))

# Rumus + Output
harga_satuan = total_bayar / banyak_barang
print(f"Harga satu barang tersebut adalah: Rp. {harga_satuan:,.0f}")