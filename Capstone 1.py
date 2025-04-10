#Import tabulate untuk tabel
from tabulate import tabulate

# Data
# Data disimpang menggunakan dictionary dalam list
akun_pengguna = {
    'adinda' : '7788',
    'melati' : 'happy123',
    'dina' : '44@@'
}

# Data Review Produk
data_reviews = [
    {"nomor": 1, "username": "adinda", "produk": "Lipstick Matte", "rating": 4, "komentar": "Tahan lama dan warnanya cantik"},
    {"nomor": 2, "username": "melati", "produk": "Facial Wash", "rating": 4, "komentar": "Cocok untuk kulit kering"},
    {"nomor": 3, "username": "dina", "produk": "Glow Foundation", "rating": 3, "komentar": "Pilihan shade banyak, tapi bikin kulit kering"},
    {"nomor": 4, "username": "adinda", "produk": "Vitamin C serum", "rating": 4, "komentar": "Bisa untuk menyamarkan bekas jerawat"},
    {"nomor": 5, "username": "melati", "produk": "Glow Setting Spray", "rating": 5, "komentar": "Bikin make up tahan lama dan finishingnya dewy"}
]


def halaman_pertama():
    while True:
        print("🌸🌸 Selamat Datang di SocaBeauty!🌸🌸 \n")
        print("1. Login") #User masuk dengan username yang sudah pernah dibuat
        print("2. Buat Akun Baru") #User mendaftar username baru
        print("3. Keluar") #Keluar dari program
        menu = input("Pilih opsi (1-3): ")

        if menu == "1": #Kondisi jika user memilih menu 1
            global user
            user = login()
            if user:
                menu_utama()
        elif menu == "2":
            tambah_akun()
        elif menu == "3":
            print("👋 Keluar dari program. Sampai jumpa lagi 💐!")
            break
        else:
            print("❌ Opsi tidak tersedia. Silahkan pilih 1-3!\n")


def login():
    print("🌹🌹🌹 LOGIN 🌹🌹🌹")
    username = input("Username: ")
    password = input("Password: ")

    if username in akun_pengguna and akun_pengguna[username] == password:  #Username dan password benar, user berhasil login
        print(f"✅ Login berhasil. Selamat datang, {username} 🎀!\n")
        return username
    else:
        print("❌ Username atau password salah.\n") #User tidak berhasil login
        return


def tambah_akun():
    print("🌹🌹🌹 TAMBAH AKUN 🌹🌹🌹")
    username = input("Buat username: ")
    if username in akun_pengguna:       #Username yang dimasukkan sudah terdaftar
        print("❌ Username sudah digunakan.\n")
        return
    password = input("Buat password: ")     
    akun_pengguna[username] = password
    print(f"✅ Akun untuk '{username}' berhasil dibuat.\n")


def tampilkan_semua_reviews():
    print("\n 🎀 SocaBeauty🎀 \n ")
    headers = ["Nomor", "Username", "Produk", "Rating", "Komentar"]
    table = [[reviews['nomor'], reviews['username'], reviews['produk'], reviews['rating'], reviews['komentar']] for reviews in data_reviews]
    print(tabulate(table, headers=headers, tablefmt="double_grid", colalign=("left", "left", "left", "left")))


def tampilkan_review():
    while True:
        pilih_submenu = input('''
            1. Tampilkan Semua Data Review 
            2. Cari Data Berdasarkan Nomor
            3. Cari Data berdasarkan Username
            4. Cari Data berdasarkan Produk
            5. Menu Utama
            6. Logout
                          
            Masukkan angka Submenu yang ingin dijalankan :
            ''')
        if pilih_submenu == '1': #Kondisi jika user memilih sub menu 1 (Menampilkan Semua Data Reviews)
            if len(data_reviews)==0:
                print('Data Tidak Tersedia!')
                tampilkan_review()
            else:
                tampilkan_semua_reviews()
            tampilkan_review()

        elif pilih_submenu == '2': #Kondisi jika user memilih sub menu 2 (Menampilkan Data Tertentu berdasarkan Nomor)
            nomor_dicari = int(input('Masukkan nomor review yang ingin ditampilkan 🔎 (Masukkan Angka): '))
            
            hasil = [item for item in data_reviews if item ['nomor']== nomor_dicari]

            if hasil: 
                print ('Review Ditemukan 🎀')
                headers = ["Nomor", "Username", "Produk", "Rating", "Komentar"]
                table = [[reviews['nomor'], reviews['username'], reviews['produk'], reviews['rating'], reviews['komentar']] for reviews in hasil]
                print(tabulate(table, headers=headers, tablefmt="double_grid", colalign=("left", "left", "left", "left")))
            else:
                print('Review yang kamu cari tidak ditemukan!')
        
        elif pilih_submenu == '3': #Kondisi jika user memilih sub menu 3 (Menampilkan Data Tertentu berdasarkan Username)
            username_dicari = input('Masukkan username reviewer yang ingin ditampilkan 🔎: ')
            
            hasil = [item for item in data_reviews if item ['username'].lower()== username_dicari.lower()]

            if hasil: 
                print ('Review Ditemukan 🎀')
                headers = ["Nomor", "Username", "Produk", "Rating", "Komentar"]
                table = [[reviews['nomor'], reviews['username'], reviews['produk'], reviews['rating'], reviews['komentar']] for reviews in hasil]
                print(tabulate(table, headers=headers, tablefmt="double_grid", colalign=("left", "left", "left", "left")))
            else:
                print('Review yang kamu cari tidak ditemukan!')
            
        elif pilih_submenu == '4': #Kondisi jika user memilih sub menu 4 (Menampilkan Data Tertentu berdasarkan Produk)
            produk_dicari = input('Masukkan produk yang ingin ditampilkan 🔎: ')
            
            hasil = [item for item in data_reviews if produk_dicari.lower() in item ['produk'].lower()]

            if hasil: 
                print ('Review Ditemukan 🎀')
                headers = ["Nomor", "Username", "Produk", "Rating", "Komentar"]
                table = [[reviews['nomor'], reviews['username'], reviews['produk'], reviews['rating'], reviews['komentar']] for reviews in hasil]
                print(tabulate(table, headers=headers, tablefmt="double_grid", colalign=("left", "left", "left", "left")))
            else:
                print('Review yang kamu cari tidak ditemukan!')
        
        elif pilih_submenu == '5':
            menu_utama()

        elif pilih_submenu == '6': #Kondisi jika user memilih sub menu 5 (Logout)
            checker_logout= input(f"Apakah anda yakin ingin logout dari akun '{user}' (ya/tidak)?").lower()
            if checker_logout == 'ya':
                print(f"🔓 Anda berhasil logout dari akun '{user}' 💐!\n")
                halaman_pertama()
            elif checker_logout == 'tidak': 
                tampilkan_review()
            else:
                print('Pilihan tidak valid! Masukkan ya/tidak!')

        else:
            print("\n⚠️ Pilihan tidak valid! Masukkan angka 1-6!")


def tambah_review(user):
    while True:
        pilih_submenu = input(''' 🌸🌸 SocaBeauty 🌸🌸
            1. Tambah Review Produk
            2. Menu Utama
            3. Logout
                          
            Masukkan angka Submenu yang ingin dijalankan :
            ''')
        
        if pilih_submenu == '1': #Kondisi jika user memilih sub menu 1 (Menambah review produk baru)
            tampilkan_semua_reviews()
            print ('✨✨ Tambah Review Produk ✨✨')

            try:
                nomor_baru = int(input('Masukkan nomor review yang ingin ditambahkan: '))
            except ValueError:
                print("❌ Nomor harus berupa angka.\n")
                return
        
            for review in data_reviews:
                if review["nomor"] == nomor_baru:
                    print("❌ Nomor review sudah digunakan. Gunakan nomor yang lain.\n")
                    return

            produk = input('Nama Produk: ')

            try:
                rating = int(input("Rating (1-5): "))
                if rating < 1 or rating > 5:
                    print("❌ Rating harus antara 1 sampai 5.\n")
                    return
            except ValueError:
                print("❌ Input rating harus berupa angka.\n")
                return
            
            komentar = input("Komentar: ")

            headers = ["Nomor", "Username", "Produk", "Rating", "Komentar"]
            table = [[nomor_baru, user, produk, rating, komentar]]
            print(tabulate(table, headers=headers, tablefmt="double_grid", colalign=("left", "left", "left", "left")))

            konfirmasi = input("\nApakah kamu yakin ingin menambahkan review ini? (ya/tidak): ").lower()
            if konfirmasi != 'ya':
                print("❌ Penambahan review dibatalkan.\n")
                return
            
            data_reviews.append({"nomor": nomor_baru, "username": user, "produk": produk, "rating": rating, "komentar": komentar})

            print("✅ Review berhasil ditambahkan.\n")
            tampilkan_semua_reviews()
        
        elif pilih_submenu == '2':
            menu_utama()

        elif pilih_submenu == '3': #Kondisi jika user memilih sub menu 2 (Logout)
            checker_logout= input(f"Apakah anda yakin ingin logout dari akun '{user}' (ya/tidak)?").lower()
            if checker_logout == 'ya':
                print(f"🔓 Anda berhasil logout dari akun '{user}' 💐!\n")
                halaman_pertama()
            elif checker_logout == 'tidak': 
                tambah_review(user)
            else:
                print('Pilihan tidak valid! Masukkan ya/tidak!')

        else:
            print("\n⚠️ Pilihan tidak valid! Masukkan angka 1-3!")


def ubah_review(user):
   while True:
        pilih_submenu = input(''' 🌸🌸 SocaBeauty 🌸🌸 \n
            1. Ubah Review Produk
            2. Menu Utama
            3. Logout
                          
            Masukkan angka Submenu yang ingin dijalankan :
            ''')
        if pilih_submenu == '1':
            print(" ✨✍vUbah Review Saya ✨✍")
            tampilkan_semua_reviews()
            try:
                nomor_ubah = int(input("Masukkan nomor review yang ingin diubah: "))
            except ValueError:
                print("❌ Input ID harus berupa angka.\n")
                return
            
            review_ditemukan = None
            for review in data_reviews:
                if review["nomor"] == nomor_ubah:
                    review_ditemukan = review
                    break

            if review_ditemukan is None:
                print ('❌ Review tidak ditemukan.\n')
                ubah_review(user)
                
            if review_ditemukan["username"] != user:
                print("❌ Anda hanya bisa mengubah review milik Anda sendiri.\n")
                ubah_review(user)

            for review in data_reviews:
                if review["nomor"] == nomor_ubah:
                    if review["username"] != user:
                        print("❌ Anda hanya bisa mengubah review milik Anda sendiri.\n")
                        ubah_review(user)
                    while True:
                        headers = ["Nomor", "Username", "Produk", "Rating", "Komentar"]
                        table = [[review_ditemukan['nomor'], review_ditemukan['username'], review_ditemukan['produk'], review_ditemukan['rating'], review_ditemukan['komentar']]]
                        print(tabulate(table, headers=headers, tablefmt="double_grid", colalign=("left", "left", "left", "left")))
                        
                        print ('n\ Pilih Data yang ingin diubah: ')
                        print("1. Nama Produk")
                        print("2. Rating")
                        print("3. Komentar")

                        pilihan = input("Masukkan pilihan (1/2/3): ")

                        if pilihan == '1':
                            produk_baru = input("Masukkan nama produk baru: ")
                            review_ditemukan["produk"] = produk_baru
                            print("✅ Nama produk berhasil diperbarui.")
                        elif pilihan == '2':
                            try:
                                rating_baru = int(input("Masukkan rating baru (1-5): "))
                                if rating_baru < 1 or rating_baru > 5:
                                    print("❌ Rating harus antara 1 sampai 5.")
                                    continue
                                review_ditemukan["rating"] = rating_baru
                                print("✅ Rating berhasil diperbarui.")
                            except ValueError:
                                print("❌ Input rating harus berupa angka.")
                        elif pilihan == '3':
                            komentar_baru = input("Masukkan komentar baru: ")
                            review_ditemukan["komentar"] = komentar_baru
                            print("✅ Komentar berhasil diperbarui.")
                        else:
                            print("❌ Pilihan tidak valid.")
                            continue
                            
                        lanjut = input("Apakah ingin mengubah data lain? (ya/tidak): ").lower()
                        if lanjut != 'ya':
                            headers = ["Nomor", "Username", "Produk", "Rating", "Komentar"]
                            table = [[review_ditemukan['nomor'], review_ditemukan['username'], review_ditemukan['produk'], review_ditemukan['rating'], review_ditemukan['komentar']]]
                            print(tabulate(table, headers=headers, tablefmt="double_grid", colalign=("left", "left", "left", "left")))
                            print("✅ Review berhasil diperbarui.\n")
                            ubah_review(user)


        elif pilih_submenu == '2':
            menu_utama()

        elif pilih_submenu == '3': #Kondisi jika user memilih sub menu 3 (Logout)
            checker_logout= input(f"Apakah anda yakin ingin logout dari akun '{user}' (ya/tidak)?").lower()
            if checker_logout == 'ya':
                print(f"🔓 Anda berhasil logout dari akun '{user}' 💐!\n")
                halaman_pertama()
            elif checker_logout == 'tidak': 
                ubah_review(user)
            else:
                print('Pilihan tidak valid! Masukkan ya/tidak!')

        else:
            print("\n⚠️ Pilihan tidak valid! Masukkan angka 1-3!")


def hapus_review(user):
    while True:
        pilih_submenu = input(''' 🌸🌸 SocaBeauty 🌸🌸 \n
            1. Hapus Review Produk
            2. Menu Utama
            3. Logout
                          
            Masukkan angka Submenu yang ingin dijalankan :
            ''')
        if pilih_submenu == '1':
            print(" 🌸 HAPUS REVIEW 🌸 ")
            tampilkan_semua_reviews()
            try:
                nomor_hapus = int(input('Masukkan nomor review yang ingin dihapus 🔎 (Masukkan Angka): '))
            except ValueError:
                print("❌ Input nomor harus berupa angka.\n")
                return

            review_ditemukan = None
            for review in data_reviews:
                if review["nomor"] == nomor_hapus:
                    review_ditemukan = review
                    break

            if review_ditemukan is None:
                print ('❌ Review dengan nomor tersebut tidak ditemukan.\n')
                hapus_review(user)
                
            if review_ditemukan["username"] != user:
                print("❌ Anda hanya bisa menghapus review milik Anda sendiri.\n")
                hapus_review(user)
     
            print ('Hapus Review 🎀')
            headers = ["Nomor", "Username", "Produk", "Rating", "Komentar"]
            table = [[review_ditemukan['nomor'], review_ditemukan['username'], review_ditemukan['produk'], review_ditemukan['rating'], review_ditemukan['komentar']]]
            print(tabulate(table, headers=headers, tablefmt="double_grid", colalign=("left", "left", "left", "left")))

            checker_hapus = input('Apakah kamu yakin ingin menghapus? (ya/tidak): ').lower()
            if checker_hapus == 'ya':
                data_reviews.remove(review)
                print("✅ Review berhasil dihapus.\n")
                tampilkan_semua_reviews()
                
            elif checker_hapus == 'tidak': 
                hapus_review(user)

            else:
                print('❌ Penghapusan dibatalkan. Data yang kamu input bukan huruf y/n!') 
                hapus_review(user)      

        elif pilih_submenu == '2':
            menu_utama()

        elif pilih_submenu == '3': #Kondisi jika user memilih sub menu 3 (Logout)
            checker_logout= input(f"Apakah anda yakin ingin logout dari akun '{user}' (ya/tidak)?").lower()
            if checker_logout == 'ya':
                print(f"🔓 Anda berhasil logout dari akun '{user}' 💐!\n")
                halaman_pertama()
            elif checker_logout == 'tidak': 
                hapus_review(user)
            else:
                print('Pilihan tidak valid! Masukkan ya/tidak!')

        else:
            print("\n⚠️ Pilihan tidak valid! Masukkan angka 1-3!")


def menu_utama():
    while True:
        print("🌸🌸 SocaBeauty 🌸🌸")
        print("1. Tampilkan review produk")
        print("2. Tambah review")
        print("3. Ubah review saya")
        print("4. Hapus review saya")
        print("5. Logout")

        pilihan = input("Pilih opsi (1-5): ")
        print()
        if pilihan == "1":
            tampilkan_review()
        elif pilihan == "2":
            tambah_review(user)
        elif pilihan == "3":
            ubah_review(user)
        elif pilihan == "4":
            hapus_review(user)
        elif pilihan == "5":
            print(f"🔓 Anda berhasil logout dari akun '{user}' 💐!\n")
            break
        else:
            print("❌ Opsi tidak tersedia! Silahkan pilih 1-5!\n")


halaman_pertama()