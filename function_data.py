from tabulate import tabulate
import json

# Data siswa menggunakan dictionary dalam dictionary
data_siswa = {
    '2007111111': {'nama': 'Rony', 'kelas': 11, 'tahun_masuk': 2022, 'matematika': 75, 'indonesia': 90, 'fisika': 77, 'kimia': 80, 'biologi': 85},
    '2007111112': {'nama': 'Siti', 'kelas': 11, 'tahun_masuk': 2022, 'matematika': 70, 'indonesia': 80, 'fisika': 70, 'kimia': 81, 'biologi': 90},
    '2007111113': {'nama': 'Budi', 'kelas': 11, 'tahun_masuk': 2022, 'matematika': 70, 'indonesia': 70, 'fisika': 70, 'kimia': 70, 'biologi': 70},
    '2007111114': {'nama': 'Sekar', 'kelas': 11, 'tahun_masuk': 2022, 'matematika': 79, 'indonesia': 86, 'fisika': 80, 'kimia': 85, 'biologi': 82},
    '2007111115': {'nama': 'Alif', 'kelas': 11, 'tahun_masuk': 2022, 'matematika': 85, 'indonesia': 92, 'fisika': 89, 'kimia': 80, 'biologi': 85}
}

#-----------------Fungsi untuk Guru-------------------
# Fungsi untuk menampilkan data siswa dalam bentuk tabel
def lihat_data_siswa(data_siswa):
    # Menampilkan data siswa tanpa filter terlebih dahulu
    print("\n----------------------------------Data Nilai Siswa--------------------------------------")
    data_siswa_list = [{'NIS': nis,
                        'Nama': info['nama'],
                        'Kelas': info['kelas'],
                        'Tahun Masuk': info['tahun_masuk'],
                        'Matematika': info['matematika'],
                        'Indonesia': info['indonesia'],
                        'Fisika': info['fisika'],
                        'Kimia': info['kimia'],
                        'Biologi': info['biologi']}
                       for nis, info in data_siswa.items()]
    print(tabulate(data_siswa_list, headers="keys", tablefmt="pretty"))

    # Meminta input dari pengguna apakah ingin menggunakan filter atau tidak
    apply_filter = input("Apakah Anda ingin menggunakan filter? (y/n): ").strip().lower()

    # Jika pengguna ingin menggunakan filter
    if apply_filter == 'y':
        # Menampilkan daftar kolom yang bisa dipilih untuk filter
        print("\nPilihan Kolom untuk Filter:")
        pilihan_kolom = ['Kelas', 'Tahun Masuk', 'Matematika', 'Indonesia', 'Fisika', 'Kimia', 'Biologi']
        for i, kolom in enumerate(pilihan_kolom, 1):
            print(f"{i}. {kolom}")

        # Meminta pengguna untuk memilih kolom untuk filter
        try:
            index_pilihan = int(input("Masukkan nomor kolom yang ingin difilter: ")) - 1
            filter_option = pilihan_kolom[index_pilihan]
        except (IndexError, ValueError):
            print("Pilihan tidak valid. Menampilkan data tanpa filter.")
            print(tabulate(data_siswa_list, headers="keys", tablefmt="pretty"))
            return

        # Meminta nilai untuk filter berdasarkan pilihan kolom yang dipilih
        filter_value = input(f"Masukkan nilai untuk filter {filter_option}: ").title().strip()

        # Melakukan filter jika filter_option dan filter_value ada
        if filter_value:
            try:
                filter_value = int(filter_value)
                data_siswa_list = [info for info in data_siswa_list if info[filter_option] == filter_value]
                # Menampilkan data setelah difilter
                print(f"\nData Siswa Setelah Filter Berdasarkan Kolom '{filter_option}' dengan Nilai {filter_value}:")
                print(tabulate(data_siswa_list, headers="keys", tablefmt="pretty"))
                
                # Meminta input dari pengguna apakah ingin mengurutkan data setelah filter atau tidak
                apply_sort = input("Apakah Anda ingin mengurutkan data ini? (1: ascending / 2: descending / 3: tidak): ").strip()
                
                # Jika pengguna memilih untuk mengurutkan data
                if apply_sort == '1' or apply_sort == '2':
                    # Menampilkan daftar kolom yang bisa dipilih untuk sorting
                    print("\nPilihan Kolom untuk Sorting:")
                    pilihan_kolom = ['Nama', 'Kelas', 'Tahun Masuk', 'Matematika', 'Indonesia', 'Fisika', 'Kimia', 'Biologi']
                    for i, kolom in enumerate(pilihan_kolom, 1):
                        print(f"{i}. {kolom}")

                    # Meminta pengguna untuk memilih kolom untuk sorting
                    try:
                        index_pilihan = int(input("Masukkan nomor kolom yang ingin diurutkan: ")) - 1
                        sort_option = pilihan_kolom[index_pilihan]
                    except (IndexError, ValueError):
                        print("Pilihan tidak valid. Menampilkan data tanpa sorting.")
                        return

                    # Mengurutkan data secara ascending atau descending
                    if apply_sort == '1':
                        data_siswa_list.sort(key=lambda x: x[sort_option])
                        sort_direction = "Ascending"
                    elif apply_sort == '2':
                        data_siswa_list.sort(key=lambda x: x[sort_option], reverse=True)
                        sort_direction = "Descending"

                    # Menampilkan data setelah diurutkan
                    print(f"\nData Siswa Setelah Diurutkan {sort_direction} Berdasarkan Kolom '{sort_option}':")
                    print(tabulate(data_siswa_list, headers="keys", tablefmt="pretty"))
                
                elif apply_sort == '3':
                    print("Tidak melakukan pengurutan. Menampilkan data tanpa pengurutan.")
                    print(tabulate(data_siswa_list, headers="keys", tablefmt="pretty"))
                else:
                    print("Pilihan pengurutan tidak valid. Menampilkan data tanpa pengurutan.")
                    print(tabulate(data_siswa_list, headers="keys", tablefmt="pretty"))

            except ValueError:
                print("Input harus berupa angka untuk kolom numerik seperti 'Matematika', 'Indonesia', dsb.")
        else:
            print("Nilai filter tidak boleh kosong.")
            
    elif apply_filter != 'n':
        print("Pilihan tidak valid. Menampilkan data tanpa filter.")
        print(tabulate(data_siswa_list, headers="keys", tablefmt="pretty"))
    # Jika pengguna tidak ingin menggunakan filter
    else:
        # Meminta input dari pengguna apakah ingin mengurutkan data atau tidak
        apply_sort = input("Apakah Anda ingin mengurutkan data ini? (1: ascending / 2: descending / 3: tidak): ").strip()

        # Jika pengguna memilih untuk mengurutkan data
        if apply_sort == '1' or apply_sort == '2':
            # Menampilkan daftar kolom yang bisa dipilih untuk sorting
            print("\nPilihan Kolom untuk Sorting:")
            pilihan_kolom = ['Nama', 'Kelas', 'Tahun Masuk', 'Matematika', 'Indonesia', 'Fisika', 'Kimia', 'Biologi']
            for i, kolom in enumerate(pilihan_kolom, 1):
                print(f"{i}. {kolom}")

            # Meminta pengguna untuk memilih kolom untuk sorting
            try:
                index_pilihan = int(input("Masukkan nomor kolom yang ingin diurutkan: ")) - 1
                sort_option = pilihan_kolom[index_pilihan]
            except (IndexError, ValueError):
                print("Pilihan tidak valid. Menampilkan data tanpa sorting.")
                return

            # Mengurutkan data secara ascending atau descending
            if apply_sort == '1':
                data_siswa_list.sort(key=lambda x: x[sort_option])
                sort_direction = "Ascending"
            elif apply_sort == '2':
                data_siswa_list.sort(key=lambda x: x[sort_option], reverse=True)
                sort_direction = "Descending"

            # Menampilkan data setelah diurutkan
            print(f"\nData Siswa Setelah Diurutkan {sort_direction} Berdasarkan Kolom '{sort_option}':")
            print(tabulate(data_siswa_list, headers="keys", tablefmt="pretty"))
        
        elif apply_sort == '3':
            print("Tidak melakukan pengurutan. Menampilkan data tanpa pengurutan.")
            print(tabulate(data_siswa_list, headers="keys", tablefmt="pretty"))
        else:
            print("Pilihan pengurutan tidak valid. Menampilkan data tanpa pengurutan.")
            print(tabulate(data_siswa_list, headers="keys", tablefmt="pretty"))

# Fungsi validasi untuk angka
def validasi_angka(prompt, min_value=None, max_value=None):
    while True:
        nilai = input(prompt)
        if nilai.isdigit():
            nilai = int(nilai)
            if (min_value is None or nilai >= min_value) and (max_value is None or nilai <= max_value):
                return nilai
        print(f"Input harus berupa angka{' antara ' + str(min_value) + ' dan ' + str(max_value) if min_value is not None and max_value is not None else ''}. Coba lagi.")

# Fungsi validasi untuk nama (hanya huruf dan spasi)
def validasi_nama(prompt):
    while True:
        nama = input(prompt).strip()
        if nama.replace(" ", "").isalpha():
            return nama
        print("Nama hanya boleh mengandung huruf dan spasi.")

# Fungsi untuk menambah data siswa
def tambah_data_siswa(data_siswa):
    max_nis = max(int(nis) for nis in data_siswa.keys()) if data_siswa else 2007000000
    nis_baru = str(max_nis + 1)
    nama = validasi_nama("\nMasukkan nama siswa: ").title().strip()
    kelas = validasi_angka("Masukkan kelas siswa (10/11/12): ", 10, 12)
    tahun_masuk = validasi_angka("Masukkan tahun masuk siswa: ", 2000, 2024)
    matematika = validasi_angka("Masukkan nilai Matematika: ", 0, 100)
    indonesia = validasi_angka("Masukkan nilai Indonesia: ", 0, 100)
    fisika = validasi_angka("Masukkan nilai Fisika: ", 0, 100)
    kimia = validasi_angka("Masukkan nilai Kimia: ", 0, 100)
    biologi = validasi_angka("Masukkan nilai Biologi: ", 0, 100)
    
    data_siswa[nis_baru] = {
        'nama': nama,
        'kelas': kelas,
        'tahun_masuk': tahun_masuk,
        'matematika': matematika,
        'indonesia': indonesia,
        'fisika': fisika,
        'kimia': kimia,
        'biologi': biologi
    }
    print("\nData siswa berhasil ditambahkan!")

# Fungsi untuk memperbarui data siswa
def update_data_siswa(data_siswa):
    while True:
        nis = input("Masukkan NIS Siswa yang akan diupdate: ").strip()
        if nis in data_siswa:
            print(f"\nData saat ini untuk siswa dengan NIS {nis}:")
            print(tabulate([data_siswa[nis]], headers="keys", tablefmt="pretty"))
            
            print("\nPilih kolom yang akan diupdate:")
            print("1. Nama")
            print("2. Kelas")
            print("3. Tahun Masuk")
            print("4. Nilai Matematika")
            print("5. Nilai Indonesia")
            print("6. Nilai Fisika")
            print("7. Nilai Kimia")
            print("8. Nilai Biologi")
            print("9. Keluar")

            pilihan = input("\nMasukkan nomor kolom yang akan diupdate: ").strip()
            
            if pilihan == '1':
                data_siswa[nis]['nama'] = validasi_nama("Masukkan Nama Siswa baru: ").title()
            elif pilihan == '2':
                data_siswa[nis]['kelas'] = validasi_angka("Masukkan Kelas Siswa baru (10-12): ", 10, 12)
            elif pilihan == '3':
                data_siswa[nis]['tahun_masuk'] = validasi_angka("Masukkan Tahun Masuk Siswa baru: ")
            elif pilihan == '4':
                data_siswa[nis]['matematika'] = validasi_angka("Masukkan Nilai Matematika Siswa baru (0-100): ", 0, 100)
            elif pilihan == '5':
                data_siswa[nis]['indonesia'] = validasi_angka("Masukkan Nilai Indonesia Siswa baru (0-100): ", 0, 100)
            elif pilihan == '6':
                data_siswa[nis]['fisika'] = validasi_angka("Masukkan Nilai Fisika Siswa baru (0-100): ", 0, 100)
            elif pilihan == '7':
                data_siswa[nis]['kimia'] = validasi_angka("Masukkan Nilai Kimia Siswa baru (0-100): ", 0, 100)
            elif pilihan == '8':
                data_siswa[nis]['biologi'] = validasi_angka("Masukkan Nilai Biologi Siswa baru (0-100): ", 0, 100)
            elif pilihan == '9':
                print("Tidak ada perubahan yang dilakukan.")
                return
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                return
            
            print("\nData siswa berhasil diperbarui.")
            break
        else:
            print("NIS tidak ditemukan.")
        
# Fungsi untuk menghapus data siswa
def hapus_data_siswa(data_siswa):
    while True:
        nis = input("Masukkan NIS siswa yang ingin dihapus: ").strip()
        if nis.isdigit():
            if nis in data_siswa:
                del data_siswa[nis]
                print("\nData siswa berhasil dihapus!")
            else:
                print("NIS tidak ditemukan.")
            break
        else:
            print("NIS harus berupa angka. Silakan coba lagi.")

# Fungsi untuk melakukan backup data siswa ke file JSON
def backup_data_siswa(data_siswa, filename="backup_data_siswa.json"):
    with open(filename, 'w') as backup_file:
        json.dump(data_siswa, backup_file, indent=4)
    print(f"\nData siswa berhasil dibackup ke file {filename}!")

# Fungsi untuk melihat rekap data siswa
def statistik_nilai_siswa(data_siswa):
    mata_pelajaran = ['matematika', 'indonesia', 'fisika', 'kimia', 'biologi']
    print("\nStatistik Nilai Siswa")
    for pelajaran in mata_pelajaran:
        nilai_siswa = [data[pelajaran] for data in data_siswa.values()]
        nilai_tertinggi = max(nilai_siswa)
        nilai_terendah = min(nilai_siswa)
        rata_rata = sum(nilai_siswa) / len(nilai_siswa)
        print(f"\nMata Pelajaran: {pelajaran.capitalize()}")
        print(f"Nilai Tertinggi: {nilai_tertinggi}")
        print(f"Nilai Terendah: {nilai_terendah}")
        print(f"Rata-rata Nilai: {rata_rata:.2f}")

#-----------------Fungsi untuk Siswa-------------------
# Fungsi untuk melihat data siswa berdasarkan NIS
def lihat_data_siswa_saya(data_siswa, nis_siswa):
    if nis_siswa in data_siswa:
        data_siswa_saya = data_siswa[nis_siswa]
        print("\n----------------------------------Data Nilai Saya--------------------------------------")
        print(tabulate([data_siswa_saya], headers="keys", tablefmt="pretty"))
    else:
        print("NIS tidak ditemukan dalam database.")

# Fungsi untuk menghitung statistik nilai siswa berdasarkan NIS
def hitung_statistik_nilai_siswa(data_siswa, nis_siswa):
    if nis_siswa in data_siswa:
        data_siswa_saya = data_siswa[nis_siswa]
        nilai_matematika = data_siswa_saya['matematika']
        nilai_indonesia = data_siswa_saya['indonesia']
        nilai_fisika = data_siswa_saya['fisika']
        nilai_kimia = data_siswa_saya['kimia']
        nilai_biologi = data_siswa_saya['biologi']
        
        # Hitung statistik nilai
        nilai_tertinggi = max(nilai_matematika, nilai_indonesia, nilai_fisika, nilai_kimia, nilai_biologi)
        nilai_terendah = min(nilai_matematika, nilai_indonesia, nilai_fisika, nilai_kimia, nilai_biologi)
        rata_rata = (nilai_matematika + nilai_indonesia + nilai_fisika + nilai_kimia + nilai_biologi) / 5
        
        # Menampilkan statistik nilai
        print("\n----------------------------------Rekap Nilai Saya--------------------------------------")
        print(f"Nilai Tertinggi   : {nilai_tertinggi}")
        print(f"Nilai Terendah    : {nilai_terendah}")
        print(f"Rata-rata Nilai   : {rata_rata:.2f}")
        if rata_rata >= 80:
            print("\nSelamat nilai rata-rata anda diatas KKM, anda LULUS!")
        else:
            print("\nMohon maaf nilai anda kurang dari 80, anda BELUM LULUS. Silahkan hubungi guru anda untuk remedial.")
    else:
        print("NIS tidak ditemukan dalam database.")
