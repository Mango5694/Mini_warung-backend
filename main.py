def tampilkan_stok():
    global stock_barang
    print("\n" + "="*30)
    print("Sistem Stock Barang Gading")
    print("="*30)
    if not stock_barang:
        print("  (Stok sedang kosong)")
    else:
        for barang in stock_barang:
            print(f"- {barang}")
    print("="*30)

def simpan_ke_hp():
    global stock_barang
    f = open("data_warung.txt", "w")
    f.write(str(stock_barang))
    f.close()
    
try:
    f_buka = open("data_warung.txt", "r")
    stock_barang = eval(f_buka.read())
    f_buka.close()
except:
    stock_barang = ["Minyak", "Beras", "Gula", "Garam"]

while True:
    print("\n--- MENU UTAMA MINI WARUNG ---")
    print("1. Lihat Stok Barang")
    print("2. Tambah Barang Baru")
    print("3. Hapus Barang Habis")
    print("4. Keluar Aplikasi")

    pilihan = input("\nPilih menu (1-4): ")

    if pilihan == "1":
        tampilkan_stok()

    elif pilihan == "2":
        while True:
        	baru = input("\nMasukkan nama barang baru(ketik `selesai' kembali):")
        	
        	if baru.lower().strip() == "selesai":
        		break
        	
        	stock_barang.append(baru)
        	simpan_ke_hp() 
        	print(f">>> Berhasil menambah {baru} ke stok!")
        	tampilkan_stok()
        	

    elif pilihan == "3":
        while True:
        	hapus = input("\nMasukkan nama barang yang ingin dihapus(ketik 'selesai' untuk kembali): ")
        	
        	if hapus.lower().strip() == "selesai":
        		break
        	try:
        		stock_barang.remove(hapus)
        		simpan_ke_hp()
        		print(f">>> Sukses! {hapus} telah dikeluarkan.")
        		tampilkan_stok()
        	except:
        		print(f">>> GAGAL: Barang '{hapus}' tidak ada di daftar!")

    elif pilihan == "4":
        print("Menutup aplikasi... Data aman tersimpan. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid! Masukkan angka 1 sampai 4 saja.")