from prettytable import PrettyTable

print("--------------------------------------------------")
print("                 Fathinatuz Zaina                 ")
print("                    2409116016                    ")
print("               Sistem Informasi A'24              ")
print("             Program Manajemen E-Surat            ")
print("--------------------------------------------------")

users = {
    "operator": "operator1",
    "user": "016"
}

list_surat = []

def login():
    print("\n--------------------------------------------------")
    print("    Selamat Datang Di Program Fathinatuz Zaina    ")
    print("--------------------------------------------------")
    
    role = input("\nRole Anda: ")
    password = input("Password: ")
    
    if role in users and users[role] == password:
        return role
    else:
        print("\nLogin yang Anda lalukan gagal.")
        return
    
def menu_operator():
    while True:
        print("\n------------------------------")
        print("|        Menu Operator       |")
        print("------------------------------")
        print("|   1   |     Buat Surat     |")
        print("|   2   |    Lihat Surat     |")
        print("|   3   |   Perbarui Surat   |")
        print("|   4   |     Hapus Surat    |")
        print("|   5   |       Keluar       |")
        print("------------------------------")
        
        pilihan = input("\nPilih Menu: ")

        if pilihan == "1":
            buat_surat()
        elif pilihan == "2":
            lihat_surat()
        elif pilihan == "3":
            perbarui_surat()
        elif pilihan == "4":
            hapus_surat()
        elif pilihan == "5":
            break
        else:
            print("\nPilihan Tidak Tersedia")

def buat_surat():
    Nama = input("Masukkan Nama Surat: ")
    Isi = input("Masukkan Isi Surat: ")
    list_surat.append({"Nama": Nama, "Isi": Isi})
    print("\nSurat Telah Berhasil Dibuat")

def lihat_surat():
    if not list_surat:
        print("\nSurat Tidak Ditemukan")
        return
    
    table = PrettyTable()
    table.field_names = ["Nama Surat", "Isi Surat"]

    for surat in list_surat:
        table.add_row([surat["Nama"], surat["Isi"]])

    print(table)

def perbarui_surat():
    Nama = input("\nMasukkan Nama Surat yang Ingin diperbarui: ")
    for surat in list_surat:
        if surat["Nama"] == Nama:
            baru = input("Masukkan Isi Surat yang Terbaru: ")
            surat["Isi"] = baru
            print("\nSurat Telah Berhasil diperbarui")
            return
    print("\nMaaf, Surat Tidak Ditemukan")

def hapus_surat():
    Nama = input("\nMasukkan Nama Surat yang Ingin dihapus: ")
    for surat in list_surat:
        if surat["Nama"] == Nama:
            list_surat.remove(surat)
            print("\nSurat Berahsil Dihapus")
            return
    print("\nMaaf, Surat Tidak Ditemukan")

def menu_user():
    while True:
        print("\n------------------------------")
        print("|          Menu User         |")
        print("------------------------------")
        print("|   1   |     Lihat Surat    |")
        print("|   2   |        Keluar      |")
        print("------------------------------")

        pilihan = input("\nPilih Menu: ")

        if pilihan == "1":
            lihat_surat()
        elif pilihan == "2":
            break
        else:
            print("\nPilihan Tidak Tersedia")

def main():
    while True:
        role = login()
        if role == "operator":
            menu_operator()
        elif role == "user":
            menu_user()
        else:
            print("Silahkan Coba Lagi^^")
        
        melanjutkan = input("Apakah Anda Ingin Keluar?(y/n): ")
        if melanjutkan.lower()!= 'n':
            print("Terimakasih Telah Menggunakan Program ini^^")
            break

if __name__ == "__main__":
    main()