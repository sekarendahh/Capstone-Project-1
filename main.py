# Sekar Endah Sriwedari
# JCDSOL-015


from function_data import lihat_data_siswa, tambah_data_siswa, update_data_siswa, hapus_data_siswa, backup_data_siswa, statistik_nilai_siswa, lihat_data_siswa_saya, hitung_statistik_nilai_siswa, data_siswa

while True:
    print("\n-------------------Selamat Datang di SMA IPA!-----------------------")
    print('''\nSilakan Pilih Pengguna Anda : 
          1. Guru
          2. Siswa
          3. Keluar
          ''')
    user = input("Masukkan angka 1/2/3 : ").strip()

    if user == '1':
        while True:
            print("\n-------------------Menu Guru-----------------------")
            print("1. Lihat Data Siswa")
            print("2. Tambah Data Siswa")
            print("3. Perbarui Data Siswa")
            print("4. Hapus Data Siswa")
            print("5. Backup Data Siswa")
            print("6. Rekap Nilai Siswa")
            print("7. Kembali ke Pilihan Pengguna")
            pilihan = input("\nMasukkan pilihan Anda: ").strip()
            
            if pilihan == '1':
                lihat_data_siswa(data_siswa)
            elif pilihan == '2':
                tambah_data_siswa(data_siswa)
            elif pilihan == '3':
                update_data_siswa(data_siswa)
            elif pilihan == '4':
                hapus_data_siswa(data_siswa)
            elif pilihan == '5':
                backup_data_siswa(data_siswa)
            elif pilihan == '6':
                statistik_nilai_siswa(data_siswa)
            elif pilihan == '7':
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    elif user == '2':
        while True:
            nis_siswa = input("Masukkan NIS Anda: ").strip()
            if nis_siswa.isdigit():
                if nis_siswa in data_siswa:
                    while True:
                        nama_siswa = data_siswa[nis_siswa]['nama']
                        print(f"\nSelamat Datang {nama_siswa}! ")
                        print("\n-------------------Menu Siswa-----------------------\n")
                        print("1. Lihat Data Siswa Saya")
                        print("2. Rekap Nilai Siswa Saya")
                        print("3. Kembali ke Pilihan Pengguna")
                        pilihan_siswa = input("\nMasukkan pilihan Anda (1/2/3): ").strip()
                        
                        if pilihan_siswa == '1':
                            lihat_data_siswa_saya(data_siswa, nis_siswa)
                        elif pilihan_siswa == '2':
                            hitung_statistik_nilai_siswa(data_siswa, nis_siswa)
                        elif pilihan_siswa == '3':
                            break
                        else:
                            print("Pilihan tidak valid. Silakan coba lagi.")
                    break  # keluar dari perulangan input NIS karena NIS sudah ditemukan dan selesai
                else:
                    print("NIS tidak ditemukan. Silakan coba lagi.")
            else: 
                print("NIS harus berupa angka. Silakan coba lagi.")
                
    elif user == '3':
        print("Terima kasih! Sampai Jumpa Kembali ^_^")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
